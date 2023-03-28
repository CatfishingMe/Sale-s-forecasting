from django.shortcuts import render


def csv_loader(request):
    return render(request, 'csv_loader/csv_loader.html')
