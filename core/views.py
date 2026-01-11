from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProfile, Recommendation
from .forms import RunPlanForm, ProfileForm
from .utils import build_risk_graph


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()

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

    recommendations = Recommendation.objects.filter(
        run_plan__profile=profile
    ).select_related("run_plan").order_by("run_plan__planned_start")

    graph = build_risk_graph(recommendations)

    return render(
        request,
        "core/recommendation_list.html",
        {"recommendations": recommendations, "graph": graph},
    )
