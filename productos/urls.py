from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProdReg,ProdList, ProductStockFromView, SendProductFromView, MaterialFormView,ListMat, MaterialStockFormView, SendMaterialFormView, ListMat,ListMatStock,ListProdStock
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ##################Prod y materiales#######################################
    path('registro/',login_required(ProdReg.as_view()),name = 'reg-prod'),
    path('listado/', login_required(ProdList.as_view()), name = 'list-prod'),
    path('list_mat',login_required(ListMat.as_view()),name = 'list_mat'),
    ####################Stock###################################################
    path('ing_stock_prod/', login_required(ProductStockFromView.as_view()), name = 'ing_stock_prod' ),
    path('env_prod/', login_required(SendProductFromView.as_view()), name = 'env_prod'),
    path('reg_mat/', login_required(MaterialFormView.as_view()), name = 'reg_mat'),
    path('env_mat/', login_required(SendMaterialFormView.as_view()), name = 'env_mat'),
    path('ing_stock_mat/',login_required(MaterialStockFormView.as_view()), name = 'ing_stock_mat'),
    path('mat_stock/',login_required(ListMatStock.as_view()),name = 'mat_stock'),
    path('mat/',login_required(ListMat.as_view()),name = 'mat'),
    path('prod_stock',login_required(ListProdStock.as_view()), name = 'prod_stock'),
]
