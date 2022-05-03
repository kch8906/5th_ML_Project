
from django.contrib import admin
from django.urls import path, include
from co_eyes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('co_eyes.urls'))
]
