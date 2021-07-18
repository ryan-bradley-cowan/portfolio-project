from django.contrib import admin

from .models import Job

# in the jobs app this will make a jobs model visually in the admin login
admin.site.register(Job)
