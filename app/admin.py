from django.contrib import admin

from app.models import Author, Blog

admin.site.register([Author, Blog])
