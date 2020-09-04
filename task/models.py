from django.db import models

# Create your models here.
class Task(models.Model):
  """Model definition for Task."""
  title = models.CharField(max_length=255)
  date = models.DateTimeField(  auto_now_add=True)
  completed = models.BooleanField(default=False)
  # TODO: Define fields here

  class Meta:
    """Meta definition for Task."""
    ordering= ['completed','date']
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'

  def __str__(self):
    """Unicode representation of Task."""
    return self.title

  def get_absolute_url(self):
    """Return absolute url for Task."""
    return ('')

  # TODO: Define custom methods here
