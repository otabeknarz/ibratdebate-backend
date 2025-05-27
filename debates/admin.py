from django.contrib import admin

from .models import Debate, Ticket


@admin.register(Debate)
class DebateAdmin(admin.ModelAdmin):
    list_display = ("region", "district", "date", "time", "is_passed")
    list_filter = ("is_passed",)
    ordering = ("-created_at", "is_passed")
