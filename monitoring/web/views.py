from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #TODO: Logic buat nampilin piutang dan omsets
    return render(request, 'web/index.html')

def data_master_cabang(request):
    return render(request, 'web/datamaster_cabang.html')

def data_master_pengguna(request):
    return render(request, 'web/pengguna.html')

def monitoring(request):
    return render(request, 'web/monitoring.html')