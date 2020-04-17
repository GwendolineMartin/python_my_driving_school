from django import forms
from .models import Rdv
from .models import Forfait


class RdvForm(forms.ModelForm):

    class Meta:
        model = Rdv
        fields = ('date', 'start_time', 'end_time',
                  'lieu', 'id_student', 'id_instructor',)


class ForfaitForm(forms.ModelForm):

    class Meta:
        model = Forfait
        fields = ('newHeures', 'totalHeures', 'id_student',)
