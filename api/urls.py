from django.contrib import admin
from django.urls import path,include
from api.views import HospitalViewSet,TasksViewSet,SignUpViewSet,UserRegistrationViewSet,LoginView
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'taks', TasksViewSet)
router.register(r'signup', SignUpViewSet)
router.register(r'user_registration', UserRegistrationViewSet)

urlpatterns = [    
    path('',include(router.urls)),
      path('login/', LoginView.as_view())
   


      
]


#companies/{companyId}/employees