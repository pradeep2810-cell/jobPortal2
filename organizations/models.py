from django.db import models
from accounts.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    type = models.CharField(max_length=100,
                            choices=[('Education', 'Education'),
                                     ('IT', 'IT'),
                                     ('Consultancy', 'Consultancy'),
                                     ('NGO/INGO', 'NGO/INGO'),
                                     ('Other', 'Other'),
                                     ])
    details = models.TextField()
    logo = models.ImageField(upload_to='organizations')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categorie'


class OrgUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
