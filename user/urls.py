from django.urls import path
from .views import GrafView,RegUserEntity,RegAdmin,RegEntity, ListEntity,HomeUserView,HomeUserView2,ListEntityUser, ProfileMunFormView, ProfileCopFormView, ProfilePuntFormView,post_estad_mu
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ########################Home para Usuarios##########################################
    path('home/',login_required(HomeUserView2), name = 'home'),
    ######################Manejo de Usuarios###########################################
    path('crear_user/', login_required(RegUserEntity.as_view()) , name = 'crear_user'),
    path('crear_admin/', login_required(RegAdmin.as_view()),name = 'crear_admin'),
    #######################URLS entidades##########################################
    path('crear_entity/', login_required(RegEntity.as_view()) , name = 'crear_entity'),
    path('participantes/', login_required(ListEntity.as_view()), name = 'participantes'),
    path('entidades/',login_required(ListEntityUser.as_view()), name = 'entidades-user'),
    path('crear_mun/',login_required(ProfileMunFormView.as_view()), name = 'crear_mun'),
    path('crear_cop/',login_required(ProfileCopFormView.as_view()), name = 'crear_cop'),
    path('crear_punt/',login_required(ProfilePuntFormView.as_view()), name = 'crear_punt'),
    ###########Estadisticas de Entidades#################################################
    path('estad_mu/',login_required(post_estad_mu),name = 'estad_mu'),
    path('graf/',login_required(GrafView.as_view()), name = 'graf'),
]