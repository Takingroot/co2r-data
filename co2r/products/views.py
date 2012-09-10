from dynamicresponse.response import SerializeOrRender

from co2r.products.models import Product

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
