from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")

def result(request):
    cls = joblib.load('finalized_model.sav')

    lis = []
    lis.append(request.GET['g'])
    lis.append(request.GET['a'])
    lis.append(request.GET['A'])
    lis.append(request.GET['B'])
    lis.append(request.GET['C'])
    lis.append(request.GET['D'])
    lis.append(request.GET['E'])
    lis.append(request.GET['F'])
    lis.append(request.GET['G'])
    lis.append(request.GET['H'])
    lis.append(request.GET['I'])
    lis.append(request.GET['J'])
    lis.append(request.GET['K'])
    lis.append(request.GET['L'])
    lis.append(request.GET['M'])
    lis.append(request.GET['N'])
    lis.append(request.GET['O'])
    lis.append(request.GET['P'])
    lis.append(request.GET['Q'])
    lis.append(request.GET['R'])
    lis.append(request.GET['S'])
    lis.append(request.GET['T'])
    lis.append(request.GET['U'])
    lis.append(request.GET['V'])

    print(lis)

    newlis = []
    for x in lis:
        if x=="Male":
            x=0
            newlis.append(x)
        elif x=="Female":
            x=1
            newlis.append(x)
        elif x=="Prefer not to say":
            x=2
            newlis.append(x)
        elif x=="Less than 18":
            x=0
            newlis.append(x)
        elif x=="18-30":
            x=1
            newlis.append(x)
        elif x=="More than 30":
            x=2
            newlis.append(x)
        elif x=="Yes":
            x=2
            newlis.append(x)
        elif x=="Sometimes":
            x=1
            newlis.append(x)
        elif x=="No":
            x=0
            newlis.append(x)

    print(newlis)

    ans = cls.predict([newlis])
    print('Answer:------>>>>>>>',ans)
    return render(request, "result.html",{'ans': ans})