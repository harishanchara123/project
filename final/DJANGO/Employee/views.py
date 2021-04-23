
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from Employee.models import Advisor,Book,user
from Employee.serializers import AdvisorSerializer,BookSerializer

from django.core.files.storage import default_storage

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages 

from django.contrib.auth  import authenticate,  login, logout


@csrf_exempt
def AdvisorApi(request,id=0):
    if request.method=='GET':
        departments = Advisor.objects.all()
        departments_serializer = AdvisorSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    


@csrf_exempt
def BookApi(request,id=1):
    if request.method=='GET':
        employees = Book.objects.filter(Id=id)
        employees_serializer = BookSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = BookSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("200_OK",safe=False)
        return JsonResponse("Failed to book.",safe=False)
    



# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['uploadedFile']
#     file_name = default_storage.save(file.name,file)

#     return JsonResponse(file_name,safe=False)










def register(request):
    if request.method=="POST":
        # Get the post parameters
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
    
        myuser = user.objects.create_user(name, email, password)
        myuser.save()
        messages.success(request, "200_OK")
        return redirect('home')

    else:
        return HttpResponse("AD_REQUEST")





def Login(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']

        user=authenticate(username= name, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "200_OK")
            return redirect("home")
        else:
            messages.error(request, "401_AUTHENTICATION_ERROR")
            return redirect("home")

    return HttpResponse("400_BAD_REQUEST")