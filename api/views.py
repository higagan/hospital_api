from django.shortcuts import render
from rest_framework import viewsets
from api.models import Hospital,Tasks,SignUp,UserRegistration
from api.serilizer import HospitalSerilizer,TaskSerilizer,SignUpSerilizer,UserRegistrationSerilizer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerilizer

    @action(detail=True,methods=['get'])
    def tasks(self,request,pk=None):   
        try:                
            hospital = Hospital.objects.get(pk=pk)
            tasks=Tasks.objects.filter(hospital=hospital)
            tasks_serializer=TaskSerilizer(tasks,many=True,context={'request':request})
            return Response(tasks_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Hospital might not exists !! Error'
            })



class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerilizer


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerilizer

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerilizer

def login(request):
    print("------------")
    print(request)
    print("------------")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = SignUp.objects.get(username=username, password=password)
        
        if user is not None:
            return Response({'message':'User Found'})
        else:
            return Response({'message':'User Not Found'})

  




