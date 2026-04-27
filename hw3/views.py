from django.http import HttpResponse
from django.shortcuts import redirect

history_data = {
    1885: "У Франції в 1885 році відбувалися важливі політичні події.",
    1914: "У 1914 році почалася Перша світова війна."
}

cities_data = {
    "Paris": {
        1924: "У 1924 році в Парижі проходили Олімпійські ігри."
    },
    "Marseille": {
        1956: "У 1956 році в Марселі відбувалися значні події."
    }
}

def history_home(request):
    return HttpResponse("<h1>Розділ Історія</h1>")


def history_year(request, year):
    if year in history_data:
        return HttpResponse(f"<h1>{history_data[year]}</h1>")
    return redirect('/history/')


def cities_home(request):
    city = request.GET.get('city')
    year = request.GET.get('year')

    if city and year:
        try:
            year = int(year)
        except:
            return redirect('/cities/')

        if city in cities_data and year in cities_data[city]:
            return HttpResponse(f"<h1>{cities_data[city][year]}</h1>")

        return redirect('/cities/')

    return HttpResponse("<h1>Сторінка міст</h1>")


def city_year(request, city, year):
    if city in cities_data and year in cities_data[city]:
        return HttpResponse(f"<h1>{cities_data[city][year]}</h1>")
    return redirect('/cities/')

