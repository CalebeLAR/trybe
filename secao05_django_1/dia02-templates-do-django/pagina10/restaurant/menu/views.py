from django.shortcuts import render
from menu.models import Recipe


def index(request):
    context = {"recipes": Recipe.objects.all()}
    return render(request, "home.components.html", context=context)
