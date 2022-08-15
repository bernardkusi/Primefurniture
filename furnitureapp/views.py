# Create your views here.
from random import Random, random
from django.shortcuts import redirect, render
from .forms import MessageForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import items,purchase

# Create your views here.
def index(request):
    itemlist=items.objects.all()[0:8]
    context={'items':itemlist}
    return render(request,'index.html',context)

def product(request,pk):
    product=items.objects.get(id=pk)
    itemlist=items.objects.all()[0:4]
    context={'product':product,'items':itemlist}
    return render(request,'product.html',context)


def products(request):
    itemlist=items.objects.all()
    context={'items':itemlist}
    return render(request,'products.html',context)


def cart(request):
    if(request.user.is_authenticated):
        cart=purchase.objects.filter(userid=request.user,status=False)
        number=len(cart)
        total=0
        for x in cart:
            total+=x.itemid.itemprice            
        context={'cart':cart,'number':number,'total':total}
        return render(request,'cart.html',context)
    messages.info(request,"Please log in to start shopping")
    return redirect('signin')


def purchases(request,pk):
    if(request.user.is_authenticated):
        item=items.objects.get(id=pk)
        check=purchase.objects.filter(itemid=item,userid=request.user,status=False).exists()
        if(check):
            print('Item Already exists')
        else:
            product=purchase.objects.create(itemid=item,userid=request.user)
        return redirect('cart')
    messages.info(request,"Please log in to start shopping")
    return redirect('signin')
    

def remove(request):
    if(request.user.is_authenticated):
        itemid=request.POST.get("removeid")
        product=purchase.objects.get(itemid=itemid,userid=request.user,status=False)
        product.delete()
    return redirect('cart')

def order(request):
    if(request.user.is_authenticated):
        if request.method=="POST":
            products=purchase.objects.filter(userid=request.user,status=False)
            for item in products:
                item.status=True
                item.save()
            messages.info(request,"Order placed successfully")
            return redirect('index')
        else:
            return redirect('index')
    else:
        messages.info(request,"Please log in to start shopping")
        return redirect('signup')

def message(request):
    if(request.method=="POST"):
        form=MessageForm(request.POST)
        if (form.is_valid):
            form.save()
    return redirect('index')

def signin(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('email')+request.POST.get('password')
        try:
            user=User.objects.get(email=email)
        except:
            messages.info(request,'User does not exist')
            return redirect('signin')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('signin')



    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('email')+request.POST.get('password')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('password2')

        user=User.objects.filter(email=email).exists()
        if user:
            messages.info(request,'User with this email already exists')
            return redirect('signup')


        if type(firstname)==str and type(lastname)==str:
            if password1==password2:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                user=authenticate(request,username=username,password=password1)
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Passwords do not match')
                return redirect('signup')
        else:
            messages.info(request,'Names must be only letters')
            return redirect('signup')

    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect('index')