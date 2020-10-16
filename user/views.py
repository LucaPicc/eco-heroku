from decimal import Decimal
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from .forms import UserForm, UserAdminForm, EntityForm, ProfileCopForm, ProfileMunForm, ProfilePuntForm
from .models import UserCustom, Entity, ProfileCop, ProfileMun, ProfilePunt
from django.urls import reverse_lazy


class RegUserEntity(CreateView):
    model = UserCustom
    template_name = 'users/crear_usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if form.is_valid():
            new_user = UserCustom(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                is_user_entity = True,
                entity_id = userlog.entity_id
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class RegAdmin(CreateView):
    model = UserCustom
    template_name = 'users/crear_usuario.html'
    form_class = UserAdminForm
    success_url = reverse_lazy('index')
    
    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = UserCustom(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                is_admin_entity = True,
                entity_id = form.cleaned_data.get('entity').id
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class RegEntity(CreateView):
    model = Entity
    template_name = 'users/crear_entidad.html'
    form_class = EntityForm
    success_url = reverse_lazy('home')
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('tipo') == 'MU':
                form.save()
                return redirect('crear_mun')
            elif form.cleaned_data.get('tipo') == 'CO':
                form.save()
                return redirect('crear_cop')
            elif form.cleaned_data.get('tipo') == 'PL':
                form.save
                return redirect('crear_punt')
        else:
            return render(request,self.template_name,{'form':form})
class ListEntity(ListView):
    model = Entity
    template_name = 'listarentidad.html'

class ListEntityUser(ListView):
    model = Entity
    template_name = 'users/entidades-user.html'

class HomeUserView(TemplateView):
    template_name = "users/home-user.html"

def HomeUserView2(request):
    userlog = UserCustom.objects.get(id = request.user.id)
    entity = Entity.objects.get(id = userlog.entity_id)

    return render(request, 'users/home-user.html',{'entity':entity,'userlog':userlog})
class ProfileMunFormView(CreateView):
    model = ProfileMun
    template_name = "users/mun.html"
    form_class = ProfileMunForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            ent = Entity.objects.latest('id')
            mun = ProfileMun(
                mun_id = ent.id,
                hab = form.cleaned_data.get('hab'),
                dispo_final = form.cleaned_data.get('dispo_final'),
                difreco = form.cleaned_data.get('difreco'),
                complejo_tratamiento = form.cleaned_data.get('complejo_tratamiento'),
                compostaje_biodigestion = form.cleaned_data.get('compostaje_biodigestion'),
                planta_clasif = form.cleaned_data.get('planta_clasif'),
                otros = form.cleaned_data.get('otros'),
                ton_recup = form.cleaned_data.get('ton_recup'),
                pers_recol = form.cleaned_data.get('pers_recol'),
                pers_comp_am = form.cleaned_data.get('pers_comp_am'),
                ton_proces = form.cleaned_data.get('ton_proces'),
                cost_recol = form.cleaned_data.get('cost_recol'),
                cost_comp_am = form.cleaned_data.get('cost_comp_am'),
                ing_venta = form.cleaned_data.get('ing_venta'),
            )
            mun.save()
            return redirect('crear_entity')
        else:
            return render(request,self.template_name,{'form':form})


class ProfileCopFormView(CreateView):
    model = ProfileCop
    template_name = "users/cop.html"
    form_class = ProfileCopForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cop = ProfileCop(
                cop_id = Entity.objects.latest('id').id,
                cant_socio = form.cleaned_data.get('cant_socio'),
                fuent_rec = form.cleaned_data.get('fuent_rec'),
                recol = form.cleaned_data.get('recol'),
                empl = form.cleaned_data.get('empl'),
                ton_rec = form.cleaned_data.get('ton_rec'),
                ton_a_rechazo = form.cleaned_data.get('ton_a_rechazo'),
                gast_totales = form.cleaned_data.get('gast_totales'),
            )
            cop.save()
            return redirect('crear_entity')
        else:
            return render(request,self.template_name,{'form':form})

class ProfilePuntFormView(CreateView):
    model = ProfilePunt
    template_name = "users/punt.html"
    form_class = ProfilePuntForm

    def post(self, request, *args, **kwargs):
        form = form = self.form_class(request.POST)
        if form.is_valid():
            punt = ProfilePunt(
                punt_id = Entity.objects.latest('id').id,
                propiedad = form.cleaned_data.get('propiedad'),
                operacion = form.cleaned_data.get('operacion'),
                ton_recup = form.cleaned_data.get('ton_recup'),
                visitas = form.cleaned_data.get('visitas'),
                gast_op = form.cleaned_data.get('gast_op'),
                cant_personas = form.cleaned_data.get('cant_personas'),
            )
            punt.save()
            return redirect('crear_entity')
        else:
            return render(request,self.template_name,{'form':form})

def post_estad_mu(request):
    userlog = UserCustom.objects.get(id = request.user.id)
    entity = Entity.objects.get(id = userlog.entity_id)
    if entity.tipo == 'MU':
        mu = ProfileMun.objects.get(mun_id = entity.id)
        
        mu_indc_prud = mu.ton_recup / mu.pers_clas /12
        mu_indc_prud = round(mu_indc_prud,2)
        
        mu_indc_lab = (mu.pers_recol + mu.pers_comp_am)/ ( mu.hab * 0.001)
        mu_indc_lab = round(mu_indc_lab,2)
        
        mu_girsu = 0
        
        mu_indc_rec = Decimal(mu.ton_recup) *Decimal( 1000.00)/ Decimal(mu.hab)
        mu_indc_rec = round(mu_indc_rec,2)
        return render(request,'users/estad_mu.html',{'mu':mu,'mu_indc_prud':mu_indc_prud,'mu_indc_lab':mu_indc_lab,'mu_indc_rec':mu_indc_rec})
    elif entity.tipo == 'CO':
        cop = ProfileCop.objects.get(cop_id = entity.id)

        cop_indc_prud = cop.ton_rec / cop.empl /12
        cop_indc_prud = round(cop_indc_prud,2)

        cop_girsu = cop.gast_totales / cop.ton_rec
        cop_girsu = round(cop_girsu,2)

        cop_ind_rec = cop.ton_a_rechazo/cop.ton_rec -1
        return render(request,'users/estad_cop.html',{'cop':cop,'cop_indc_prud':cop_indc_prud,'cop_girsu':cop_girsu,'cop_ind_rec':cop_ind_rec})

    elif entity.tipo == 'PL':
        pl = ProfilePunt(punt_id = entity.id)

        pl_indc_prud = pl.ton_recup / pl.cant_personas /12

        pl_girsu = 0

        pl_indc_rec = 0

        return render(request,'users/estad_pl.html',{'pl':pl,'pl_indc_prud':pl_indc_prud,'pl_girsu':pl_girsu,'pl_indc_rec':pl_indc_rec})

class GrafView(TemplateView):
    template_name = 'users/graf.html'
