from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView
from .forms import WorkerForm,  PosFormCreate

from django.views.generic import View

from .render import Render

from django.db.models import Q

from django.core.paginator import Paginator

from .models import Worker, Position, Tabel_time



def workers(request):
    search_query = request.GET.get('search', '')

    if search_query:
        worker = Worker.objects.filter(Q(first_name__icontains=search_query) | Q(middle_name__icontains=search_query) | Q(last_name__icontains=search_query))
    else:
        worker = Worker.objects.all()

    paginator = Paginator(worker, 10)
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
        'prev_page_url': prev_url,

    }
    return render(request, 'workers.html', context=context)


class CreateWorker(View):
    def get(self, request):

        template = 'create_worker.html'
        context = {

                'list_articles': Worker.objects.all().order_by('-id'),
                'form': WorkerForm(),

        }
        return render(request, template, context)

    def post(self, request):
        bound_form = WorkerForm(request.POST)
        context = {'form': bound_form}
        if bound_form.is_valid():
            new = bound_form.save()

            return HttpResponseRedirect("/workers")

        return render (request, 'create_worker.html', context=context)



def create_pos(request):
    success = False
    if request.method == 'POST':
        form = PosFormCreate(request.POST)
        if form.is_valid():
            form.save()
            success = True
            return HttpResponseRedirect("/workers")

    template = 'create_pos.html'
    context = {
        'list_articles': Position.objects.all().order_by('-id'),
        'form': PosFormCreate(),
        'success': success
    }
    return render(request, template, context)


# изменение данных в бд
class Edit(View):
    def get(self, request, id):
            # form = CarFormCreate()
            tom = Worker.objects.get(id=id)
            #pos = Position.objects.all()
            bount_form = WorkerForm(instance=tom)
            context = {

                    'form': bount_form,
                    #'position': pos,
                    'worker': tom,
                }

            return render(request, "edit_worker.html", context=context)

    def post(self, request, id):
        tom = Worker.objects.get(id=id)
        #pos = Position.objects.all()
        context = {
            #'position': pos,
            'worker': tom,
        }
        if request.method == "POST":
                #type = Type_customer(id=id)
                #type.id = request.POST.get("T_customer")

                pos = Position(id=id)
                pos.id = request.POST.get("P_position")

                # tom.position = request.POST.get("position")

                tom.first_name = request.POST.get("first_name")
                tom.middle_name = request.POST.get("middle_name")
                tom.last_name = request.POST.get("last_name")
                tom.phone = request.POST.get("phone")
                tom.passport = request.POST.get("passport")
                tom.adress = request.POST.get("adress")
                tom.P_position = pos
                tom.save()
                return HttpResponseRedirect("/workers")
        else:
                return render(request, "edit_worker.html", context=context)



def tabel(request, id):
    try:
        tab = Tabel_time.objects.get(worker_id=id)
        if request.method == "POST":
            tab.worker = id
            tab.day1 = request.POST.get("day1")
            tab.day2 = request.POST.get("day2")
            tab.day3 = request.POST.get("day3")
            tab.day4 = request.POST.get("day4")
            tab.day5 = request.POST.get("day5")
            tab.day6 = request.POST.get("day6")
            tab.day7 = request.POST.get("day7")
            tab.day8 = request.POST.get("day8")
            tab.day9 = request.POST.get("day9")
            tab.day10 = request.POST.get("day10")
            tab.day11 = request.POST.get("day11")
            tab.day12 = request.POST.get("day12")
            tab.day13 = request.POST.get("day13")
            tab.day14 = request.POST.get("day14")
            tab.day15 = request.POST.get("day15")
            tab.day16 = request.POST.get("day16")
            tab.day17 = request.POST.get("day17")
            tab.day18 = request.POST.get("day18")
            tab.day19 = request.POST.get("day19")
            tab.day20 = request.POST.get("day20")
            tab.day21 = request.POST.get("day21")
            tab.day22 = request.POST.get("day22")
            tab.day23 = request.POST.get("day23")
            tab.day24 = request.POST.get("day24")
            tab.day25 = request.POST.get("day25")
            tab.day26 = request.POST.get("day26")
            tab.day27 = request.POST.get("day27")
            tab.day28 = request.POST.get("day28")
            tab.day29 = request.POST.get("day29")
            tab.day30 = request.POST.get("day30")
            tab.day31 = request.POST.get("day31")
            tab.save()
            return HttpResponseRedirect("/workers")
        else:
            return render(request, 'table_time.html', {'tab': tab})
    except Tabel_time.DoesNotExist:
        if request.method == "POST":
            tabel.worker = id

            tabel.save()
            return HttpResponseRedirect("/workers")
        else:
            return render(request, "table_time.html", {"tabel": tabel})

# удаление данных из бд
def delete(request, id):
    try:
        person = Worker.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/workers")
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

