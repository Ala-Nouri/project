from django.contrib import admin
from django.contrib.admin import filters
from django.forms import models
from .models import club, user,eventc

# Register your models here.



@admin.register(eventc)
class eventadmin(admin.ModelAdmin):
    list_display=('title','status','date')
    search_fields=('title',)
    ordering =('-add_date',)



@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=('first_name','last_name','is_club')
    search_fields=('first_name','last_name',)
    list_filter=('is_club',)
    ordering =('first_name',)
    

@admin.register(club)
class clubadmin(admin.ModelAdmin):
    list_display=('name','chef_id')
