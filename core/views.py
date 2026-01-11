from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .models import UserProfile
from .forms import RunPlanForm, ProfileForm, LoginForm


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})


@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, "core/profile.html", {"form": form})


@login_required
def create_run_plan(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = RunPlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.profile = profile
            plan.save()
            return redirect("/recommendations/")
    else:
        form = RunPlanForm()

    return render(request, "core/create_run_plan.html", {"form": form})


@login_required
def recommendation_list(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    recommendations = profile.run_plans.all().order_by("-planned_start")

    return render(
        request,
        "core/recommendation_list.html",
        {"recommendations": recommendations},
    )
