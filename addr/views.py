from django.shortcuts import render
from .models import Address
from django.utils import timezone


def addr_list(request):
    addrs = Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/addr_list.html', {'addrs':addrs})

