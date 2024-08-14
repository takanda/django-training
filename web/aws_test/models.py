from django.db import models


class Person(models.Model):
    id = models.BigIntegerField(primary_key=True)
    birthday = models.DateField(null=False)
