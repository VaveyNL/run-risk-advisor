from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RunPlan, Recommendation, UserProfile
from .services.weather import get_weather
from .services.air_quality import get_air_quality
from .services.risk import calculate_risk


def generate_recommendation(run_plan):
    profile = run_plan.profile
    city = profile.city

    if not city:
        return

    weather = get_weather(city.latitude, city.longitude)
    air = get_air_quality(city.latitude, city.longitude)

    risk_score, risk_level, explanation = calculate_risk(
        run_plan=run_plan,
        weather=weather,
        air=air,
        profile=profile,
    )

    Recommendation.objects.update_or_create(
        run_plan=run_plan,
        defaults={
            "risk_score": risk_score,
            "risk_level": risk_level,
            "explanation": explanation,
        }
    )


@receiver(post_save, sender=RunPlan)
def on_run_plan_save(sender, instance, **kwargs):
    generate_recommendation(instance)


@receiver(post_save, sender=UserProfile)
def on_profile_change(sender, instance, **kwargs):
    for plan in instance.run_plans.all():
        generate_recommendation(plan)
