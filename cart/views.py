from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import MenuItem
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    menu_items = get_object_or_404(MenuItem, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        cart.add(product=menu_items,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    menu_items = get_object_or_404(MenuItem, id=product_id)
    cart.remove(menu_items)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'pages/cart/cart_detail.html', {'cart': cart})
