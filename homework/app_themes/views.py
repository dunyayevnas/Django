from django.shortcuts import render

# Create your views here.

def themes_list(reuest):
    list_les = []
    with open('lessons.txt', 'r') as file:
        for f in file:
            list_les.append(f)

    return render(reuest, 'themes.html', context= {'list_les': list_les})
