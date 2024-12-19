from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    search_fields = 'id', 'name'


@admin.register(models.Contact)
class Contact(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone'
    ordering= '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    # list_display = 'first_name',

