from django.db import models
from django.utils import timezone
from jobs.models import Job
from jobseekers.models import JobSeeker


class Application(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=100,
                              choices=[('Submitted', 'Submitted'),
                                       ('On Review', 'On Review'),
                                       ('Selected', 'Selected'),
                                       ('Waiting Listed', 'Waiting Listed'),
                                       ('Rejected', 'Rejected'),
                                       ], default='Submitted')

    def __str__(self):
        return f'{ self.jobseeker.user.username } - { self.job.title }'