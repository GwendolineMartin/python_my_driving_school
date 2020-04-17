from django.contrib import admin

from .models import Rdv
from .models import Forfait

admin.site.register(Rdv)
admin.site.register(Forfait)