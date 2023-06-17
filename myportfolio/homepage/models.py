from django.db import models

# Create your models here.
class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    year_month = models.DateField()

    def __str__(self):
        return self.title    