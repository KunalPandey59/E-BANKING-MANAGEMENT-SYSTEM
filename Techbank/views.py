from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from Techbank.models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def Reg(request):
    return render(request,'Reg.html')
def Register(request):
    r=SignUp1()
    r.fullname=request.GET['fullname']
    r.username=request.GET['username']
    r.email=request.GET['email']
    r.Phno=request.GET['Phno']
    r.Password=request.GET['Password']
    r.cmPassword=request.GET['cmPassword']
    r.DOB=request.GET['DOB']
    r.address=request.GET['address']
    r.city=request.GET['city']
    r.state=request.GET['state']
    r.zip=request.GET['zip']
    r.save()
    return render(request,'Reg.html')

def showuserreg(request):
    r=SignUp1.objects.all()
    return render(request,'showuserreg.html',{'r':r})
def showuserpage(request):
    r=SignUp1.objects.all()
    return render(request,'showuserpage.html')

def userlogin(request):
    return render(request,'userlogin.html')
def userlog(request):
    a=request.GET['email']
    b=request.GET['Password']
    if SignUp1.objects.filter(email=a,Password=b):
        return render(request,'showuserpage.html')
    else:
        return render(request,'userlogin.html')

def logout_user(request):
    logout1(request)
    return redirect('userlogin.html')


    

def adminregpage(request):
    return render(request,'adminregpage.html')
def adminreg(request):
    A=Admin_signup()
    A.Admin_name=request.GET['Admin_name']
    A.Admin_username=request.GET['Admin_username']
    A.Admin_email=request.GET['Admin_email']
    A.Phno=request.GET['Phno']
    A.Password=request.GET['Password']
    A.cmPassword=request.GET['cmPassword']
    A.DOB=request.GET['DOB']
    A.address=request.GET['address']
    A.city=request.GET['city']
    A.state=request.GET['state']
    A.zip=request.GET['zip']
    A.save()
    return render(request,'adminregpage.html')

def showadminreg(request):
    A=Admin_signup.objects.all()
    return render(request,'showadminreg.html',{'A':A})
def showadminpage(request):
    A=Admin_signup.objects.all()
    return render(request,'showadminpage.html')

def adminlogin(request):
    return render(request,'adminlogin.html')
def adminlog(request):
    a=request.GET['Admin_email']
    b=request.GET['Admin_ID']
    c=request.GET['Password']
    if Admin_signup.objects.filter(Admin_email=a,Password=c):
        return render(request,'showadminpage.html')
    else:
        return render(request,'adminlogin.html')

def logout_admin(request):
    logout2(request)
    return redirect('adminlogin.html')

def usercomplaint(request):
    return render(request,'usercomplaint.html')
def complnt(request):
    c=complaint()
    c.Name=request.GET['Name']
    c.Username=request.GET['Username']
    c.Account_type=request.GET['Account_type']
    c.Phno=request.GET['Phno']
    c.Email=request.GET['Email']
    c.Inbox=request.GET['Index']
    c.save()
    return render(request,'usercomplaint.html')

def showcomplaint(request):
    c=complaint.objects.all()
    return render(request,'showcomplaint.html',{'c':c})



def transaction(request):
    return render(request,'transaction.html')
def transaction2(request):
    return render(request,'transaction2.html')
def transfer(request):
    t=trans()
    t.name=request.GET['name']
    t.email=request.GET['email']
    t.IFSC=request.GET['IFSC']
    t.accnumber=request.GET['accnumber']
    t.amount=request.GET['amount']
    t.date=request.GET['date']
    t.choose=request.GET['choose']
    t.scnd_accnumber=request.GET['scnd_accnumber']
    t.save()
    return render(request,'transaction.html')
def showtrans(request):
    t=trans.objects.all()
    return render(request,'showtrans.html',{'t':t})



def edit(request,id):
    A=Admin_signup.objects.get(id=id)
    return render(request,'edit.html',{'A':A}) 
def edcode(request,id):
    A=Admin_signup.objects.get(id=id)
    A.Admin_name=request.GET['a1']
    A.Admin_email=request.GET['a2']
    A.pwd=request.GET['a3']
    A.phno=request.GET['a4']
    A.save()
    return redirect('../showtrans.html')

def contact_us(request):
    return render(request,'contact_us.html')

def admin_dele(request,id):
    A=Admin_signup.objects.get(id=id)
    A.delete()
    return redirect('../showadminreg')

def trans_dele(request,id):
    t=trans.objects.get(id=id)
    t.delete()
    return redirect('../showtrans')

def user_dele(request,id):
    r=SignUp1.objects.get(id=id)
    r.delete()
    return redirect('../showuserregpage')


def customer_details(request):
    r=SignUp1.objects.all()
    return render(request,'customer_details.html')





CUSTOMERS = [
    {'account_no': 'Jane Doe', 'name': 'Jane Doe', 'email': 'jane@email.com', 'balance': '$5,200', 'account_type': 'Savings'},
    {'account_no': '100789012', 'name': 'John Smith', 'email': 'john@email.com', 'balance': '$2,950', 'account_type': 'Checking'},
]

def search_customer(request):
    customer_data = username
    if request.method == 'POST':
        name = request.POST.get('name')
        account_no = request.POST.get('account_no')
        for customer in CUSTOMERS:
            if customer['name'].lower() == name.lower() and customer['account_no'] == account_no:
                customer_data = customer
                break
    return render(request, 'search_customer.html', {'customer': customer_data})

def balance_quary(request):
    return render(request,'balance_quary.html')