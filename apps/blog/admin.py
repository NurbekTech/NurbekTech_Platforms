from django.contrib import admin
from . import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")


admin.site.register(models.Post, PostAdmin)
