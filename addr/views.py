from django.shortcuts import render, get_object_or_404
from .models import Address
from django.utils import timezone


def con_list(request):
    cons = Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'addr/con_list.html', {'cons':cons})


def con_detail(request, pk):
    con = get_object_or_404(Address, pk=pk)
    return render(request, 'addr/con_detail.html', {'con':con})