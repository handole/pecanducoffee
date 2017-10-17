from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, category_slug=None):   
    products = Product.objects.filter(available=True)

    paginator = Paginator(products , 9) # Show 9 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        "page_request_var": page_request_var,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product/detail.html', context)

