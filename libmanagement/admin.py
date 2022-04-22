from django.contrib import admin

from libmanagement.models import Author, Category, Books 

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Books)
