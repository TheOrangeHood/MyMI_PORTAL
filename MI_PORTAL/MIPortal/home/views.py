from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import CoordieAssignedTask
from django.contrib.auth.decorators import login_required
from .decorators import  allowed_users

# password for test user is Harry$$$***000
# Create your views here.
@login_required(login_url='/login')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['Admin'])
def assignedTask(request):
    # if request.user=='admin':
        # user = self.request.user
        alltasks = CoordieAssignedTask.objects.filter(cg=request.user)
        # alltasks = CoordieAssignedTask.objects.all()

        # alltasks = CoordieAssignedTask.objects.filter(coordieID=request.user)
        context = {'tasks': alltasks}
        return render(request, 'assignedTask.html',context)
    # else:
    #     alltasks = CoordieAssignedTask.objects.filter(coordieID='request.user')
    #     context = {'tasks': alltasks}
    #     return render(request, 'assignedTask.html',context)


@login_required(login_url='/login')
def assignedTask_coordie(request):
    # if request.user=='admin':
        # user = self.request.user
        # alltasks = CoordieAssignedTask.objects.all()
        alltasks = CoordieAssignedTask.objects.filter(coordieID=request.user)
        context = {'tasks': alltasks}
        return render(request, 'assignedTask.html',context)
    # else:
    #     alltasks = CoordieAssignedTask.objects.filter(coordieID='request.user')
    #     context = {'tasks': alltasks}
    #     return render(request, 'assignedTask.html',context)


@login_required(login_url='/login')
@allowed_users(allowed_roles=['Admin'])
def addTask(request):
    if request.method=="POST":
        cg = request.user
        coordieID = request.POST.get('coordieID')
        coordieEmail = request.POST.get('coordieEmail')
        coordieTask  = request.POST.get('coordieTask')
        taskCompleted = False
        print(coordieID,coordieEmail,coordieTask)
        ins = CoordieAssignedTask(cg=cg,coordieID=coordieID,coordieEmail=coordieEmail,coordieTask=coordieTask,taskCompleted=taskCompleted)
        ins.save()
        print("The task has been added")
        # return redirect(request, 'addTask.html')
    return render(request, 'addTask.html')

@login_required(login_url='user-login')
# # @allowed_users(allowed_roles=['Admin'])
@allowed_users(allowed_roles=['Admin'])
def deleteTask(request, pk):
    task = CoordieAssignedTask.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('assigned')
    context = {
        'task': task
    }
    return render(request, 'deleteTask.html', context)

@login_required(login_url='user-login')
# # @allowed_users(allowed_roles=['Admin'])
# @allowed_users(allowed_roles=['Admin'])
def completeTask(request, pk):
    task = CoordieAssignedTask.objects.get(id=pk)
    if request.method == 'POST':
        task.taskCompleted = True
        task.save()
        return redirect('assigned_coordie')
    context = {
        'task': task
    }
    return render(request, 'completeTask.html', context)
# def saveTask(request):
    
# @login_required(login_url='/login')
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method=="POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username, password)

        # check if user has entered correct credentials
         user = authenticate(username=username, password=password)

         if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

         else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
