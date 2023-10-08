from django.urls import path
from menu.views import index, recipe_details

urlpatterns = [
    path("", index, name="index"),
    path("recipe/<int:id>", recipe_details, name="details-page"),
]
