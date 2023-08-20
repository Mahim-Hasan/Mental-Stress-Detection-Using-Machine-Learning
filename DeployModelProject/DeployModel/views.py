from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")

def result(request):
    cls = joblib.load('finalized_model.sav')
    data = request.POST

    lis = []
    lis.append(data['g'])
    lis.append(data['a'])
    lis.append(data['A'])
    lis.append(data['B'])
    lis.append(data['C'])
    lis.append(data['D'])
    lis.append(data['E'])
    lis.append(data['F'])
    lis.append(data['G'])
    lis.append(data['H'])
    lis.append(data['I'])
    lis.append(data['J'])
    lis.append(data['K'])
    lis.append(data['L'])
    lis.append(data['M'])
    lis.append(data['N'])
    lis.append(data['O'])
    lis.append(data['P'])
    lis.append(data['Q'])
    lis.append(data['R'])
    lis.append(data['S'])
    lis.append(data['T'])
    lis.append(data['U'])
    lis.append(data['V'])

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