from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy

from user.models import UserCustom, Entity
from .models import Product, ProductStock, SendProduct, Material, MaterialStock, SendMaterial, MovMStock, MovPStock
from .forms import ProdForm, ProductStockForm, SendProductForm, MaterialForm, MaterialStockForm, SendMaterialForm


class ProdReg(CreateView):
    model = Product
    template_name = 'productos/registro.html'
    form_class = ProdForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_prod = Product(
                nombre = form.cleaned_data.get('nombre'),
                descripcion = form.cleaned_data.get('descripcion'),
                material = form.cleaned_data.get('material'),
                cantkg = form.cleaned_data.get('cantkg'),
            )
            new_prod.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class ProdList(ListView):
    model = Product
    template_name = 'productos/list.html'
class ProductStockFromView(CreateView):
    model = ProductStock
    template_name = "productos/reg_prod_stock.html"
    form_class = ProductStockForm
    success_url = reverse_lazy('home')

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if form.is_valid():
            prod = ProductStock(
                entity_id = userlog.entity_id,
                product = form.cleaned_data.get('product'),
                cantidad = form.cleaned_data.get('cantidad')
            )
            mov = MovPStock(
                entity_id = userlog.entity_id, 
                usuario_id = userlog.id,
                product = form.cleaned_data.get('product'),
                tipo = 'EP',
                peso = form.cleaned_data.get('peso')
            )
            if ProductStock.objects.filter(entity_id= prod.entity_id,product_id = prod.product_id).exists():
                prod_c = ProductStock.objects.filter(entity_id= prod.entity_id,product_id = prod.product_id).get()
                cant = prod_c.cantidad + prod.cantidad
                prod_c.cantidad = cant
                prod_c.save()
                mov.save()
            else:
                prod.save()
                mov.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class SendProductFromView(CreateView):
    model = ProductStock
    template_name = "productos/env_prod.html"
    form_class = ProductStockForm
    success_url = reverse_lazy('home')

class ListProdStock(ListView):
    model = ProductStock
    template_name = 'productos/pro_stock.html'

class MaterialFormView(CreateView):
    model = Material
    template_name = "productos/reg_mat.html"
    form_class = MaterialForm
    success_url = reverse_lazy('home')

class ListMat(ListView):
    model = Material
    template_name = 'productos/list_mat.html'

class MaterialStockFormView(CreateView):
    model = MaterialStock
    template_name = "productos/reg_mat_stock.html"
    form_class = MaterialStockForm
    success_url = reverse_lazy('home')

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if form.is_valid():
            mat = MaterialStock(
                entity_id = userlog.entity_id,
                material = form.cleaned_data.get('material'),
                peso = form.cleaned_data.get('peso')
            )
            mov = MovMStock(
                entity_id = userlog.entity_id, 
                usuario_id = userlog.id,
                material = form.cleaned_data.get('material'),
                tipo = 'EM',
                peso = form.cleaned_data.get('peso')
            )
            if MaterialStock.objects.filter(entity_id = mat.entity_id, material_id=mat.material_id).exists():
                mat_c = MaterialStock.objects.filter(entity_id = mat.entity_id, material_id=mat.material_id).get()
                peso_c = mat_c.peso + mat.peso
                mat_c.peso = peso_c
                mat_c.save()
                mov.save()
            else:
                mat.save()
                mov.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class ListMatStock(ListView):
    model = MaterialStock
    template_name = 'productos/mat_stock.html'
    

class SendMaterialFormView(CreateView):
    model = SendMaterial
    template_name = "productos/env_mat.html"
    form_class = SendMaterialForm
    success_url = reverse_lazy('home')



