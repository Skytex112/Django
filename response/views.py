from django.shortcuts import render

def reviews_view(request):
    reviews_list = [
        {
            "text": "Курс по Django був дуже корисним та цікавим!",
            "date": "02.06.2026"
        },
    ]
    
    context = {
        'reviews': reviews_list
    }
    
    return render(request, 'reviews.html', context)