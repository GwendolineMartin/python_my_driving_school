from django.shortcuts import render

# Create your views here.


def rdv_list(request):
    return render(request, 'intra/rdv_list.html', {})
