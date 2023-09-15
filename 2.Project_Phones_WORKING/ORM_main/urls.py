from django.contrib import admin
from django.urls import path

from phones.views import index, show_catalog, show_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('catalog/', show_catalog, name='catal'),
    path('catalog/<nazvanie>/', show_product, name='nazv')       # И теперь, всё, что стоит после "catalog/" - будет перебаваться в функцию show_product под названием параметра - nazvanie

]



