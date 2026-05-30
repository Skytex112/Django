from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Book, Reader

def register(request):

    error = None

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            error = "Паролі не співпадають"

        elif User.objects.filter(username=username).exists():
            error = "Користувач вже існує"

        else:
            User.objects.create_user(username=username, password=password)
            return redirect('/hw6/login/')

    return render(request, 'register.html', {'error': error})


def user_login(request):

    error = None

    if request.method == 'POST':

        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('/hw6/books/')
        else:
            error = "Невірний логін або пароль"

    return render(request, 'login.html', {'error': error})


@login_required
def books(request):

    mode = request.GET.get('mode')

    if mode == 'available':
        books = Book.objects.filter(is_available=True)
    else:
        books = Book.objects.all()

    return render(request, 'books.html', {'books': books})


@login_required
def readers(request):

    return render(request, 'readers.html', {
        'readers': Reader.objects.all()
    })


@login_required
def add_book(request):

    if request.method == 'POST':

        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            year=request.POST['year'],
            style=request.POST['style'],
            publisher=request.POST['publisher']
        )

        return redirect('/hw6/books/')

    return render(request, 'add_book.html')

@login_required
def add_reader(request):

    if request.method == 'POST':

        Reader.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            registration_date=request.POST['date']
        )

        return redirect('/hw6/readers/')

    return render(request, 'add_reader.html')

@login_required
def take_book(request, book_id):

    book = Book.objects.get(id=book_id)

    reader = Reader.objects.first()

    if book.is_available:
        book.reader = reader
        book.is_available = False
        book.save()

    return redirect('/hw6/books/')