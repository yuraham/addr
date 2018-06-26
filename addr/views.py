from django.shortcuts import render, get_object_or_404, redirect
from .models import Address, AddrMemo
from django.utils import timezone
from .forms import AddrForm, MemoForm
from django.contrib.auth.decorators import login_required


def con_list(request):
    cons = Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'addr/con_list.html', {'cons':cons})


def con_detail(request, pk):
    con = get_object_or_404(Address, pk=pk)
    return render(request, 'addr/con_detail.html', {'con':con})


@login_required
def con_secret_addr(request, pk):
    con = get_object_or_404(Address, pk=pk)
    con.secret()
    return redirect('addr:con_detail', pk=pk)


@login_required
def con_new(request):
    if request.method == "POST":
        form = AddrForm(request.POST)
        if form.is_valid():
            con = form.save(commit=False)
            con.writer = request.user
            con.save()
            return redirect('addr:con_detail', pk=con.pk)
    else:
        form=AddrForm
    return render(request, 'addr/con_edit.html', {'form':form})


@login_required
def con_edit(request, pk):
    con = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddrForm(request.POST, instance=con)
        if form.is_valid():
            con = form.save(commit=False)
            con.writer = request.user
            con.save()
            return redirect('addr:con_detail', pk=con.pk)
    else:
        form=AddrForm(instance=con)
    return render(request, 'addr/con_edit.html', {'form':form})


@login_required
def con_draft_list(request):
    cons = Address.objects.filter(published_date__isnull=True).order_by('save_date')
    return render(request, 'addr/con_draft_list.html', {'cons':cons})


@login_required
def con_publish(request, pk):
    con = get_object_or_404(Address, pk=pk)
    con.publish()
    return redirect('addr:con_detail', pk=pk)


@login_required
def con_remove(request, pk):
    con = get_object_or_404(Address, pk=pk)
    con.delete()
    return redirect('addr:con_list')


@login_required
def con_memo_new(request, pk):
    con = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memos = form.save(commit=False)
            memos.contact = con
            memos.save()
            return redirect('addr:con_detail', pk=con.pk)
    else:
        form = AddrMemo()
    return render(request, 'addr/con_memo_new.html', {'form':form})