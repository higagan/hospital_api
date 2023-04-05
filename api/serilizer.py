from .models import Hospital,Tasks,SignUp,UserRegistration
from rest_framework import serializers

class HospitalSerilizer(serializers.HyperlinkedModelSerializer):
    hospital_id = serializers.ReadOnlyField()
    class Meta:
        model = Hospital
        fields="__all__"

class TaskSerilizer(serializers.HyperlinkedModelSerializer):
    task_id = serializers.ReadOnlyField()
    class Meta:
        model = Tasks
        fields="__all__"

class SignUpSerilizer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = SignUp
        fields="__all__"

class UserRegistrationSerilizer(serializers.HyperlinkedModelSerializer):
    registration_id = serializers.ReadOnlyField()
    class Meta:
        model = UserRegistration
        fields="__all__"


