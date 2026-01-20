from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from core.models import City, UserProfile, RunPlan

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        cities_data = [
            ("Москва", 55.7558, 37.6173),
            ("Екатеринбург", 56.8389, 60.6057),
            ("Санкт-Петербург", 59.9343, 30.3351),
            ("Казань", 55.7961, 49.1064),
            ("Краснодар", 45.0355, 38.9753),
            ("Волгоград", 48.7080, 44.5133),
            ("Ростов-на-Дону", 47.2357, 39.7015),
            ("Владивосток", 43.1155, 131.8855),
        ]

        cities = []
        for name, lat, lon in cities_data:
            city, created = City.objects.get_or_create(
                name=name,
                defaults={"latitude": lat, "longitude": lon, "is_active": True},
            )
            cities.append(city)

        self.stdout.write(self.style.SUCCESS(f"Cities ready: {City.objects.count()}"))

        base_password = "user12345!"

        for i in range(1, 11):
            username = f"user{i}"

            user, created = User.objects.get_or_create(username=username)

            if created:
                user.set_password(base_password)
                user.email = f"{username}@example.com"
                user.save()

            profile, _ = UserProfile.objects.get_or_create(user=user)

            profile.city = cities[(i - 1) % len(cities)]

            if i <= 3:
                profile.sensitivity_level = "low"
                profile.pm25_limit = 40
            elif i <= 7:
                profile.sensitivity_level = "medium"
                profile.pm25_limit = 35
            else:
                profile.sensitivity_level = "high"
                profile.pm25_limit = 25

            profile.save()

            RunPlan.objects.get_or_create(
                profile=profile,
                planned_start=timezone.now(),
                defaults={"duration_min": 30, "intensity": "medium"},
            )

        self.stdout.write(self.style.SUCCESS("Users + profiles + run plans seeded ✅"))
        self.stdout.write(self.style.WARNING("Login examples: user1 / user12345!"))
