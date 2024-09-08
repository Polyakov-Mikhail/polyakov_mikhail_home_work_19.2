from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Негодяй по имени {name} оставил номер телефона {phone} с текстом "{message}"')
    return render(request, "contacts.html")


def unit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Негодяй по имени {name} оставил почту {email} с текстом {message}')
    return render(request, "unit.html")
