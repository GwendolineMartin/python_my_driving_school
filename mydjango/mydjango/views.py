from django.http import HttpResponse


def home(request):
    return HttpResponse('Coucou les copines, on est sur la HomePage')
