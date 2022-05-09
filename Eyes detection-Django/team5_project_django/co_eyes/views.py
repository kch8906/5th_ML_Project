from .models import Predictlabel, Temp
from django.shortcuts import redirect, render


# Create your views here.
def co_eyes(request):
    class_object = Temp.objects.last()
    return render(request, "main.html", {'class_object': class_object})
