from django.db import models
from django.utils import timezone


class Address(models.Model):
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num = models.IntegerField()
    num2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    save_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name