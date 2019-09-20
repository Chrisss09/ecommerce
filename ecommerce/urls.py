from django.contrib import admin
from django.urls import path, include
from accounts.views import index, logout, login, register, profile
from products import urls as urls_products
from products.views import all_products
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name='index'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include(urls_products)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
