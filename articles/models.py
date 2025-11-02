from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title