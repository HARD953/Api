from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Personne(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    prenom=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    ethnie=models.CharField(max_length=100,blank=False)
    numero_cni=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    age=models.PositiveBigIntegerField(blank=False)
    class Meta:
        abstract=True
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)

class AgentRecenseur(Personne):
    id=models.BigAutoField(primary_key=True)
    created=models.DateTimeField(auto_now_add=True)
    
class Localite(models.Model):
    district=models.CharField(max_length=100,blank=False)
    region=models.CharField(max_length=100,blank=False)
    departement=models.CharField(max_length=100,blank=False)
    sous_prefecture=models.CharField(max_length=100,blank=False)
    commune=models.CharField(max_length=100,blank=False)
    quartier=models.CharField(max_length=100,blank=False)

class Affecter(models.Model):
    agentr=models.ForeignKey(AgentRecenseur,on_delete=models.CASCADE)
    localite=models.ForeignKey(Localite,on_delete=models.CASCADE)
    create=models.DateTimeField(auto_now_add=True)