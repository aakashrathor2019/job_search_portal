from django.contrib import admin
from .models import ProfileUser

# Register your models here.
@admin.register(ProfileUser)
class UserPrpfile(admin.ModelAdmin):
  list_display=['username','pro_image','contact','gender','qualification']


