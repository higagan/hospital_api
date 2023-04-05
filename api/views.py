from django.shortcuts import render
from rest_framework import viewsets
from api.models import Hospital,Tasks,SignUp,UserRegistration
from api.serilizer import HospitalSerilizer,TaskSerilizer,SignUpSerilizer,UserRegistrationSerilizer
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import status
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

class LoginView(APIView):
    def post(self, request):
        try:
            # Retrieve the username and password from the request data
            username = request.data.get('username')
            password = request.data.get('password')

            # Query the SignUp model for a user with the given username and password
            user = SignUp.objects.get(username=username, password=password)

            # If a user was found, return a success response
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)

        except SignUp.DoesNotExist:
            # If no user was found, return a failure response
            return Response({'message': 'Failure'}, status=status.HTTP_400_BAD_REQUEST)



