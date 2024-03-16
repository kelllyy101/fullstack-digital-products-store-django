from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review

from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories_filter = request.GET['category'].split(',')
            categories = Category.objects.filter(name__in=categories_filter)
            products = products.filter(category__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            

    current_sorting = f'{sort}_{direction}'

    for p in products:
        p.rating = p.get_rating()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    """ A view to show individual product description """

    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    rating = 0
    if len(reviews) > 0:
        for r in reviews:
            rating += r.rating
        rating = rating/len(reviews)

    context = {
        'product': product,
        'rating': rating,
    }

    return render(request, 'products/product_description.html', context)

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners have permission.')
        return redirect(reverse('home'))

    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Added product!')
            return redirect(reverse('product_description', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners have permission.')
        return redirect(reverse('home'))
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_description', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners have permission.')
        return redirect(reverse('home'))
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))