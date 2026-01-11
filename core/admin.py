from django.contrib import admin
from .models import City, UserProfile, RunPlan, Recommendation


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "sensitivity_level", "pm25_limit")
    search_fields = ("user__username",)
    list_filter = ("city", "sensitivity_level")


@admin.register(RunPlan)
class RunPlanAdmin(admin.ModelAdmin):
    list_display = ("profile", "planned_start", "duration_min", "intensity")
    search_fields = ("profile__user__username",)
    list_filter = ("intensity",)
    ordering = ("-planned_start",)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("run_plan", "risk_score", "risk_level", "created_at")
    search_fields = ("run_plan__profile__user__username",)
    list_filter = ("risk_level",)
    ordering = ("-created_at",)
