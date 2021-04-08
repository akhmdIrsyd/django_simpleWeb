from django.shortcuts import render, redirect, HttpResponse

from .models import agenda,berita,galery,kontak
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

def detail_berita(request):
    #Data_berita = berita.objects.order_by("-id")[:4]
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def detail_agenda(request):
    #Data_berita = berita.objects.order_by("-id")[:4]
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def Berita(request):
    #Data_berita = berita.objects.order_by("-id")
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def Galery(request):
    #Data_berita = berita.objects.order_by("-id")
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)

def agenda(request):
    #Data_berita = berita.objects.order_by("-id")
    context = {
        #'rows1':Data_berita,
    }
    return render(request, 'web/detail_berita.html',context)