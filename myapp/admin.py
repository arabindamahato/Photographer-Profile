from django.contrib import admin
from . models import Photographer, Subscriber, Gallary, Content

# Register your models here.

admin.site.register(Photographer)
admin.site.register(Subscriber)
admin.site.register(Gallary)
admin.site.register(Content)