from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def login_view(request):
    return render(request, "core/login.html")


def profile(request):
    return render(request, "core/profile.html")


def create_run_plan(request):
    return render(request, "core/create_run_plan.html")


def recommendation_list(request):
    return render(request, "core/recommendation_list.html")
