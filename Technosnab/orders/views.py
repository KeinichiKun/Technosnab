from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Order, Cars, Worker, Сustomer, Product
from .forms import OrderForm, СustomerForm
from django.db.models import Q
from django.views.generic import View

from django.template import RequestContext


from django.views.generic.list import ListView
import re


from django.core.paginator import Paginator
# Create your views here.

def orders(request):

    search_query_date = request.GET.get('search_date', '')
    search_query_text = request.GET.get('search_text', '')

    search_query_from = request.GET.get('search_date_from', '')
    search_query_to = request.GET.get('search_date_to', '')

    if (search_query_from and search_query_to):
        def date_from_to(search_query_from, search_query_to):
            return

    if (search_query_text or search_query_date == None):
        orders = Order.objects.filter(Q(adress__icontains=search_query_text) |
                                      Q(customer__first_name__icontains=search_query_text) |
                                      Q(customer__middle_name__icontains=search_query_text) |
                                      Q(customer__last_name__icontains=search_query_text) |
                                      Q(customer__organization__icontains=search_query_text) |
                                      Q(customer__phone__icontains=search_query_text) |
                                      Q(product__product_caption__icontains=search_query_text) |
                                      Q(car__state_number__icontains=search_query_text)|
                                      Q(worker__first_name__icontains=search_query_text)|
                                      Q(worker__middle_name__icontains=search_query_text) |
                                      Q(worker__last_name__icontains=search_query_text)
                                      ).order_by('-date')
    elif (search_query_text or search_query_date):
        orders = Order.objects.filter(Q(adress=search_query_text) | Q(date=search_query_date)
                                      ).order_by('-date')
    elif (search_query_to and search_query_from != None):
        orders = Order.objects.raw("SELECT * FROM `orders_order` WHERE date >= %s and date <= %s", [search_query_from, search_query_to])
    else:
        orders = Order.objects.order_by('-date')

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


# добавление данных в бд
# def create(request):
#     car = Cars.objects.all()
#     customer = Сustomer.objects.all()
#     worker = Worker.objects.all()
#     product = Product.objects.all()
#     if request.method == "POST":
#         tom = Order()
#         car = Cars()
#         worker = Worker()
#         customer = Сustomer()
#         product = Product()
#         car.id = request.POST.get("car")
#         worker.id = request.POST.get("worker")
#         customer.id = request.POST.get("customer")
#         product.id = request.POST.get("product")
#
#         tom.car = car
#         tom.worker = worker
#         tom.customer = customer
#         tom.product = product
#         tom.quantity = request.POST.get("quantity")
#         tom.time = request.POST.get("time")
#         tom.final_price = request.POST.get("final_price")
#         tom.adress = request.POST.get("adress")
#         tom.caption = request.POST.get("caption")
#         tom.date = request.POST.get("date")
#         tom.save()
#         return HttpResponseRedirect("/orders")
#     else:
#         return render(request, "create_order.html", {"car": car, "worker": worker, "customer": customer, "product": product})
#
class OrderCreate(View):
        def get(self, request):
            # form = CarFormCreate()
            template = 'create_order.html'
            context = {

                'list_articles': Order.objects.all().order_by('-id'),
                'form': OrderForm(),

            }
            return render(request, template, context)

        def post(self, request):
            bound_form = OrderForm(request.POST)
            context = {'form': bound_form}
            if bound_form.is_valid():
                new = bound_form.save()

                return HttpResponseRedirect("/orders")

            return render(request, 'create_order.html', context=context)



class CreateCustomer(View):
    def get(self, request):
        # form = CarFormCreate()
        template = 'cr_or_customer.html'
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

            return HttpResponseRedirect("/orders/create")

        return render(request, 'cr_or_customer.html', context=context)



class OrderEdit(View):
        def get(self, request, id):


            tom = Order.objects.get(id=id)

            car = Cars.objects.all()
            # customer = Сustomer.objects.all()
            # worker = Worker.objects.all()
            # product = Product.objects.all()

            bount_form = OrderForm(instance=tom)
            context = {

                'form': bount_form,
                # 'position': pos,
                'order': tom,

                # "car": car,
                # "customer": customer,
                # "worker": worker,
                # "product": product,
            }

            return render(request, "edit_order.html", context=context)

        def post(self, request, id):
            tom = Order.objects.get(id=id)


            context = {"order": tom,

                       }

            if request.method == "POST":

                car = Cars(id=id)
                worker = Worker(id=id)
                customer = Сustomer(id=id)
                product = Product(id=id)

                car.id = request.POST.get("car")
                worker.id = request.POST.get("worker")
                customer.id = request.POST.get("customer")
                product.id = request.POST.get("product")



                tom.car = car
                tom.worker = worker
                tom.customer = customer
                tom.product = product
                tom.quantity = request.POST.get("quantity")
                tom.time = request.POST.get("time")
                tom.adress = request.POST.get("adress")
                tom.caption = request.POST.get("caption")
                tom.date = request.POST.get("date")
                tom.save()
                return HttpResponseRedirect("/orders")
            else:
                return render(request, "edit_order.html", context=context)


'''Удаление'''
def delete(request, id):
    try:
        cars = Order.objects.get(id=id)
        cars.delete()
        return HttpResponseRedirect("/orders")
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def complite(request, id):
    try:
            tom = Order.objects.get(id=id)
            tom.status = "C"

            tom.save()
            return HttpResponseRedirect("/orders")
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")




