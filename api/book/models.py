from django.db import models

class Auther(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    published_at = models.DateField()
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    