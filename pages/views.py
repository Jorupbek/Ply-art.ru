import requests
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from cart.forms import CartAddProductForm
from pages.models import Slider, Contacts, Faq, Pages, About
from shop.models import Product, Category


def home_page_view(request):
    cart_product_form = CartAddProductForm()
    context = {
        'slides': Slider.objects.all(),
        'products': Product.objects.filter(in_home=True)[:8],
        'cart_product_form': cart_product_form,
        'categories': Category.objects.filter(in_home=True).order_by('position')[:5],
        'about': About.objects.first(),
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    context = {
        'contacts': Contacts.objects.first(),
        'about': About.objects.first(),
    }
    return render(request, 'pages/about_us.html', context)


def contacts_page(request):
    return render(request, 'pages/contacts.html', {'contacts': Contacts.objects.first()})


def faq_page(request):
    return render(request, 'pages/faq.html', {'faqs': Faq.objects.all()})


class PagesDetail(DetailView):
    model = Pages
    template_name = 'pages/page_template.html'


class SendFormTelegram(View):

    def get(self, request):
        name = request.GET.get('name', None)
        phone = request.GET.get('phone', None)
        comment = request.GET.get('message', None)
        token = '5100919779:AAFPnAZxhiTF0LGjP6R54ZkCNZlUbkpvBHU'
        chatid = '-726388449'
        message = f'Заявка с сайта \nИмя пользователя: {name}, \nТелефон: {phone} \n' \
                  f'Комментарий {comment}\n\n'

        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
            chat_id=chatid,
            text=message
        ))
        return redirect('home')
