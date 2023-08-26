from django.contrib import admin
from .models import *
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=('name','discription','postimage','datetime')

class webadmin(admin.ModelAdmin):
    list_display=('name','username','mobile','email')

admin.site.register(webuser, webadmin)
admin.site.register(post, postadmin)