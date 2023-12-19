from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from core.forms import CommentForm
from core.models import Category, MenuItem, Comment, SubCategory


# Create views here.
class MenuListView(ListView):
    template_name = 'pages/menu_page.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        queryset = MenuItem.objects.filter(available=True)

        if subcategory_slug:
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            queryset = queryset.filter(subcategory=subcategory)
        elif category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query),
                available=True
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.kwargs.get('category_slug')
        context['subcategory'] = self.kwargs.get('subcategory_slug')
        return context


# View for products that are on offer.
class OfferedProductListView(ListView):
    template_name = 'pages/offer_products.html'  
    context_object_name = 'offered_products'

    def get_queryset(self):
        return MenuItem.objects.filter(on_offer=True, available=True)


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'pages/menu_item_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
    queryset = MenuItem.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_item = self.get_object()

        # Fetch comments related to the menu item
        comments = Comment.objects.filter(menu_item=menu_item)
        context['comments'] = comments
        context['cart_product_form'] = CartAddProductForm()
        context['comment_form'] = CommentForm()

        recommended_products = MenuItem.objects.filter(
            available=True,
            subcategory=menu_item.subcategory
        ).exclude(id=menu_item.id)
        context['recommended_products'] = recommended_products[:4]

        return context

    def post(self, request, *args, **kwargs):
        menu_item = self.get_object()

        # Process the comment form submission
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = self.request.user
            new_comment.menu_item = menu_item
            new_comment.save()
            messages.success(request, 'your comment is added.')
            return redirect('menu_item_detail', slug=menu_item.slug)

        return self.get(request, *args, **kwargs)
