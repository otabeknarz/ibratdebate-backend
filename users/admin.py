from django.contrib import admin

from .models import User, Region, District


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "username", "created_at")
    list_filter = ("is_active",)
    ordering = ("-id",)
    date_hierarchy = "created_at"
    search_fields = ("username", "name", "first_name", "last_name", "id")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("-id",)
    date_hierarchy = "created_at"


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    search_fields = ("name",)
    ordering = ("-id",)
    date_hierarchy = "created_at"
