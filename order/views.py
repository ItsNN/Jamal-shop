from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import OrderItem, Order



class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pages/cart/order_checkout.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order_history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)  

        if self.request.user.is_authenticated:
            order.user = self.request.user  # Assign the logged-in user to the order

        order.save()  # Save the order with the user
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        messages.success(self.request, 'Your order has been placed successfully.')
        return super().form_valid(form)


class OrderHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/order-summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user).order_by('-created')
        context['orders'] = orders
        return context
