from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "featured", "created_at")
    list_filter = ("featured",)
    search_fields = ("user__username", "text")
