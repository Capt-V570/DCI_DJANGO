from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):  # -> str:
        # return super().__str__()
        return f"title: {self.title}, desctiption: {self.description}"


# "Make migrations" -> Translate Python to SQL
