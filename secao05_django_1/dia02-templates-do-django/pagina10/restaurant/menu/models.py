from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f"{self.name}"
    pass
