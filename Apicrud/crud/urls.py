from django.urls import path
from .viewsR.recenser import get7,get_id7
from .viewsR.deces import get2,get_id2
from .viewsR.enfant import get3,get_id3
from .viewsR.equipement import get4,get_id4
from .viewsR.migrant import get5,get_id5
from .viewsR.commodite import get1,get_id1
from .viewsR.parents import get6,get_id6
from .viewsR.donateurID import get8,get_id8,doneffectuer2,ddoneffectuer2
from .viewsR.donateurAN import get9,get_id9,ddoneffectuer,doneffectuer
from .viewsR.donateurET import get10,get_id10,doneffectuer1,ddoneffectuer1
from .viewsR.localite import localite,localited
from .viewsR.agent import agent,agentd
from .viewsR.affecter import affecter,affecterd

urlpatterns = [
    path('recenser/', get7),
    path('details/<int:pk>/', get_id7),
    path('deces/', get2),
    path('ddetails/<int:pk>/', get_id2),
    path('enfant/', get3),
    path('denfant/<int:pk>/', get_id3),
    path('migrant/', get5),
    path('dmigrant/<int:pk>/', get_id5),
    path('commodite/', get1),
    path('dcommodite/<int:pk>/', get_id1),
    path('parents/', get6),
    path('dparents/<int:pk>/', get_id6),
    path('equipement/', get4),
    path('dequipement/<int:pk>/', get_id4),
    path('donateurid/', get8),
    path('ddonateurid/<int:pk>/', get_id8),
    path('donateurano/', get9),
    path('ddonateurano/<int:pk>/', get_id9),
    path('donateureta/', get10),
    path('ddonateureta/<int:pk>/', get_id10),
    path('effectuerdona/', doneffectuer),
    path('deffectuerdona/<int:pk>/', ddoneffectuer),
    path('effectuerdone/', doneffectuer1),
    path('deffectuerdone/<int:pk>/', ddoneffectuer1),
    path('effectuerdoni/', doneffectuer2),
    path('deffectuerdoni/<int:pk>/', ddoneffectuer2),
    path('agent/', agent),
    path('agentd/<int:pk>/', agentd),
    path('localite/', localite),
    path('localited/<int:pk>/', localited),
    path('affecter/', affecter),
    path('affecterd/<int:pk>/', affecterd),
]
