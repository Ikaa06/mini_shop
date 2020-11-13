import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from home.forms import ReservationForm, ApplicationsForm
from home.models import products


class index(ListView):
    """ Основаная страница """

    def get(self, request, **kwargs):
        data = products.objects.filter(available=True)[:3]

        return render(request, "home/index.html", {'products': data})


class Product(ListView):
    """ Основаная продукт """

    def get(self, request, slug):
        data = products.objects.get(slug=slug)
        return render(request, "home/product.html", {'product': data})


class ProductList(ListView):
    """ Основаная продукт """

    def get(self, request, **kwargs):
        data = products.objects.filter(available=True)
        return render(request, "home/productList.html", {'products': data})


class Save_send(View):
    """
    Сохранение товара
    """

    def post(self, request):
        data = request.POST
        item = products.objects.get(pk=data.get('product'))
        form = ReservationForm(data)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.product = item
            new_item.save()
            response_data = {'status': True, 'message': 'Спасибо за обрашение'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")


class applications_send(View):
    def post(self, request):
        data = request.POST
        form = ApplicationsForm(data)
        if form.is_valid():
            form.save()
            response_data = {'status': True, 'message': 'Спасибо за обрашение'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
