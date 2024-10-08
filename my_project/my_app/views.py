import random
from django.shortcuts import render

def hello_world(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guess_number(request):
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        number = request.session.get('number')

        if guess < number:
            message = "Загадане число більше!"
        elif guess > number:
            message = "Загадане число менше!"
        else:
            message = "Вітаємо! Ви вгадали число!"
            number = random.randint(1, 100)
            request.session['number'] = number
    else:
        number = random.randint(1, 100)
        request.session['number'] = number
        message = ""

    return render(request, 'guess_number.html', {'message': message})
