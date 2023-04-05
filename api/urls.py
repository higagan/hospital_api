from django.contrib import admin
from django.urls import path,include
from api.views import HospitalViewSet,TasksViewSet,SignUpViewSet,UserRegistrationViewSet,login
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'taks', TasksViewSet)
router.register(r'signup', SignUpViewSet)
router.register(r'user_registration', UserRegistrationViewSet)
router.register(r'login', login)
urlpatterns = [    
    path('',include(router.urls))
   


      
]


#companies/{companyId}/employees