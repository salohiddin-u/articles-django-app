from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.TextField()
    text = models.TextField()
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title