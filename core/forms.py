from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import RunPlan, UserProfile


class StyledFormMixin:
    def _style_fields(self):
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class RunPlanForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = RunPlan
        fields = ["planned_start", "duration_min", "intensity"]
        widgets = {
            "planned_start": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style_fields()


class ProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["city", "sensitivity_level", "pm25_limit"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style_fields()


class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style_fields()
