from django.shortcuts import render

def task1(request):
    greeting = None

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        greeting = f'Доброго дня, {first_name} {last_name}!'

    return render(request, 'task1.html', {'greeting': greeting})


def task2(request):
    primes = []

    if request.method == 'POST':
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))

        for num in range(start, end + 1):
            if num > 1:
                is_prime = True

                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break

                if is_prime:
                    primes.append(num)

    return render(request, 'task2.html', {'primes': primes})


def task3(request):
    user = None

    if request.method == 'POST':
        user = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'age': request.POST.get('age'),
            'gender': request.POST.get('gender'),
            'email': request.POST.get('email')
        }

    return render(request, 'task3.html', {'user': user})

def task4(request):
    table = []

    if request.method == 'POST':
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))

        for i in range(start, end + 1):
            row = []

            for j in range(1, 11):
                row.append(f'{i} × {j} = {i * j}')

            table.append(row)

    return render(request, 'task4.html', {'table': table})