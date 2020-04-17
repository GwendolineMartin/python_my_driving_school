from django.db import models
from django.contrib.auth.models import User

# class Creneaux(models.Model):
# creneau = models.CharField(max_length=10)

class Rdv(models.Model):
    date = models.DateField()
    # creneau = models.ManyToManyField(Creneaux)
    start_time = models.TimeField()
    end_time = models.TimeField()
    lieu = models.CharField(max_length=50)
    id_student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student')
    id_instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='instructor')

    # class Meta:
    # verbose_name = _('rdv')
    # ordering = ['start', 'end']

    def publish(self):
        self.save()

    def __str__(self):
        return self.lieu


class Forfait(models.Model):
    newHeures = models.IntegerField()
    totalHeures = models.IntegerField()
    id_student = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return '%s %s' % (self.totalHeures, self.newHeures)