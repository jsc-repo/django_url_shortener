from django.db import models

# Create your models here.
class Question(models.Model):
    original_url = models.URLField(max_length=256)
    hash = models.CharField(max_length=10)
    created_at = models.DateTimeField("created at", auto_now_add=True)

    def __str__(self) -> str:
        return self.original_url
