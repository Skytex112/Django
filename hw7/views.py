from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant

def restaurants(request):

    if request.method == "POST":
        Restaurant.objects.create(
            name=request.POST['name'],
            specialization=request.POST['specialization'],
            address=request.POST['address'],
            website=request.POST['website'],
            phone=request.POST['phone']
        )
        return redirect('/hw7/restaurants/')

    query = request.GET.get('q')

    if query:
        restaurants = Restaurant.objects.filter(specialization__icontains=query)
    else:
        restaurants = Restaurant.objects.all()

    return render(request, 'restaurants.html', {
        'restaurants': restaurants
    })

def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    restaurant.delete()
    return redirect('/hw7/restaurants/')

def edit_restaurant(request, id):

    restaurant = get_object_or_404(Restaurant, id=id)

    if request.method == "POST":
        restaurant.name = request.POST['name']
        restaurant.specialization = request.POST['specialization']
        restaurant.address = request.POST['address']
        restaurant.website = request.POST['website']
        restaurant.phone = request.POST['phone']
        restaurant.save()

        return redirect('/hw7/restaurants/')

    return render(request, 'edit_restaurant.html', {
        'restaurant': restaurant
    })