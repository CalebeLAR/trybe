from django.urls import path
from menu.views import index, recipe_details, delete

urlpatterns = [
    path("", index, name="index"),
    path("recipe/<int:id>", recipe_details, name="details-page"),
    path("recipe/<int:id>/delete", delete, name="delete-page"),
]
