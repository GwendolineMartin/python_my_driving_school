from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Rdv
from .models import Forfait
from .forms import RdvForm


# Create your views here.


def rdv_list(request):
    rdv = Rdv.objects.all()
    return render(request, 'intra/rdv_list.html', {'rdvs': rdv})


def rdv_detail(request, pk):
    rdv = get_object_or_404(Rdv, pk=pk)
    return render(request, 'intra/rdv_detail.html', {'rdv': rdv})


def rdv_create(request):
    if request.method == "POST":
        form = RdvForm(request.POST)
        if form.is_valid():
            rdv = form.save()
            rdv.save()
            return redirect('rdv_dedirectTo', pk=rdv.pk)
    else:
        form = RdvForm()
    return render(request, 'intra/rdv_edit.html', {'form': form})


def rdv_edit(request, pk):
    rdv = get_object_or_404(Rdv, pk=pk)
    if request.method == "POST":
        form = RdvForm(request.POST, instance=rdv)
        if form.is_valid():
            rdv = form.save()
            rdv.save()
            return redirect('rdv_detail', pk=rdv.pk)
    else:
        form = RdvForm(instance=rdv)
    return render(request, 'intra/rdv_edit.html', {'form': form})


def rdv_remove(request, pk):
    rdv = get_object_or_404(Rdv, pk=pk)
    rdv.delete()
    return redirect('rdv_list')


def forfait_list(request):
    forfait = Rdv.objects.all()
    return render(request, 'intra/forfait_list.html', {'forfaits': forfait})


def forfait_detail(request, pk):
    forfait = get_object_or_404(Rdv, pk=pk)
    return render(request, 'intra/forfait_detail.html', {'forfait': forfait})


def forfait_create(request):
    if request.method == "POST":
        form = RdvForm(request.POST)
        if form.is_valid():
            forfait = form.save()
            forfait.save()
            return redirect('forfait_dedirectTo', pk=forfait.pk)
    else:
        form = RdvForm()
    return render(request, 'intra/forfait_edit.html', {'form': form})


def forfait_edit(request, pk):
    forfait = get_object_or_404(Rdv, pk=pk)
    if request.method == "POST":
        form = RdvForm(request.POST, instance=forfait)
        if form.is_valid():
            forfait = form.save()
            forfait.save()
            return redirect('forfait_detail', pk=forfait.pk)
    else:
        form = RdvForm(instance=forfait)
    return render(request, 'intra/forfait_edit.html', {'form': form})


def forfait_remove(request, pk):
    forfait = get_object_or_404(Rdv, pk=pk)
    forfait.delete()
    return redirect('forfait_list')
