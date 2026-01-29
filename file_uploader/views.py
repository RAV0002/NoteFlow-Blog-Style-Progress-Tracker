from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import UploadedFile

# Create your views here.
@login_required
def upload_file_view(request):

    if request.method == "POST":
        requested_files = request.FILES.getlist('document')
        for f in requested_files:
            UploadedFile.objects.create(
                name= f.name,
                file=f,
                owner=request.user
            )
        return redirect('file_uploader:upload_file_view')
    uploaded_files = UploadedFile.objects.filter(owner=request.user).order_by('-date_added')
    context = {'files':uploaded_files}
    return render(request, 'file_uploader/upload_file_site.html', context)

@login_required
def delete_file(request, file_id):
    file_record = get_object_or_404(UploadedFile, id=file_id)
    check_content_owner(file_record.owner, request.user)
    if request.method == 'POST':
        if file_record.file:
            file_record.file.delete()
        file_record.delete()
        
    return redirect('file_uploader:upload_file_view')

@login_required
def delete_all_files(request):
    if request.method == 'POST':
        uploaded_files = UploadedFile.objects.filter(owner=request.user)
        for f in uploaded_files:
            check_content_owner(f.owner, request.user)
            if f.file:
                f.file.delete()
            f.delete()
    return redirect('file_uploader:upload_file_view')


def check_content_owner(fileOwner, user):
    if fileOwner != user:
        raise Http404