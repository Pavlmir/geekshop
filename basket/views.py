from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from mainapp.models import Product
from basket.models import Basket


@login_required
def basket_add(request, product_id):
    # product = get_object_or_404(Product, id=product_id)
    try:
        product_id = int(product_id)
    except Exception as exp:
        print(f"Wrong input numbers! {exp}")
        raise exp
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
    else:
        basket = baskets.first()

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, id):
    try:
        id = int(id)
    except Exception as exp:
        print(f"Wrong input numbers! {exp}")
        raise exp
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    try:
        id = int(id)
        quantity = int(quantity)
    except Exception as exp:
        print(f"Wrong input numbers! {exp}")
        raise exp
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets,
        }
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})