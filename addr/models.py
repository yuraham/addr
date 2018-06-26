from django.db import models
from django.utils import timezone


class Address(models.Model):
    name = models.CharField(max_length=100)
    num = models.IntegerField()
    num2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    save_date = models.DateTimeField(default=timezone.now())
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    secret = models.BooleanField(default=False)

    def __str__(self):
        return self.name