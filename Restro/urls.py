
from django.conf.urls import url
from . import views

app_name = 'Restro' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    url('book_table/', views.user_register, name='user_register'),
    url('menu/', views.menu, name='menu'),
    url('drinks/', views.drinks, name='drinks'),
    url('healthy_food/', views.healthy_food, name='healthy_food'),
    url('organic_food/', views.organic_food, name='organic_food'),
    url('cakes/', views.cakes, name='cakes'),
    url('sea_food/', views.sea_food, name='sea_food'),
    url('spicy/', views.spicy, name='spicy'),
    url('meat_dish/', views.meat_dish, name='meat_dosh'),
    url('order_breakfast/', views.order_breakfast, name='order_breakfast'),
    url('order_lunch/', views.order_lunch, name='order_lunch'),
    url('order_dinner/', views.order_dinner, name='order_dinner'),
    url('cheese_dish/', views.cheese_dish, name='cheese_dish'),
    url('pizzas/', views.pizzas, name='pizzas'),
    url('desserts/', views.desserts, name='desserts'),
    url('', views.home),

]
