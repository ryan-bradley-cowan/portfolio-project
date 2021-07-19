from django.db import models

class Blog(models.Model):
    # these field types come from https://docs.djangoproject.com/en/3.2/ref/models/fields/
    # title, pub_date, body, image
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
