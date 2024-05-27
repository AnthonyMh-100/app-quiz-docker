from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('home/', views.view_home, name='view_home'),
    path('login/', views.view_login, name='view_login'),
    path('', views.redirect_login, name='redirect_login'),
    path('register/', views.view_register, name='view_register'),
    path('logout/', views.view_logout, name='view_logout'),
    path('my/cart/', views.view_cart, name='view_cart'),
    path('generate/cart/', views.view_generate_pdf, name='view_generate_pdf'),
    path('search/product', views.view_search_product, name='view_search_product'),

    path('my/cart/delete/<int:id>', views.view_del_cart, name='view_del_cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)