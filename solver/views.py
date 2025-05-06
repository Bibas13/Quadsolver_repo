from django.shortcuts import render
import math

def quadratic_form(request):
    return render(request, 'solver/form.html')

def solve_quadratic(request):
    if request.method != 'POST':
        return render(request, 'solver/form.html')
    try:
        name = request.POST.get('name', '').upper()
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))
    except (ValueError, TypeError):
        return render(request, 'solver/results.html', {
            'name': '',
            'message': 'Please enter valid numbers.',
            'a': '', 'b': '', 'c': '',
            'root1': '', 'root2': ''
        })

    g = b**2 - 4*a*c
    root1 = root2 = None
    message = ""

    if a == 0 and b != 0:
        root1 = -c / b
        message = "This is a linear equation."
    elif a == 0:
        message = "Invalid equation. Both a and b cannot be zero."
    elif g > 0:
        root1 = (-b + math.sqrt(g)) / (2 * a)
        root2 = (-b - math.sqrt(g)) / (2 * a)
        message = "Two distinct real roots."
    elif g == 0:
        root1 = root2 = -b / (2 * a)
        message = "One real repeated root."
    else:
        real = -b / (2 * a)
        imag = math.sqrt(abs(g)) / (2 * a)
        root1 = f"{real} + {imag}i"
        root2 = f"{real} - {imag}i"
        message = "Complex roots."

    context = {
        'name': name,
        'a': a,
        'b': b,
        'c': c,
        'root1': root1,
        'root2': root2,
        'message': message,
    }

    return render(request, 'solver/results.html', context)
