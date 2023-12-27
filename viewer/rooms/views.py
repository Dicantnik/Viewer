from django.shortcuts import render
from .models import Room
from django.views import View
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
# Create your views here.

# def main(request):
#     return render(request, 'main.html')
from .models import Room

class MainView(View):
    def get(self, request):
        return render(request, 'main.html')
    
    def post(self, request):
        args = request.POST
        ctx = {}
        if "newname" in request.POST:
            if request.user.is_authenticated:
                splink = args.get('newurl').split('?')[1]
                splink = splink.split('&')[0][2:]
                print(splink)
                url = 'https://www.youtube.com/embed/' + splink
                newroom = Room(name=args.get('newname'), link=url, videocode = splink,
                               user=request.user)
                newroom.save()
                return redirect("rooms:room", code=newroom.code)
            else:
                ctx = {"status":"error_create"}
            return render(request, 'main.html', ctx)
        elif "oldcode" in request.POST:
            print("I try to find old room.")
            print(f"Code: {args.get('oldcode')}")
            try:
                room = Room.objects.all().get(code=args.get('oldcode'))
                return redirect("rooms:room", code=args.get('oldcode'))
            except:
                ctx = {"status":"error_find"}
                return render(request, 'main.html', ctx)
    

def room(request, code):
    room = Room.objects.get(code=code)
    ctx = {"room": room}
    return render(request, 'rooms/room.html', ctx)


def profileview(request):
    if request.user.is_authenticated:
        user = request.user
        rooms = Room.objects.all().filter(user=user)
        ctx = {'rooms':rooms}
        return render(request, 'rooms/profile.html', ctx)
    else:
        return PermissionDenied()