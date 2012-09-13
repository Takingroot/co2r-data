from dynamicresponse.response import SerializeOrRender

from django.http import Http404

from co2r.products.models import Product, Footprint


def products(request):
    """
    Returns a list of all products
    """
    products = Product.objects.all()

    return SerializeOrRender('products/list.html', {'products': products})


def product(request, internal_name):
    """
    Returns a list of all products
    """
    product = Product.objects.get(internal_name=internal_name)

    return SerializeOrRender('products/product.html', {'product': product})


def footprints(request):
    footprints = Footprint.objects.all()
    return SerializeOrRender('products/footprints.html', {'footprints': footprints})


def footprint(request, internal_name, year):
    try:
        footprint = Footprint.objects.get(product__internal_name=internal_name,
            year=year)
    except Footprint.DoesNotExist:
        raise Http404

    return SerializeOrRender('products/footprint.html', {'footprint': footprint})

