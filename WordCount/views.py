from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    return render(request,'HomePage.html',{'text':'This is from the dictionary'})

def WordCount(request):
    AllText= request.GET['alltext']
    wordCount=AllText.split()
    return render(request,'countpage.html',{'AllText':AllText,'length':len(wordCount)})

def AboutUs(request):
    return render(request,'AboutPage.html')