from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .models import Post, Entry
from .forms import PostForm,EntryForm

# Create your views here.
def index(request):
    """Strona główna"""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

@login_required
def post(request, post_id):
    """Strona z wpisami do wybranego postu"""
    post = Post.objects.get(id=post_id)
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}

    return render(request, 'blog/post.html', context)

@login_required
def new_post(request):
    """Strona do dodawania posta"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blog:index')
    context = {'form':form}

    return render(request, 'blog/new_post.html', context)

@login_required
def new_entry(request, post_id):
    """Strona dodawania wpisu do posta"""
    post = Post.objects.get(id=post_id)
    check_topic_owner(post.owner, request.user)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post
            new_entry.save()
            return redirect('blog:post', post_id=post_id)
    context = {'post':post,'form':form}

    return render(request, 'blog/new_entry.html',context)

@login_required
def edit_entry(request, entry_id):
    """Strona edycji wpisu w poście"""
    entry = Entry.objects.get(id=entry_id)
    post = entry.post
    check_topic_owner(post.owner, request.user)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post', post_id = post.id)
    context = {'entry':entry,'post':post,'form':form}
    
    return render(request, 'blog/edit_entry.html', context)


def check_topic_owner(postOwner, user):
    if postOwner != user:
        raise Http404
