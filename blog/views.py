from django.shortcuts import render, redirect
from .models import Post, Entry
from .forms import PostForm,EntryForm

# Create your views here.
def index(request):
    """Strona główna"""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)
def post(request, post_id):
    """Strona z wpisami do wybranego postu"""
    post = Post.objects.get(id=post_id)
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}

    return render(request, 'blog/post.html', context)

def new_post(request):
    """Strona do dodawania posta"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    context = {'form':form}

    return render(request, 'blog/new_post.html', context)

def new_entry(request, post_id):
    post = Post.objects.get(id=post_id)
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

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    post = entry.post

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post', post_id = post.id)
    context = {'entry':entry,'post':post,'form':form}
    
    return render(request, 'blog/edit_entry.html', context)


