from django.contrib import admin
from .models import Applicants, result, customUser

# Register your models here.
admin.site.register(Applicants)
admin.site.register(result)
admin.site.register(customUser)