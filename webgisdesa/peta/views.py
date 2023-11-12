from django.shortcuts import render, redirect
from .models import Restoran
from django.contrib import messages

# Create your views here.
def LihatRestoran(request):
    SemuaRestoran = Restoran.objects.all()

    context = {
        'Semua_Restoran' : SemuaRestoran
    }

    return render (request, "peta/index.html", context)

# Views for CREATE
def createRestoran(request):
    return render(request, 'peta/create.html')

def simpan(request):
    restoran = Restoran()
    restoran.nama = request.POST.get('nama')
    restoran.lat = request.POST.get('lat')
    restoran.long = request.POST.get('long')
    restoran.jenis = request.POST.get('jenis')
    restoran.save()
    messages.success(request, "Restoran baru sudah ditambahkan!")
    return redirect('/peta/create')

# View untuk DELETE
def deleteRestoran(request, id):
    restoran = Restoran.objects.get(id = id)
    restoran.delete()
    messages.success(request, "Restoran berhasil dihapus")
    return redirect('/peta')

# View untuk UPDATE
def updateRestoran(request, id):
    restoran = Restoran.objects.get(id = id)
    return render(request, 'peta/update.html', {'restoran': restoran})

def update(request, id):
    restoran = Restoran.objects.get(id = id)
    restoran.nama = request.POST.get('nama')
    restoran.lat = request.POST.get('lat')
    restoran.long = request.POST.get('long')
    restoran.jenis = request.POST.get('jenis')
    restoran.save()
    messages.success(request, "Restoran sudah diupdate!")
    return redirect('/peta')
