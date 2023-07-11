from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Section(models.Model):
    title = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)
    details = RichTextUploadingField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
