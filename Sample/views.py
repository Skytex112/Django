from django.shortcuts import render
from django.template.response import TemplateResponse

import random

class Person:
    def __init__(self, name, surname, age = 18, number = ""):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
    
    def __str__(self):
        return f"'name':'{self.name}', 'surname':'{self.surname}', 'age':'{self.age}'"

def constacts(request):
    persons =[
        Person(name = "Name 1", surname= "Surname 1", number="(1111) 111-1111"),
        Person(name = "Name 2", surname= "Surname 2", number="(2222) 222-2222"),
        Person(name = "Name 3", surname= "Surname 3", number="(3333) 333-3333"),
    ]
    return TemplateResponse(request, "contacts.html", {"persons" : persons})

def style(request):
    return render(request, 'main_page.html')

def index(request):
    context = {}
    context["welcome_text"] = "You're welcome"
    context["html_tag"]='<h3 style="color: red;"> HTML tag </h3>'
    
    context["value_int"] = 10
    context["value_float"]= 10.5345
    context["value_bool"] = False
    
    context["list"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sturday", "Sunday"]
    context["dict"] = {"key1":"value1"}
    context["object"] = Person("William", "Butcher", 30)
    context["random_value"] = random.randint(-2,11)
    context["empty_list"] = []
    
    
    return render(request, "index.html", context=context)

def text_format(request):
    return TemplateResponse(request, 'text-format.html', {
        "list":[i for i in range(0, 10)]
    })