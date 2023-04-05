from django.shortcuts import render
from .forms import UploadFileForm


def csv_loader(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        csv_file = request.FILES['file']

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")

        context = {
            'filename': f'{csv_file}'
        }

        # loop over the lines and save them to db via model
        for line in lines:
            print(line)

        return render(request, 'csv_loader/csv_loader.html', context)

    else:

        return render(request, 'csv_loader/csv_loader.html')

