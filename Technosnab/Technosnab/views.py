from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_order(request):
    return redirect('orders', permanent=True)