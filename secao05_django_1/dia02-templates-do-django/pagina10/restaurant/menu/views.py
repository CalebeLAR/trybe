from django.shortcuts import render
from menu.models import Recipe


def index(request):
    context = {"recipes": Recipe.objects.all()}
    return render(request, "home.html", context=context)


def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {
        "recipe_name": recipe.name,
        "recipe_id": id,
        "ingredients": recipe.ingredients.split(" "),
        "instructions": recipe.instructions.split(" "),
        "image_url": recipe.image,
    }

    return render(request, "details.html", context=context)


def delete(request, id):
    Recipe.objects.get(id=id).delete()
    context = {"recipes": Recipe.objects.all()}
    return render(request, "home.html", context=context)
