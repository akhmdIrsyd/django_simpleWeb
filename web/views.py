from django.shortcuts import render

# Create your views here.
def index(request):
    #Data_siswa = data_siswa.objects.all()
    context = {
    }
    return render(request, 'web/index.html')