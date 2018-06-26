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
    secret_addr = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def secret(self):
        self.secret = True
        self.save()

    def __str__(self):
        return self.name


class AddrMemo(models.Model):
    contact = models.ForeignKey('addr.Address', related_name='memos')
    author = models.CharField(max_length=200)
    text = models.TextField()
    secret_memo = models.BooleanField(default=False)

    def secret(self):
        self.secret = True
        self.save()

    def __str__(self):
        return self.text
