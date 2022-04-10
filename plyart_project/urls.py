from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pages.views import SendFormTelegram

urlpatterns = [
    path('obivan/', admin.site.urls),
    path('send-msg/', SendFormTelegram.as_view(), name='send_message'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls')),
    path('', include('pages.urls')),
    path('ordres/', include('orders.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
