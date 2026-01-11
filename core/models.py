from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField("Город", max_length=100)
    latitude = models.DecimalField("Широта", max_digits=8, decimal_places=5)
    longitude = models.DecimalField("Долгота", max_digits=8, decimal_places=5)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    SENSITIVITY_CHOICES = [
        ("low", "Низкая"),
        ("medium", "Средняя"),
        ("high", "Высокая"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Пользователь"
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Город"
    )

    sensitivity_level = models.CharField(
        "Чувствительность",
        max_length=20,
        choices=SENSITIVITY_CHOICES,
        default="medium"
    )

    pm25_limit = models.PositiveIntegerField("Допустимый PM2.5", default=35)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"Профиль {self.user.username}"


class RunPlan(models.Model):
    INTENSITY_CHOICES = [
        ("low", "Маленькая"),
        ("medium", "Средняя"),
        ("high", "Высокая"),
    ]

    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="run_plans",
        verbose_name="Профиль"
    )

    planned_start = models.DateTimeField("Начало пробежки")
    duration_min = models.PositiveIntegerField("Длительность (минуты)")
    intensity = models.CharField("Интенсивность", max_length=20, choices=INTENSITY_CHOICES)

    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "План пробежки"
        verbose_name_plural = "Планы пробежек"
        ordering = ["-planned_start"]

    def __str__(self):
        return f"{self.profile.user.username} — {self.intensity}"


class Recommendation(models.Model):
    RISK_LEVELS = [
        ("low", "Низкий"),
        ("medium", "Средний"),
        ("high", "Высокий"),
    ]

    run_plan = models.OneToOneField(
        RunPlan,
        on_delete=models.CASCADE,
        related_name="recommendation",
        verbose_name="План пробежки"
    )

    risk_score = models.PositiveIntegerField("Риск (0–100)")
    risk_level = models.CharField("Уровень риска", max_length=20, choices=RISK_LEVELS)
    explanation = models.TextField("Пояснение")
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"

    def __str__(self):
        return f"Риск {self.risk_score}"
