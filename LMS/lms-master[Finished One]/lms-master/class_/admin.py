from django.contrib import admin
from .models import Class,ClassJoined,Comment,Stream
# Register your models here.
admin.site.register([Class,Comment,Stream,ClassJoined])
