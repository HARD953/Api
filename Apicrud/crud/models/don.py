from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class DonateurId(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    prenom=models.CharField(max_length=100,blank=False)
    Email=models.EmailField(max_length=100,blank=False)
    mdp=models.CharField(max_length=100,blank=False)

class DonateurAno(models.Model):
    adresse=models.CharField(max_length=100,blank=False)

class DonateurEta(DonateurId):
    Ministere=models.CharField(max_length=100,blank=False)

class EffectuerDon(models.Model):
    cible=models.CharField(max_length=100,blank=True)
    categorie=models.CharField(max_length=100,blank=True)
    nature=models.CharField(max_length=100,blank=True)
    lieu_reception=models.CharField(max_length=100,blank=True)
    photo=models.CharField(max_length=100,blank=True)
    Etat=models.CharField(max_length=100,blank=True)
    create=models.DateTimeField(auto_now_add=True)
    montant=models.FloatField(max_length=100,blank=True)
    provider=models.CharField(max_length=100,blank=True)
    class Meta:
        abstract=True

class EffectuerDonId(EffectuerDon):
    donateur=models.ForeignKey(DonateurId,on_delete=models.CASCADE)

class EffectuerDonAno(EffectuerDon):
    donateur=models.ForeignKey(DonateurAno,on_delete=models.CASCADE)

class EffectuerDonEta(EffectuerDon):
    donateur=models.ForeignKey(DonateurEta,on_delete=models.CASCADE)