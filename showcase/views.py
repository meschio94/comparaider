from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from .filters import GliderFilter
from .models import Maker, Glider, Size
from members.decorators import manufacturer_required, person_required
from .forms import MakerEditForm,GliderForm,SizeForm
# Create your views here.


class IndexView(ListView):
    template_name = 'showcase/index.html'

class Prova(TemplateView):
    template_name = 'showcase/prova.html'
    def get_context_data(self, **kwargs):
        context = super(Prova, self).get_context_data(**kwargs)
        context['gliders'] = Glider.objects.all()
        return context


class Manufactures(TemplateView):
    template_name = 'showcase/manufactures.html'

    def get_context_data(self, **kwargs):
        context = super(Manufactures, self).get_context_data(**kwargs)
        model = Maker.objects.all().order_by('name')

        page = self.request.GET.get('page', 1)
        paginator = Paginator(model, 2)

        try:
            manufactures = paginator.page(page)
        except PageNotAnInteger:
            manufactures = paginator.page(1)
        except EmptyPage:
            manufactures = paginator.page(paginator.num_pages)

        context['manufactures'] = manufactures

        return context


class ShowManufacturesProfileView(DetailView):
    model = Maker
    template_name = 'showcase/manufacture_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowManufacturesProfileView, self).get_context_data(**kwargs)

        model = Glider.objects.all()
        myFilter = GliderFilter(self.request.GET, queryset=model)
        model = myFilter.qs

        page_manufacture = get_object_or_404(Maker, id=self.kwargs['pk'])

        # context['gliders'] = model
        context['myFilter'] = myFilter
        context['manufactures'] = Maker.objects.all()
        context['sizes'] = Size.objects.all()
        context['page_manufacture'] = page_manufacture
        page = self.request.GET.get('page', 1)
        paginator = Paginator(model, 2)

        # parte paginatore con numeri manuale
        # page_number = self.request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        # context['gliders'] = page_obj
        # fine parte paginatore manuale

        try:
            gliders = paginator.page(page)
        except PageNotAnInteger:
            gliders = paginator.page(1)
        except EmptyPage:
            gliders = paginator.page(paginator.num_pages)

        context['gliders'] = gliders
        return context


class GlidersView(ListView):
    model = Glider
    template_name = 'showcase/index.html'

    def get_context_data(self, **kwargs):
        context = super(GlidersView, self).get_context_data(**kwargs)
        context['gliders'] = GlidersView.objects.all()
        context['glidersprova'] = "prova"
        return context

@manufacturer_required
def manufacturer_admin(request):
    user = request.user
    manufacturer = user.manufacturer_user
    gliders = manufacturer.manufacturer_glider.all()

    return render(request, 'showcase/control_panel_manufacture.html', {'manufacturer':manufacturer, 'gliders':gliders})


@manufacturer_required
def add_glider(request):

    form = GliderForm(request.POST or None) #add
    if request.method == 'POST':
        form = GliderForm(request.POST, request.FILES)

        if form.is_valid():
            Glider = form.save(commit=False)
            user = request.user
            manufacturer = user.manufacturer_user
            Glider.maker = manufacturer
            Glider.save()

            return redirect('showcase:manufacture_panel')
        else:
            form = GliderForm()
    return render(request, 'showcase/control_panel_add_glider.html', {'add_glider_form':form})

@manufacturer_required
def add_size(request,pk):

    form = SizeForm(request.POST or None) #add
    if request.method == 'POST':
        form = SizeForm(request.POST, request.FILES)

        if form.is_valid():
            Size = form.save(commit=False)
            user = request.user
            manufacturer = user.manufacturer_user
            glider = manufacturer.manufacturer_glider.get(pk=pk)

            Size.glider = glider
            Size.save()

            return redirect('showcase:edit_glider', pk=pk)
        else:
            form = SizeForm()
    return render(request, 'showcase/control_panel_add_size.html', {'add_size_form':form})


@manufacturer_required
def edit_glider(request, pk):

    user = request.user
    manufacturer = user.manufacturer_user
    glider = manufacturer.manufacturer_glider.get(pk=pk)

    form = GliderForm(request.POST or None) #add

    if request.method == 'POST':
        form = GliderForm(request.POST, request.FILES, instance=glider)



        if form.is_valid():
            form.save()

            return redirect('showcase:manufacture_panel')
        else:
            form = GliderForm(instance=glider)
    return render(request, 'showcase/control_panel_edit_glider.html', {'edit_glider_form':form, 'glider':glider})

@manufacturer_required
def edit_size(request, pkg, pks):

    user = request.user
    manufacturer = user.manufacturer_user
    glider = manufacturer.manufacturer_glider.get(pk=pkg)
    size = glider.glider_size.get(pk=pks)
    form = SizeForm(request.POST or None) #add

    if request.method == 'POST':
        form = SizeForm(request.POST, request.FILES, instance=size)

        if form.is_valid():
            form.save()

            return redirect('showcase:edit_glider', pk=pkg)
        else:
            form = SizeForm(instance=size)
    return render(request, 'showcase/control_panel_edit_size.html', {'edit_size_form':form, 'glider':glider, 'size':size})


@manufacturer_required
def edit_info(request):
    manufacturer = request.user
    #manufacturer = user.manufacturer_user

    if request.method == 'POST':
        name = request.POST.get('name','')
        logoImage = request.POST.get('logoImage','')
        textIntro = request.POST.get('textIntro','')

        if name:

            manufacturer.logoImage = logoImage
            manufacturer.logoImage.save()

            manufacturer.textIntro = textIntro
            manufacturer.textIntro.save()

            manufacturer.name = name
            manufacturer.save()
            return redirect('showcase:manufacture_panel')

    return render(request, 'showcase/control_panel_add_glider.html', {'edit_info':manufacturer})




#pronti per il macero

class User(TemplateView):
    template_name = 'user.html'


def gliders():

    return "prova"

def glider_list(request):
    model = Glider.objects.all()
    myFilter = GliderFilter(request.GET, queryset=model)
    model = myFilter.qs
    context = {
        'myFilter': myFilter,
        'gliderlist':model,
    }
    return render(request,'index.html', context)

def view_glider_table(request, id=None):
    instance = get_object_or_404(Glider, id=id)
    context={
        'instance':instance
    }
    return render(request, 'showcase/modal_glider.html')

