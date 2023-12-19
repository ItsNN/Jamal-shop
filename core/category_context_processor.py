from .models import Category


def category_data(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'navbar_categories': categories}
