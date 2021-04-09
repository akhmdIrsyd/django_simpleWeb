from django.shortcuts import render, redirect, HttpResponse

from .models import agenda,berita,galery,kontak
from .forms import KontakForm
# Create your views here.
def index(request):
    banner1 =  berita.objects.order_by("-id")[:1]
    banner2 = berita.objects.order_by("-id")[:2]
    data_berita= berita.objects.order_by("-id")[:3]
    data_galeri= galery.objects.order_by("-id")[:6]
    context = {
        'rows1':banner1,
        'rows2':banner2,
        'rows3':data_berita,
        'rows4':data_galeri,
    }
    return render(request, 'web/index.html',context)

def detail_berita(request, pk):
    data_berita = berita.objects.get(id=pk)
    context = {
        'rows1':data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def detail_agenda(request):
    #Data_berita = berita.objects.order_by("-id")[:4]
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def About(request):
    #Data_berita = berita.objects.order_by("-id")
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/about.html',context)

def Berita(request):
    data_berita= berita.objects.order_by("-id")
    context = {
        'rows1':data_berita,
    }
    return render(request, 'web/berita.html',context)

def Galery(request):
    data_galeri= galery.objects.order_by("-id")
    context = {
        'rows1':data_galeri,
    }
    return render(request, 'web/galery.html',context)

def Agenda(request):
    #Data_berita = berita.objects.order_by("-id")
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def Kontak(request):
    if request.method == 'POST':
        form = KontakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontak')
    else:
        form = KontakForm()
    context = {
        'form': form,
    }
    return render(request, 'web/kontak.html', context)