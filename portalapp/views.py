from django.shortcuts import render

# Create your views here.
from portalapp.models import HydJob
from portalapp.models import PuneJob
from portalapp.models import BangaloreJob
from portalapp.models import ChennaiJob
from portalapp.models import MumbaiJob


# Create your views here.

def job_view(request):
    jobs = HydJob.objects.all()

    hb_tech = {
        'name':'HBTECHNOLOGY',

    }
    return render(request, 'tempapp/index.html', hb_tech)

def login_view(request):
    user_info = {
        "username":"hushen.beg",
        "password":"doche@123"
    }
    return render(request, 'tempapp/login.html', user_info)

def hyd_jobs(request):
    jobs = HydJob.objects.all()
    return render(request, 'tempapp/hyd.html', {'jobs':jobs})

def pune_jobs(request):
    jobs = PuneJob.objects.all()
    return render(request, 'tempapp/pune.html', {'jobs':jobs})

def chennai_jobs(request):
    jobs = ChennaiJob.objects.all()
    return render(request, 'tempapp/chennai.html', {'jobs':jobs})

def bangolore_jobs(request):
    jobs = BangaloreJob.objects.all()
    return render(request, 'tempapp/bangalore.html', {'jobs':jobs})

def mumbai_jobs(request):
    jobs = MumbaiJob.objects.all()
    return render(request, 'tempapp/mumbai.html', {'jobs':jobs})

