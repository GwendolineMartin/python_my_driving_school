from django.db import models

# Create your models here.
class User(models.Model):
    prenom = models.CharField(max_length=30, null=True)
    nom = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50)
    mdp = models.CharField(max_length=10)
    age = models.DateField()
    adresse = models.CharField(max_length=50, null=True)
    departement = models.CharField(max_length=50, null=True)
    ville = models.CharField(max_length=50, null=True)
    telephone = models.IntegerField()
    typeUser = models.IntegerField()
    id_instructor = models.IntegerField(null=True)
    # date_creation  =  models.DateTimeField(default=timezone.now(), blank=True, verbose_name="Date création") 

class Planning(models.Model):
    date = models.DateTimeField()     
    creneau = models.TimeField()
    lieux = models.CharField(max_length=50)
    id_student = models.ForeignKey(User, on_delete=models.CASCADE)
    id_instructor = models.ForeignKey(User, on_delete=models.CASCADE)

class Forfait(models.Model):
    newHeures = models.IntegerField()
    totalHeures = models.IntegerField()
    id_student = models.IntegerField()