from django.shortcuts import render, HttpResponse
from portfolio.models import Contact
# Create your views here.
def portfolio(request):
    # return HttpResponse("This is my Homepage (/)")
    context = {'name': 'Vinuya', 'course': "Computer Engineer"}
    return render(request, 'portfolio.html', context)

def about(request):
    # return HttpResponse("This is my about page (/)")
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to the db")

    # return HttpResponse("This is my contact page (/)")
    return render(request, 'contact.html')

def projects(request):
    # return HttpResponse("This is my projects [age (/)")
    return render(request, 'projects.html')