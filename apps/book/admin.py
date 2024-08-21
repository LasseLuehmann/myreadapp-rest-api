from django.contrib import admin
from .models import Book,Author,Tag,BookAuthor

# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(BookAuthor)