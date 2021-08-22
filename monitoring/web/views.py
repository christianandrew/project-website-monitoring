from django.http.request import HttpRequest
from .models import Cabang
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #TODO: Logic buat nampilin piutang dan omsets
    return render(request, 'web/index.html')

#datamaster/cabang/
def data_master_cabang(request: HttpRequest):
    if request.method == 'GET':
        cabangs = Cabang.objects.all().order_by('id')
        ctx = {
            'cabangs': cabangs
        }
        return render(request, 'web/datamaster_cabang.html', ctx)
    else:
        d = request.POST
        id = d.get("id", None)
        nama = d.get("nama", None)
        alamat = d.get("alamat", None)
        status = False
        if id:
            cabang = Cabang.objects.get(id=id)
        if 'edit' in d:
            cabang: Cabang = Cabang.objects.get(id=id)
            assert nama is not None
            cabang.nama = nama.strip()
            assert alamat is not None
            cabang.alamat = alamat.strip()
            cabang.save()
            status = True
        elif alamat:
            cabang: Cabang = Cabang(nama=nama, alamat=alamat)
            cabang.save()
            status = True
        cabangs = Cabang.objects.all().order_by('id')    
        ctx = {
            'status': status,
            'cabang': cabang,
            'cabangs': cabangs
        }     
            
        return render(request, 'web/datamaster_cabang.html', ctx)    

def data_master_pengguna(request):
    return render(request, 'web/pengguna.html')

def monitoring(request):
    return render(request, 'web/monitoring.html')

def admin_index(request):
    return render(request,'web/admin_index.html')

def admin_penjualan(request):
    return render(request, 'web/admin_penjualan.html')

def admin_piutang(request):
    return render(request, 'web/admin_piutang.html')