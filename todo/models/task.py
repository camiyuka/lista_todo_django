from django.db import models
from .category import CategoryEntity

class TaskEntity(models.Model):
  name = models.CharField(max_length=64)
  description = models.TextField()
  percent = models.IntegerField()
  state = models.BooleanField(default=True)
  category = models.ForeignKey(CategoryEntity, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return "Task [%i - %s - %d - %r]" % (self.id, self.name, self.percent, self.state)