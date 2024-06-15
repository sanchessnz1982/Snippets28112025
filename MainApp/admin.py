from django.contrib import admin
from MainApp.models import Snippet, Comment


# Register your models here.
admin.site.register([Snippet, Comment])