from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from django.utils import timezone
from .forms import AddrForm


def con_list(request):
    cons = Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'addr/con_list.html', {'cons':cons})


def con_detail(request, pk):
    con = get_object_or_404(Address, pk=pk)
    return render(request, 'addr/con_detail.html', {'con':con})


def con_new(request):
    if request.method == "POST":
        form = AddrForm(request.POST)
        if form.is_valid():
            con = form.save(commit=False)
            con.writer = request.user
            con.published_date = timezone.now()
            con.save()
            return redirect('addr:con_detail', pk=con.pk)
    else:
        form=AddrForm
    return render(request, 'addr/con_edit.html', {'form':form})


def con_edit(request, pk):
    con = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddrForm(request.POST, instance=con)
        if form.is_valid():
            con = form.save(commit=False)
            con.writer = request.user
            con.published_date = timezone.now()
            con.save()
            return redirect('addr:con_detail', pk=con.pk)
    else:
        form=AddrForm(instance=con)
    return render(request, 'addr/con_edit.html', {'form':form})
