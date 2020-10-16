from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Product, Material, MaterialStock, ProductStock, SendMaterial, SendProduct



class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Escriba el nombre del material',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Escriba una breve descripción del material',
                }
            ),
        }
        label = {
            'nombre': _('Nombre'),
            'descripcion': _('Descripción'),
        }

class MaterialStockForm(forms.ModelForm):
    class Meta:
        model = MaterialStock
        fields = ['material','peso']
        widgets = {
            'material': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Elija un material para el guardar en el stock',
                }
            ),
            'peso': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Introduzca la cantidad de material en kilogramos',
                }
            ),
        }
        label = {
            'nombre':_('Nomnbre del material'),
            'peso':_('Peso en kilogramos del material'),
        }


class SendMaterialForm(forms.ModelForm):
    class Meta:
        model = SendMaterial
        fields = '__all__'

class ProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ['product','cantidad']
        widgets = {
            'product': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Elija un producto para guardar en el stock',
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Introduzca la cantidad de productos en unidades',
                }
            ),
        }
        label = {
            'product':_('Nomnbre del producto'),
            'cantidad':_('Cantidad'),
            'descripcion':_('Intoduzca una breve descripción del producto'),
        }


class SendProductForm(forms.ModelForm):
    class Meta:
        model = SendProduct
        fields = '__all__'