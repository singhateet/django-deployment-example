from django.shortcuts import render
from django.conf import settings
import os

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        file_path = os.path.join(settings.STATIC_ROOT, csv_file.name)
        with open(file_path, 'wb') as f:
            for chunk in csv_file.chunks():
                f.write(chunk)
        my_dict = {
            'file_name': csv_file.name,
            'file_size': csv_file.size,
        }
        return render(request, 'upload_success.html', context=my_dict)
    return render(request, 'upload_form.html')
