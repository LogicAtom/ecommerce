from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None # Start with None to ensure no error when searching with no search term
# Check if request.get exists, if 'q' is in request then set it as a request called query
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query: # if query is blank then it wont return any results
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Constructing queries
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # Pass queries to a filter
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)