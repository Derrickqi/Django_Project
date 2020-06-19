from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'user_list.html')
