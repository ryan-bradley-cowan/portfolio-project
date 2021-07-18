from django.db import models

# migrate tells db the fields we want (i.e. db setup)

class Job(models.Model):
    # these field types come from https://docs.djangoproject.com/en/3.2/ref/models/fields/
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)