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

class Parents(Personne):
    id=models.BigAutoField(primary_key=True)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)


class Recenser(models.Model):
    parent=models.ForeignKey(Parents,on_delete=models.CASCADE)
    religion=models.CharField(max_length=100,blank=False)
    survie_mere=models.CharField(max_length=100,blank=False)
    survie_pere=models.CharField(max_length=100,blank=False)
    alphabetisation=models.CharField(max_length=100,blank=False)
    niveau_instruction=models.CharField(max_length=100,blank=False)
    statut_occup=models.CharField(max_length=100,blank=False)
    occupation_actu=models.CharField(max_length=100,blank=False)
    branche_activite=models.CharField(max_length=100,blank=False)
    situation_matr=models.CharField(max_length=100,blank=False)
    type_mariage=models.CharField(max_length=100,blank=False)
    nombre_enfant=models.CharField(max_length=100,blank=False)
    nombre_enfant_v=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parent']
    def __str__(self):
        return '{}'.format(self.parent)

class Enfant(Personne):
    ecolier=models.CharField(max_length=100,blank=True,default='oui')
    parentf=models.ForeignKey(Parents,on_delete=models.CASCADE)
    id1=models.BigAutoField(primary_key=True)

class Commodite(models.Model):
    parentc=models.ForeignKey(Parents,on_delete=models.CASCADE)
    nombre_piece=models.CharField(max_length=100,blank=False)
    nature_mur=models.CharField(max_length=100,blank=False)
    nature_toit=models.CharField(max_length=100,blank=False)
    nature_sol=models.CharField(max_length=100,blank=False)
    alimentation_eau=models.CharField(max_length=100,blank=False)
    eclairage=models.CharField(max_length=100,blank=False)
    cuisson=models.CharField(max_length=100,blank=False)
    evacuation_ordure=models.CharField(max_length=100,blank=False)
    evacuation_eau=models.CharField(max_length=100,blank=False)
    loyer=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parentc']

class Equipement(models.Model):
    parente=models.ForeignKey(Parents,on_delete=models.CASCADE)
    moyen_deplacement=models.CharField(max_length=100,blank=False)
    equipement_electr=models.CharField(max_length=100,blank=False)
    equipement_audio=models.CharField(max_length=100,blank=False)
    statut_occupation=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parente']

class Migrant(models.Model):
    parentm=models.ForeignKey(Parents,on_delete=models.CASCADE)
    deplace=models.BooleanField()
    annee_deplace=models.DateField(blank=False)
    lieu_residence_a=models.CharField(max_length=100,blank=False)
    intention_ret=models.BooleanField()
    class Meta:
        ordering=['parentm']
    def __str__(self):
        return '{}'.format(self.parent)

class Deces(models.Model):
    parentd=models.ForeignKey(Parents,on_delete=models.CASCADE)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    age_deces=models.PositiveBigIntegerField()
    nom_decede=models.CharField(max_length=100,blank=False)
    prenom_decede=models.CharField(max_length=100,blank=False)
    annee_deces=models.DateField(blank=False)
    class Meta:
        ordering=['parentd']
    def __str__(self):
        return '{}_{}'.format(self.nom_decede,self.prenom_decede)

class admins(Personne):
    idf=models.CharField(max_length=100,blank=False,unique=True)
    role=models.CharField(max_length=100,blank=False)

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
   
    