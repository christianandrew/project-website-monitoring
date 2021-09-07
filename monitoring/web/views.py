from django.contrib.auth.models import User
from django.http.request import HttpRequest
from .models import AkunBank, Cabang, Pelanggan, People, Penjualan
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    # TODO: Logic buat nampilin piutang dan omsets
    return render(request, 'web/index.html')


# datamaster/cabang/
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


def data_master_bank(request: HttpRequest):
    if request.method == 'GET':
        banks = AkunBank.objects.all().order_by('-id')
        ctx = {
            'banks': banks
        }
    else:
        d = request.POST
        id = d.get("id", None)
        nama_bank = d.get("nama_bank", None)
        nomor_rekening = d.get("nomor_rekening", None)
        nama_pemilik = d.get('nama_pemilik', None)
        if id:
            bank = AkunBank.objects.get(id=id)
        if 'edit' in d:
            bank: AkunBank = AkunBank.objects.get(id=id)
            bank.nama_bank = nama_bank
            bank.nomor_rekening = nomor_rekening
            bank.nama_pemilik = nama_pemilik
            bank.save()
        elif nama_pemilik:
            bank: AkunBank = AkunBank(nama_bank=nama_bank, nomor_rekening=nomor_rekening, nama_pemilik=nama_pemilik)
            bank.save()
        banks = AkunBank.objects.all().order_by('-id')
        ctx = {
            'banks': banks,
            'bank': bank,
            'edit': 'edit' in d
        }

    return render(request, 'web/datamaster_bank.html', ctx)


def data_master_pelanggan(request: HttpRequest):
    if request.method == 'GET':
        pelanggans = Pelanggan.objects.all().order_by('-id')
        ctx = {
            'pelanggans': pelanggans
        }
    else:
        d = request.POST
        id = d.get("id", None)
        nama = d.get("nama_perusahaan", None)
        alamat = d.get("alamat", None)
        kota = d.get("kota", None)
        telpon = d.get("telpon", None)
        nama_spv = d.get("nama_spv", None)
        telfon_spv = d.get("telfon_spv", None)
        edit = d.get("edit", None)
        if id:
            p = Pelanggan.objects.get(id=id)
        if edit:
            p: Pelanggan = Pelanggan.objects.get(id=id)
            p.nama_perusahaan = nama
            p.alamat = alamat
            p.kota = kota
            p.telpon = telpon
            p.nama_spv = nama_spv
            p.telfon_spv = telfon_spv
            p.save()
        elif nama:
            p: Pelanggan = Pelanggan(
                nama_perusahaan=nama,
                alamat=alamat,
                kota=kota,
                telpon=telpon,
                nama_spv=nama_spv,
                telfon_spv=telfon_spv
            )
            p.save()
        pelanggans = Pelanggan.objects.all().order_by('-id')
        ctx = {
            'pelanggans': pelanggans,
            'cabang': p,
            'edit': 'edit' in d

        }

    return render(request, 'web/datamaster_pelanggan.html', ctx)


def monitoring(request):
    return render(request, 'web/monitoring.html')


def admin_index(request):
    return render(request, 'web/admin_index.html')


def admin_penjualan(request):
    if request.method == 'GET':
        p = Penjualan.objects.all().order_by('-id')
        ctx = {
            'penjualans': p
        }
        return render(request, 'web/admin_penjualan.html', ctx)
    else:
        d = request.POST
        obj_id = d.get('id', None)
        edit = d.get('edit', None)
        resi = d.get("noresi", None)
        kota = d.get('kota', None)
        colly = d.get("colly", None)
        kg = d.get("kg", None)
        pengirim = d.get("pengirim", None)
        penerima = d.get("penerima", None)
        tujuan = d.get('tujuan', None)
        nominal = d.get('nominal', None)

        if obj_id:
            p = Penjualan.objects.get(id=obj_id)
        if edit:
            p.no_resi = resi
            p.kota = kota
            p.colly = colly
            p.kg = kg
            p. pengirim = pengirim
            p.penerima = penerima
            p.tujuan = tujuan
            p.nominal = nominal
            p.save()
            p = None
        all = Penjualan.objects.all().order_by('-id')
        ctx = {
            'penjualan': p,
            'penjualans': all
        }
        return render(request, 'web/admin_penjualan.html', ctx)


def admin_piutang(request):
    return render(request, 'web/admin_piutang.html')


def admin_addPenjualan(request):
    if request.method == 'GET':
        return render(request, 'web/admin_addPenjualan.html')
    else:
        d = request.POST
        resi = d.get("noresi", None)
        kota = d.get('kota', None)
        colly = d.get("colly", None)
        kg = d.get("kg", None)
        pengirim = d.get("pengirim", None)
        penerima = d.get("penerima", None)
        tujuan = d.get('tujuan', None)
        nominal = d.get('nominal', None)
        if resi:
            p = Penjualan(
                no_resi=resi,
                penerima=penerima,
                pengirim=pengirim,
                nominal=nominal,
                tujuan=tujuan,
                colly=colly,
                kg=kg,
                kota=kota
            )
            p.save()
        return redirect('/admindir/penjualan/')


def admin_piutangpelanggan(request):
    return render(request, 'web/admin_piutangpelanggan.html')


def admin_invoice(request):
    return render(request, 'web/admin_invoice.html')


def admin_pelunasan(request):
    return render(request, 'web/admin_pelunasan.html')
