from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job


def show_jobs(request):
    jobs = Job.objects.filter(deadline__gte=datetime.now())
    return render(request, 'jobs.html', {'jobs': jobs})


def show_single_job(request, jid):
    job = Job.objects.get(id=jid)
    return render(request, 'job-single.html', {'job': job})


def show_job_by_category(request, category):
    jobs = Job.objects.filter(category_id=category)
    return render(request, 'jobs.html', {'jobs': jobs})


def show_job_by_search(request):
    key = request.GET['key']
    tp = request.GET['type']
    location = request.GET['location']
    # jobs = Job.objects.filter(Q(title__icontains=key) | Q(type__icontains=tp) | Q(organization__address__icontains=location))
    jobs = Job.objects.filter(title__icontains=key).filter(type__icontains=tp).filter(organization__address__icontains=location)
    return render(request, 'jobs.html', {'jobs': jobs})
