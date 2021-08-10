import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect

# _logger = logging.getLogger(__name__)
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from comparetool.models import SizeItem, CompareItems
from showcase.filters import GliderFilter, SizeFilter
from showcase.models import Maker,Glider,Size
from reviews.models import GliderReview
from members.models import User
from showcase.views import gliders
from queryset_sequence import QuerySetSequence
from itertools import chain
from django.db.models import Q


class Homepage(TemplateView):
    template_name = 'showcase/index.html'

   

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        mySizeFilter = SizeFilter(self.request.GET, queryset=Size.objects.filter())
        model = Glider.objects.filter(Q(glider_size__in=mySizeFilter.qs)).distinct()

        myFilter = GliderFilter(self.request.GET, queryset=model)


        #query = QuerySetSequence(myFilter.qs,mySizeFilter.qs)

        model = myFilter.qs

        #context['gliders'] = model
        context['myFilter'] = myFilter
        context['mySizeFilter'] = mySizeFilter
        context['manufactures'] = get_manufactures()
        context['sizes'] = Size.objects.all()
        context['reviews'] = GliderReview.objects.all()

        page = self.request.GET.get('page', 1)
        paginator = Paginator(model, 2)

        #parte paginatore con numeri manuale
        #page_number = self.request.GET.get('page')
        #page_obj = paginator.get_page(page_number)
        #context['gliders'] = page_obj
        #fine parte paginatore manuale

        try:
            gliders = paginator.page(page)
        except PageNotAnInteger:
            gliders = paginator.page(1)
        except EmptyPage:
            gliders = paginator.page(paginator.num_pages)

        context['gliders'] = gliders
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            sizeId = request.POST['sizeId']
            size = Size.objects.get(id=sizeId)
            # Get user account information
            try:
                user = request.user
            except:
                device = request.COOKIES['device']
                user, created = User.objects.get_or_create(device=device)

            compareItems, created = CompareItems.objects.get_or_create(user=user, complete=False)
            sizeItem, created = SizeItem.objects.get_or_create(compareItems=compareItems, size=size)

            sizeItem.save()

            return redirect('comparetool:compare')

        return render(request, 'showcase/index.html')


def get_gliders():
    gliders = Glider.objects.all()

    return gliders

def get_manufactures():
    maker = Maker.objects.all()

    return maker


