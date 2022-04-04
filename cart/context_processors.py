from cart.cart import Cart
from pages.models import Contacts, Pages


def cart(request):
    context = {
        'contacts': Contacts.objects.first(),
        'pages_list': Pages.objects.all(),
        'cart': Cart(request)
    }
    return context
