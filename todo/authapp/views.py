from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
        # print(uname)
        context={}
        if uname=="" or upass=="" or ucpass=="" or uemail=="":
            context['errmsg']="Fields cannot be empty"
            return render(request,"authapp/register",context)
        elif upass!=ucpass:
            context['errmsg']="Password and Conform Mismatched"
            return render(request,"authapp/register",context)
        else:
            u=User.objects.create(username=uname,
                                  email=uemail)
            u.set_password(upass)
            u.save()
            context['success']='Account Created Successfully!!'
            #return HttpResponce("User Created Successfully")
            #return redirect('/authapp/login')

        return redirect('/authapp/login')
    
    else:
        # print("Hello")
        return render(request,"authapp/register.html")

       
    

def user_login(request):
    if request.method =="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        print("Username:",uname)
        print("Userpasseward:",upass)

        u=authenticate(username=uname,password=upass)
        #print("User Object:",u)
        #print("ID:",u.id)
        #print("username:",u.username)
        #print("Password:",u.password)
        #print("Email:",u.email)
        #print("Superuser:",u.is_superuser)
        # return HttpResponse("Deytails Fetched")
        print(u)
        if u is not None:
            login(request,u)
            return redirect('/home')
        else:
            context={}
            context['errmsg']="Invalid Username or Password"
            return render(request,'authapp/login.html',context)

    else:
        return render(request,'authapp/login.html')


def user_logout(request):
    logout(request) #destory data of the logged in user from session.
    return redirect('/authapp/login')
