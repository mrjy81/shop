from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shopify import settings
from .views import home_page, header, footer

urlpatterns = [
    path('', home_page, name='home'),
    path('header/', header, name="header"),
    path('footer/', footer, name="footer"),
    path('admin/', admin.site.urls),
    path('account/', include('shop_account.urls')),
    path('products/', include('shop_products.urls')),
    path('contact-us/', include('shopify_contact_us.urls')),
    path('site-settings/', include('siteSetting.urls')),
    path('session-orders/', include('sessions_order.urls')),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
