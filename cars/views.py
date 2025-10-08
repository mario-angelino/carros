from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request):
    search = request.GET.get('search')

    # cars = Car.objects.all()
    # cars = Car.objects.filter(brand__name='FIAT')
    # cars = Car.objects.filter(model__contains='Chevete') icontains ignora letras maiúsculas e minúsculas
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    else:
        # order_by('-model') ordena invertido
        cars = Car.objects.all().order_by('model')

    return render(
        request,
        template_name='cars.html',
        context={'cars': cars}
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        template_name='new_car.html',
        context={'new_car_form': new_car_form}
    )
