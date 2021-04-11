from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View
from django.db.models import Count

from orders.models import Order

from .forms import СustomerForm

from django.db.models import Prefetch

from .models import Сustomer, Type_customer
from django.db.models import Q

from django.core.paginator import Paginator


# Create your views here.

def customers(request):
    search_query = request.GET.get('search', '')

    if search_query:
        customer = Сustomer.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(middle_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(organization__icontains=search_query) |
            Q(phone__icontains=search_query))
    else:
        customer = Сustomer.objects.all()

    paginator = Paginator(customer, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()


    '''Кол-во заказов'''

    # number_of_order = Order.objects.count(id=2)

    ''''''

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
        'prev_page_url': prev_url,

    }
    return render(request, 'customers.html', context=context)

'''добавление данных в бд'''
class Create(View):
    def get(self, request):
        # form = CarFormCreate()
        template = 'create_customer.html'
        context = {

            'list_articles': Сustomer.objects.all().order_by('-id'),
            'form': СustomerForm(),

        }
        return render(request, template, context)

    def post(self, request):
        bound_form = СustomerForm(request.POST)
        context = {'form': bound_form}
        if bound_form.is_valid():
            new = bound_form.save()

            return HttpResponseRedirect("/customers")

        return render(request, 'create_customer.html', context=context)


'''Статистика'''
def statistics(request, id):

    search_query = request.GET.get('search', '')

    if search_query:

        orders = Order.objects.filter(Q(date=search_query))

    else:
        #orders = Order.objects.all()
        orders = Order.objects.order_by('-date')

    if search_query:

        orders = Order.objects.filter(Q(date=search_query))

    else:
        #orders = Order.objects.all()
        orders = Order.objects.filter(customer=id).order_by('-date')

    paginator = Paginator(orders, 10)
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
    return render(request, 'orders.html', context=context)


'''изменение данных в бд'''
class Edit(View):
    def get(self, request, id):

        tom = Order.objects.get(id=id)


        bount_form = СustomerForm(instance=tom)
        context = {
             'form': bount_form,

        }
        return render(request, "edit_customer.html", context=context)

    def post(self, request, id):
         customer = Сustomer.objects.get(id=id)

         context = {"customer": customer,
                    }
         if request.method == "POST":

            type = Type_customer(id=id)
            type.id = request.POST.get("T_customer")


            customer.first_name = request.POST.get("first_name")
            customer.middle_name = request.POST.get("middle_name")
            customer.last_name = request.POST.get("last_name")
            customer.organization = request.POST.get("organization")
            customer.adres = request.POST.get("adres")
            customer.phone = request.POST.get("phone")
            customer.T_customer = type
            customer.inn = request.POST.get("inn")
            customer.kpp = request.POST.get("kpp")
            customer.bank = request.POST.get("bank")
            customer.rs = request.POST.get("rs")
            customer.ks = request.POST.get("ks")
            customer.bik = request.POST.get("bik")
            customer.email = request.POST.get("email")

            customer.save()
            return HttpResponseRedirect("/customers")
         else:
            return render(request, "edit_customer.html", context=context)


'''удаление данных из бд'''
def delete(request, id):
    try:
        customer = Сustomer.objects.get(id=id)
        customer.delete()
        return HttpResponseRedirect("/customers")
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customers not found</h2>")



