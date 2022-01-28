from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    #Query the database fro a list of ALL categories currently stored.
    #Order the categories by number of likes in descending order.
    #Retrive the top 5 only -- or all if less than 5.
    #Place the list in our contex_dict dictionary (with our boldmessage!)
    #that will be passed to the template engine.
    category_list=Category.objects.order_by('-likes')[:5]

    context_dict={}
    context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']=category_list

    #REnder the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
