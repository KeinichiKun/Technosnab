from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView
from .models import Cars, Expenses, Profit, Repairs, Repairs_type, Worker
from orders.models import Order
from django.views.generic.base import View



from .forms import CarFormCreate, CarFormEdit, ExpensesFormCreate

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

def cars(request):

    search_query = request.GET.get('search', '')

    if search_query:
        cars = Cars.objects.filter(Q(state_number__icontains=search_query) |
                                   Q(Model_caption__icontains=search_query) |
                                   Q(Spec_caption__icontains=search_query) |
                                   Q(Mark_caption__icontains=search_query) |
                                   Q(carrying__icontains=search_query))
    else:
        cars = Cars.objects.all()
    paginator = Paginator(cars, 10)
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

    return render(request, 'cars.html', context=context)




''' добавление данных в бд'''


'''создание авто'''


class CreateCar(View):
    def get(self, request):
        #form = CarFormCreate()
        template = 'create_car.html'
        context = {
                'list_articles': Cars.objects.all().order_by('-id'),
                'form': CarFormCreate(),

        }
        return render(request, template, context)

    def post(self, request):
        bound_form = CarFormCreate(request.POST)
        context = {'form': bound_form}
        if bound_form.is_valid():
            new = bound_form.save()

            return HttpResponseRedirect("/cars")

        return render (request, 'create_car.html', context=context)



def create_profit(request , id):
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Profit()
        tom.car = car.id
        tom.description = request.POST.get("description")
        tom.cost = request.POST.get("cost")
        tom.save()
        return HttpResponseRedirect("/cars/detail/")
    else:
        return render(request, "create_profit.html")



def create_expenses(request, id):
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Expenses()
        tom.car = car
        tom.description = request.POST.get("description")
        tom.cost = request.POST.get("cost")
        tom.data = request.POST.get("data")
        tom.save()
        return HttpResponseRedirect("/cars/detail/" + str(car.id))
    else:
        return render(request, "create_expenses.html", {"car": car})



'''изменение данных в бд'''



class DetailCar(View):

    def edit(request, id):
        try:

            Profit.objects.order_by('date')
            Expenses.objects.order_by('data')


            if request.method == "POST":
                car = Cars.objects.get(id=id)
                car.save()
                return HttpResponseRedirect("/cars")
            else:
                '''Пагинатор потрачено'''
                expenses = Expenses.objects.filter(car=id)
                paginator_ex = Paginator(expenses, 5)
                page_number_ex = request.GET.get('page_ex', 1)
                page_ex = paginator_ex.get_page(page_number_ex)

                is_paginated_ex = page_ex.has_other_pages()

                if page_ex.has_previous():
                    prev_url_ex = '?page_ex={}'.format(page_ex.previous_page_number())
                else:
                    prev_url_ex = ''

                if page_ex.has_next():
                    next_url_ex = '?page_ex={}'.format(page_ex.next_page_number())
                else:
                    next_url_ex = ''

                '''Пагинатор заработано'''
                profit = Order.objects.filter(car=id)
                paginator_pr = Paginator(profit, 5)
                page_number_pr = request.GET.get('page_pr', 1)
                page_pr = paginator_pr.get_page(page_number_pr)

                is_paginated_pr = page_pr.has_other_pages()

                if page_pr.has_previous():
                    prev_url_pr = '?page_pr={}'.format(page_pr.previous_page_number())
                else:
                    prev_url_pr = ''

                if page_ex.has_next():
                    next_url_pr = '?page_pr={}'.format(page_pr.next_page_number())
                else:
                    next_url_pr = ''

                '''Пагинатор ремонт'''
                rep = Repairs.objects.filter(car=id)
                paginator_rep = Paginator(rep, 5)
                page_number_rep = request.GET.get('page_rep', 1)
                page_rep = paginator_rep.get_page(page_number_rep)

                is_paginated_rep = page_rep.has_other_pages()

                if page_rep.has_previous():
                    prev_url_rep = '?page_rep={}'.format(page_rep.previous_page_number())
                else:
                    prev_url_rep = ''

                if page_ex.has_next():
                    next_url_rep = '?page_rep={}'.format(page_rep.next_page_number())
                else:
                    next_url_rep = ''

                context = {

                    "profit": profit,
                    'rep': rep,
                    'page_object_ex': page_ex,
                    'page_object_pr': page_pr,
                    'page_object_rep': page_rep,
                    'is_paginated_ex': is_paginated_ex,
                    'is_paginated_pr': is_paginated_pr,
                    'is_paginated_rep': is_paginated_rep,
                    'next_page_url_ex': next_url_ex,
                    'prev_page_url_ex': prev_url_ex,
                    'next_page_url_pr': next_url_pr,
                    'prev_page_url_pr': prev_url_pr,
                    'next_page_url_rep': next_url_rep,
                    'prev_page_url_rep': prev_url_rep,
                }

                return render(request, "more_details_car.html", context=context)
        except Cars.DoesNotExist:
            return HttpResponseNotFound("<h2>Автомобиль не найден</h2>")

    def get(self, request, id):
            # form = CarFormCreate()
            car = Cars.objects.get(id=id)
            bount_form = CarFormCreate(instance=car)
            context = {
                    'car': car,
                    'form': bount_form,
                }
            return render(request, "more_details_car.html", context=context)

    def post(self, request, id):
        car = Cars.objects.get(id=id)
        if request.method == "POST":

                car.state_number = request.POST.get("state_number")
                car.expenses = request.POST.get("expenses")
                car.Model_caption = request.POST.get("Model_caption")
                car.Spec_caption = request.POST.get("Spec_caption")
                car.Mark_caption = request.POST.get("Mark_caption")
                car.carrying = request.POST.get("carrying")
                car.rent = request.POST.get("rent")
                car.save()
                return HttpResponseRedirect("/cars")
        else:
                return render(request, "more_details_car.html", {"car": car})







# удаление данных из бд
def delete(request, id):
    try:
        cars = Cars.objects.get(id=id)
        cars.delete()
        return HttpResponseRedirect("/cars")
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def deleteEx(request, id):
    try:

        expenses = Expenses.objects.get(id=id)
        expenses.delete()
        return HttpResponseRedirect("/cars/")
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



def create_rep(request, id):
    type = Repairs_type.objects.all()
    worker = Worker.objects.all()
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Repairs()
        type = Repairs_type()
        worker = Worker()
        tom.car = car
        tom.data_start = request.POST.get("data_start")
        tom.data_end = request.POST.get("data_end")
        tom.description = request.POST.get("description")
        # tom.type = type
        # tom.worker = worker
        tom.Repairs_type = type
        tom.Worker = worker
        print(request.POST)
        tom.save()
        return HttpResponseRedirect("/cars" )
    else:
        return render(request, "create_rep.html", {"car": car, "type": type, "worker": worker})

def deleteRep(request, id):
    try:
        rep = Repairs.objects.get(id=id)
        rep.delete()
        return HttpResponseRedirect("/cars/")
    except Repairs.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


class Serch(ListView):
    # поиск

    def get_queryset(self):
        return Cars.objects.filter(state_number__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context
