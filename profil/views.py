from django.shortcuts import render
from .models import About
from .forms import FormBarang

# Create your views here.
def home(request):
    about = About.objects.first()
    return render(request,'index.html', {'about':about})

def berita(request):
    return render(request,'berita.html')

def form_brg(request):
    from_brg=FormBarang()
    return render(request,'tambah_brg.html', {'form_brg':from_brg})
