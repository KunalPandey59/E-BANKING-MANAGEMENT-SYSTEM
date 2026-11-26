from django.db import models

# Create your models here.
class SignUp1(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    Phno=models.IntegerField()
    Password=models.CharField(max_length=50)
    cmPassword=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    zip=models.IntegerField()
    class Meta:
        db_table="SignUp1"


class complaint(models.Model):
    Name=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Account_type=models.IntegerField()
    Phno=models.IntegerField()
    Email=models.EmailField()
    Inbox=models.CharField(max_length=350)
    class Meta:
        db_table="complaint"



class Admin_signup(models.Model):
    Admin_name=models.CharField(max_length=50)
    Admin_username=models.CharField(max_length=50)
    Admin_ID=models.CharField(max_length=50)
    Admin_email=models.EmailField()
    Phno=models.IntegerField()
    Password=models.CharField(max_length=50)
    cmPassword=models.CharField(max_length=50)
    DOB=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.IntegerField()
    class Meta:
        db_table="Admin_signup"


class trans(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    IFSC=models.CharField(max_length=20)
    accnumber=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField()
    choose=models.CharField(max_length=50)
    scnd_accnumber=models.IntegerField()
    class Meta:
        db_table="trans"

    
