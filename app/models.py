from django.db import models

# Create your models here.
class App(models.Model):
    Name=models.CharField(max_length=15, unique=True)
    URL=models.URLField(max_length=200)
    price=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.Name
