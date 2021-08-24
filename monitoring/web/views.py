from django.contrib.auth.models import User
from django.http.request import HttpRequest
from .models import Cabang, People
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


def data_master_pengguna(request: HttpRequest):
    if request.method == 'GET':
        penggunas = People.objects.all()
        ctx = {
            'penggunas': penggunas
        }
    else:
        d = request.POST
        id = d.get("id", None)
        nama = d.get("nama", None)
        username = d.get("username", None)
        password = d.get('password', None)
        status = False
        people = People()
        if id:
            people = People.objects.get(id=id)
        if 'edit' in d:
            people: People = People.objects.get(id=id)
            assert nama is not None
            people.nama = nama.strip()
            assert username is not None
            people.user.username = username.strip()
            if password:
                people.user.set_password(password)
            people.save()
            status = True
        elif password:
            user = User.objects.create_user(username, 'none@none.com', password)
            user.first_name = nama
            user.profile.nama = nama
            user.profile.role = 2
            user.save()

            status = True
        penggunas = People.objects.all()
        ctx = {
            'penggunas': penggunas,
            'status': status,
            'cabang': people,
            'edit': 'edit' in d
        }    

    return render(request, 'web/datamaster_pengguna.html', ctx)

def monitoring(request):
    return render(request, 'web/monitoring.html')

def admin_index(request):
    return render(request,'web/admin_index.html')

def admin_penjualan(request):
    return render(request, 'web/admin_penjualan.html')

def admin_piutang(request):
    return render(request, 'web/admin_piutang.html')