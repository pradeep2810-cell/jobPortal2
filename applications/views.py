from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# @login_required
from applications.models import Application
from jobs.models import Job
from jobseekers.models import JobSeeker


def apply(request, jid):
    if request.user.is_authenticated:
        job = Job.objects.get(id=jid)
        jobseeker = JobSeeker.objects.get(user=request.user)
        app = Application.objects.filter(jobseeker=jobseeker).filter(job=job)
        if app:
            messages.success(request, 'Your application is already submitted !')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        application = Application(jobseeker=jobseeker, job=job)
        application.save()
        messages.success(request, 'Your application is submitted !')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.warning(request, 'Invalid Access, Login first !')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def myapplication(request):
    jobseeker = JobSeeker.objects.get(user=request.user)
    apps = Application.objects.filter(jobseeker=jobseeker)
    return render(request, 'myapps.html', {'apps': apps})
