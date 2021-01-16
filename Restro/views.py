from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login



from django.shortcuts import render
def home(request):
    return render(request, 'Restro/index.html')
def book_a_table(request):
    return render(request, 'Restro/book a table.html')


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'Restro/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return render(request, 'Restro/thanks_for_registration.html')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def menu(request):
    return render(request, 'Restro/menu.html')
def drinks(request):
    return render(request, 'Restro/drinks.html')
def healthy_food(request):
    return render(request, 'Restro/healthy_food.html')
def organic_food(request):
    return render(request, 'Restro/organic_food.html')
def cakes(request):
    return render(request, 'Restro/cakes.html')
def sea_food(request):
    return render(request, 'Restro/sea_food.html')
def spicy(request):
    return render(request,'Restro/spicy.html')
def meat_dish(request):
    return render(request, 'Restro/meat_dish.html')
def order_breakfast(request):
    return render(request,'Restro/order_breakfast.html')
def order_lunch(request):
    return render(request,'Restro/order_lunch.html')
def order_dinner(request):
    return render(request,'Restro/order_dinner.html')
def cheese_dish(request):
    return render(request,'Restro/cheese_dish.html')
def pizzas(request):
    return render(request,'Restro/pizzas.html')
def desserts(request):
    return render(request,'Restro/desserts.html')