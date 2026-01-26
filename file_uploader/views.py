from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

from .models import UploadedFile

# Create your views here.
@login_required
def add_file(request):

    if request.method == "POST":
        custom_name = request.POST.get('name_of_package')
        request_file = request.FILES.get('document')
        if request_file:
            new_file = UploadedFile.objects.create(
                name=custom_name,
                file=request_file
            )
            return redirect('file_uploader:add_file')
    uploaded_files = UploadedFile.objects.all()
    context = {'files':uploaded_files}
    return render(request, 'file_uploader/add_file.html', context)

@login_required
def delete_file(request, file_id):
    file_record = get_object_or_404(UploadedFile, id=file_id)
    if request.method == 'POST':
        if file_record.file:
            file_record.file.delete()
        file_record.delete()
        
    return redirect('file_uploader:add_file')