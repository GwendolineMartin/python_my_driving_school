from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Rdv
from .models import Forfait

# def index(request):
#     return HttpResponse("Hello, world. index intranet.")

def index(request):
    latest_question_list = Rdv.objects.order_by('-pub_date')[:5]
    template = loader.get_template('intranet/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'intranet/index.html', context)

def detail(request, question_id):
    rdv = get_object_or_404(Rdv, pk=question_id)
    return render(request, 'rdv/detail.html', {'rdv': rdv})
