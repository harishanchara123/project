from django.urls import path

from django.conf.urls import url
from Employee import views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   
    path("user/register/", views.register),


    path("user/login/", views.Login),


    path("user/advisor/", views.AdvisorApi),


  



  


    path("user/advisor/booking/", views.BookApi),

 

]
