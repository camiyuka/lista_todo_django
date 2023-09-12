from django.db import models

class CategoryEntity(models.Model):
  name = models.CharField(max_length=64)
  description = models.TextField()

  def __str__(self) -> str:
    return "Category [%i - %s]" % (self.id, self.name)