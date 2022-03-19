from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def index(request):
    queryset = Products.objects.all()
    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        queryset = queryset.filter(title__icontains=item_name)
    # paginator
    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    return render(request, 'Shop/index.html', {'queryset': queryset})


def details(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'Shop/detail.html', {'product': product})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()
    return render(request, 'Shop/checkout.html')