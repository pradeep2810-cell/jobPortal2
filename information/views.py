from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from applications.models import Application
from information.models import Information
from jobs.models import Job
from jobseekers.models import JobSeeker
from organizations.models import Organization


def show_home(request):
    org = Organization.objects.all()
    job = Job.objects.count()
    candidates = JobSeeker.objects.count()
    filled = Application.objects.filter(status='Selected').count()
    stats = [candidates, job, filled, len(org)]
    jobs = Job.objects.order_by('-id')[:10]
    return render(request, 'index.html', {'organizations': org, 'stats': stats, 'jobs': jobs})


def show_about(request):
    # information = Information.objects.all()
    # information = Information.objects.filter(id=2)
    # information = Information.objects.get(pk=2)
    information = Information.objects.filter(section__title='About')
    return render(request, 'about.html', {'information': information})


def show_contacts(request):
    info = Information.objects.filter(section__title='Contacts')
    # info = Information.objects.filter(section_id=2)
    return render(request, 'contacts.html', {'info': info})


def show_policy(request):
    return HttpResponse('This is Policy Page')
