from django.shortcuts import render
from .models import Room
from django.views import View
from django.shortcuts import redirect
# Create your views here.

# def main(request):
#     return render(request, 'main.html')

class MainView(View):
    def get(self, request):
        return render(request, 'main.html')
    
    def post(self, request):
        if "newname" in request.POST:
            print("I will create new room.")
            print(f"Name: {request.POST.get('newname')}")
            print(f"URL: {request.POST.get('newurl')}")
            return redirect('rooms:main')
        elif "oldcode" in request.POST:
            print("I try to find old room.")
            print(f"Code: {request.POST.get('oldcode')}")
            return redirect('rooms:main')
    

def room(request):
    return render(request, 'rooms/room.html')