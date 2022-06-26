from rest_framework import serializers
from crud.models import*

class RecensementS(serializers.ModelSerializer):
    class Meta:
        model = Recenser
        fields = '__all__'

class ParentS(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'

class EnfantS(serializers.ModelSerializer):
    class Meta:
        model = Enfant
        fields = '__all__'      

class CommoditeS(serializers.ModelSerializer):
    class Meta:
        model = Commodite
        fields = '__all__'


class EquipementS(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'

class DeceS(serializers.ModelSerializer):
    class Meta:
        model = Deces
        fields = '__all__'

class MigrantS(serializers.ModelSerializer):
    class Meta:
        model = Migrant
        fields = '__all__'

class DanteurAS(serializers.ModelSerializer):
    class Meta:
        model = DonateurAno
        fields = '__all__'

class DanteurIDS(serializers.ModelSerializer):
    class Meta:
        model = DonateurId
        fields = '__all__'

class DanteurETS(serializers.ModelSerializer):
    class Meta:
        model = DonateurEta
        fields = '__all__'

class EffectuerDS(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonAno
        fields = '__all__'

class EffectuerDES(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonEta
        fields = '__all__'

class EffectuerDIS(serializers.ModelSerializer):
    class Meta:
        model = EffectuerDonId
        fields = '__all__'

class AfferterS(serializers.ModelSerializer):
    class Meta:
        model = Affecter
        fields = '__all__'

class AgentRecenseurS(serializers.ModelSerializer):
    class Meta:
        model = AgentRecenseur
        fields = '__all__'

class LocaliteS(serializers.ModelSerializer):
    class Meta:
        model = Localite
        fields = '__all__'

    
