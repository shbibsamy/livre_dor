from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["email", "comment"]
    readonly_fields = ["email"]