from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserCustom, Entity, ProfileCop, ProfileMun, ProfilePunt
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = UserCustom
        fields = ['username','email']
class UserAdminForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Introduzca contraseña',
            'id':'password1',
            'required':'required',
        }
    ))
    password2 = forms.CharField(label = 'Contraseña de confirmación', widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Vuelva a ingresar su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    class Meta:
        model = UserCustom
        fields = ['username','email','first_name','last_name','entity']
        widgets = {
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el correo electonico',
                    'id':'email',
                    'required':'required',
                }
            ),
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'first_name',
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido',
                    'id':'last_name',
                }
            ),
            'entity':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
        }
        label = {
            'username':_('Nombre de usuario'),
            'email':_('Correo electroníco'),
            'first_name':_('Nombre'),
            'last_name':_('Apellido'),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'
class ProfileMunForm(forms.ModelForm):
    
    class Meta:
        model = ProfileMun
        fields = '__all__'
class ProfileCopForm(forms.ModelForm):
    
    class Meta:
        model = ProfileCop
        fields = '__all__'
class ProfilePuntForm(forms.ModelForm):
    
    class Meta:
        model = ProfilePunt
        fields = '__all__'


