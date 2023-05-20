from django.shortcuts import render

def printindex(request):

    return render(request,"index.html")