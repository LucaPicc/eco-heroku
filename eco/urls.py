from django.contrib import admin
from django.urls import path, include
from .views import IndexView
from django.contrib.auth.views import logout_then_login, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name ='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('user/', include('user.urls'), name = 'user'),
    path('productos/', include('productos.urls'), name = 'productos'),
]
