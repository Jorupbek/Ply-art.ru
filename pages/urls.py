from django.urls import path

from pages.views import home_page_view, contacts_page, faq_page, about_page, PagesDetail

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about-us/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
    path('faq/', faq_page, name='faq'),
    path('<slug:slug>/', PagesDetail.as_view(), name='pages'),
]
