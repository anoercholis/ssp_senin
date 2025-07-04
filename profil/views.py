from django.shortcuts import render
from .models import About, Feature
from .forms import FormBarang

# Create your views here.
def home(request):
    about = About.objects.first()
    feature = Feature.objects.first()

    data = {
        'about':about,
        'feature':feature,
        
    }
    return render(request,'index.html', data)

def berita(request):
    return render(request,'berita.html')

def form_brg(request):
    from_brg=FormBarang()
    return render(request,'tambah_brg.html', {'form_brg':from_brg})
