from django.contrib import admin
from .models import Repository, CodeFile

admin.site.register(Repository)
admin.site.register(CodeFile)