from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def all_pupils(request):
    pupils = [
        {'id': 1, 'full_name': 'Inomjon Qurbonov', 'full_ball': 37},
        {'id': 2, 'full_name': 'Shohruxbek Turdaliyev', 'full_ball': 29},
        {'id': 3, 'full_name': 'Zafarbek Olimbayev', 'full_ball': 39},
        {'id': 4, 'full_name': 'Samariddin Baxtiyorov', 'full_ball': 31},
        {'id': 5, 'full_name': 'Ozodbek Ahrorov', 'full_ball': 37}
    ]
    return render(request, 'pupils.html', context={'pupils': pupils})

def pupil(request, id):
    pupils = [
        {'id': 1, 'full_name': 'Inomjon Qurbonov', 'full_ball': 37},
        {'id': 2, 'full_name': 'Shohruxbek Turdaliyev', 'full_ball': 29},
        {'id': 3, 'full_name': 'Zafarbek Olimbayev', 'full_ball': 39},
        {'id': 4, 'full_name': 'Samariddin Baxtiyorov', 'full_ball': 31},
        {'id': 5, 'full_name': 'Ozodbek Ahrorov', 'full_ball': 37},
        {'id': 6, 'full_name': 'Sunnatillo Sharipov', 'full_ball': 00},
    ]

    if id > len(pupils):
        return HttpResponse(f"Bazada {len(pupils)} ta foydalanuvchi bor")
    else:
        return render(request, 'pupil.html', context={'pupil': pupils[id-1]})