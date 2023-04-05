from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=100)   
    address = models.CharField(max_length=100)
    about = models.TextField()
    contact = models.CharField(max_length=100)
    added_date = models.DateTimeField()
    added_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    date =  models.DateField()
    shift = models.CharField(max_length=100,choices=
                           (('Morning','Morning (6 AM - 2 AM)'),
                           ('Afternoon','Afternoon (2 PM - 8 PM)'),
                           ("Night",'Night (9 PM - 6 AM)')
                           ))

    department = models.CharField(max_length=100, choices=
                           (('Ward','Ward'),
                           ('ICU','ICU'),
                           ("Emergency",'Emergency')
                           ))

    qualification = models.CharField(max_length=100, choices=
                           (('MBBS','MBBS'),
                           ('AYUSH','AYUSH'),
                           ("BDS",'BDS'),
                           ("Nursing",'Nursing')
                           ))
 
  
    added_date=models.DateTimeField(auto_now=True)  
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE)

class SignUp(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=(("Doctor","Doctor"),("Hospital","Hospital")))
    def __str__(self):
        return username

class UserRegistration(models.Model):
    registration_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100,choices=
                           (('Ward','Ward'),
                           ('ICU','ICU'),
                           ("Emergency",'Emergency')
                           ))
    qualification = models.CharField(max_length=100,choices=
                           (('MBBS','MBBS'),
                           ('AYUSH','AYUSH'),
                           ("BDS",'BDS'),
                           ("Nursing",'Nursing')
                           ))
    added_date=models.DateTimeField(auto_now=True)  

    user_id=models.ForeignKey(SignUp, on_delete=models.CASCADE)
    # registration_id=models.ForeignKey(SignUp, on_delete=models.CASCADE)
  










