import random
from django.shortcuts import render
import datetime
from django.http import HttpResponse

def weekday_view(request):
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    today = datetime.datetime.now().weekday()

    return HttpResponse(f"<h1>Today is: {days[today]}</h1>")



def random_quote(request):
    quotes = [
        "Stay hungry, stay foolish.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "First, solve the problem.",
        "Make it work, make it right, make it fast.",
        "Simplicity is the soul of efficiency."
    ]

    quote = random.choice(quotes)

    return HttpResponse(f"<h1>{quote}</h1>")
