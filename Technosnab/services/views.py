from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound

from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.base import View


from .forms import ServiceForm
from .models import Product

from django.core.paginator import Paginator

# Create your views here.
def services(request):

    search_query = request.GET.get('search', '')

    if search_query:
        product = Product.objects.filter(Q(product_caption__icontains=search_query))
    else:
        product = Product.objects.all()
    paginator = Paginator(product, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_page_url': next_url,
        'prev_page_url': prev_url
    }
    return render(request, 'services.html', context=context)


'''добавление данных в бд'''
# def create(request):
#     if request.method == "POST":
#         tom = Product()
#         tom.product_caption = request.POST.get("product_caption")
#         tom.price = request.POST.get("price")
#         tom.quantity_in_stock = request.POST.get("quantity_in_stock")
#         tom.save()
#         return HttpResponseRedirect("/services")
#     else:
#         return render(request, "create_product.html")


class ServiceCreate(View):

        def get(self, request):
            # form = CarFormCreate()
            template = 'create_product.html'
            context = {
                'list_articles': Product.objects.all().order_by('-id'),
                'form': ServiceForm(),

            }
            return render(request, template, context)

        def post(self, request):
            bound_form = ServiceForm(request.POST)
            context = {'form': bound_form}
            if bound_form.is_valid():
                new = bound_form.save()

                return HttpResponseRedirect("/services")

            return render(request, 'create_product.html', context=context)


'''изменение данных в бд'''
class Edit(View):
    def get(self, request, id):
            # form = CarFormCreate()
            tom = Product.objects.get(id=id)
            bount_form = ServiceForm(instance=tom)
            context = {
                    'product': tom,
                    'form': bount_form,
                }
            return render(request, "edit_product.html", context=context)

    def post(self, request, id):
            tom = Product.objects.get(id=id)
            if request.method == "POST":
                    tom.product_caption = request.POST.get("product_caption")
                    tom.price = request.POST.get("price")
                    tom.quantity_in_stock = request.POST.get("quantity_in_stock")
                    tom.save()
                    return HttpResponseRedirect("/services")
            else:
                    return render(request, "edit_product.html", {"product": tom})

# удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/services")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



class SerchProduct(ListView):


    template_name = 'services.html'

    def get_queryset(self):
        return Product.objects.filter(product_caption__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context



"""
class SerchProduct(ListView):
    model = Product
    template_name = 'services.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        product = Product.objects.filter(Q(product_caption__icontains=query))
        return product
    
"""

