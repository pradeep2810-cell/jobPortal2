from django.db import models
from organizations.models import Organization


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    details = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=100,
                            choices=[('Full Time', 'Full Time'),
                                     ('Part Time', 'Part Time')
                                     ], default='Full Time')
    desc = models.TextField()
    requirement = models.TextField()
    salary = models.FloatField()
    deadline = models.DateField()
    status = models.BooleanField(default=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
