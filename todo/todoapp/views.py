from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import TaskList
from django.db.models import Q

# Create your views here.
def contact_page(request):

    return HttpResponse("Hello From contact")

def home_page(request):

    #print("Value:",request.user.is_authenticated)
   if request.user.is_authenticated:
    q1=Q(is_active=1)
    q2=Q(user_id=request.user.id)
    t=TaskList.objects.filter(q1 & q2)
    # return HttpResponse("<h1>Hello from Home Page</h1>")
    # return redirect('/about')
    #t=TaskList.objects.all()  #select *from todoapp_tasklist
    #t=TaskList.objects.filter(is_active=1)

    #print(t)
    for x in t: #[obj1,obj2,obj3,obj4]  accessing each object
        print(x)
        print("ID:",x.id)
        print("Title:",x.title)
        print("detail:",x.detail)
        print("due_dt",x.due_dt)
        print("is_completed",x.is_completed)
        print("is_active",x.is_active)
        print()
        context={}
        context['data']=t
        return render(request,'todoapp/dashboard.html',context)
    else:
        return redirect('authapp/login')


    
def about_page(request):
    
    return HttpResponse("Hello from About Page")

def add_task(request):
    # print("Method :",request.method)
    if request.method == 'POST':
        t=request.POST['title']
        d=request.POST['del']
        dt=request.POST['duedt']
        print('Title:',t)
        print('Details:',d)
        print('Date:',dt)
        t=TaskList.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user) #object created
        t.save() #object save

       #return HttpResponse("Data inserted Successfully into database table")
        return redirect('/home')
    else:
        return render(request,'todoapp/addTask.html')
    

def dtl(request):
    context={}
    context['a']=30
    context['b']=20
    context['l']=[10,20,30,40,50,60]
    context['user']="Shardul"
    return render(request,'todoapp/dashboard.html',context)

def delete_task(request,rid):
    #print("ID to be deleted:",rid)
    #return HttpResponse("ID to be deleted:"+rid)
    #t=TaskList.objects.get(id=rid)  #select * from tablename where id =3
    #print(t)
    #t.delete()     # HARD DELETE
    #return HttpResponse("object Delete")

    t=TaskList.objects.filter(id=rid)
    t.update(is_active=0)    #SOFT DELETE
    return redirect('/home')


def edit_task(request,rid):
    #print("ID to be edit:",rid)
    #return HttpResponse("ID to be edit:"+rid)
    if request.method=="POST":
        ut=request.POST['title']
        ud=request.POST['det']
        udt=request.POST['duedt']
        # print("Update Title:",ut)
        # print("Update Details:",ud)
        # print("Update Data:",udt)
        t=TaskList.objects.filter(id=rid)
        t.update(title=ut,detail=ud,due_dt=udt)
        return redirect("/home")
        #return HttpResponse("Details Fetched")

    else:
        t=TaskList.objects.get(id=rid)
        context={}
        context['data']=t
        return render(request,'todoapp/editform.html',context) 
    

def mark_complated(request,rid):

    t=TaskList.objects.filter(id=rid)
    t.update(is_completed=1)

    return redirect('/home')
    