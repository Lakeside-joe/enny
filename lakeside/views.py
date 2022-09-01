from multiprocessing import context
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from lakeside.models import *
from dashboard.models import *
from cart.models import *
from lakeside.forms import SignupForm
from dashboard.forms import ProfileUpdateForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    specials = Style.objects.filter(special=True)
    slide1 = Inner.objects.get(pk=1)
    slide2 = Inner.objects.get(pk=4)
    slide3 = Inner.objects.get(pk=5)
    
    
    context = {
        'categories':categories,
        'specials':specials,
        'slide1':slide1,  
        'slide2':slide2,  
        'slide3':slide3,   
    }
    return render(request, 'index.html', context)
def contact(request):
    return render(request, 'contact.html')

def all_food(request):
    categories = Category.objects.all()
    all_meals = Style.objects.all()
    
    context = {
        'all_meals':all_meals,
        'categories':categories,
    }
    return render(request, 'all_food.html', context)
def categories(request):
    categories = Category.objects.all()
    specials = Style.objects.filter(special=True)
    
    context = {
        'categories':categories,
        'specials':specials,
    }
    return render(request, 'categories.html', context)
def showcase(request):
    return render(request, 'showcase.html')
def specials(request):
    return render(request, 'specials.html')
def single_category(request, id):
    categories = Category.objects.all()
    single_category = Style.objects.filter(category_id=id)
    specials = Style.objects.filter(special=True)
    cat_title = Category.objects.get(pk=id)
    
    context = {
        'categories':categories,
        'category':single_category,
        'specials':specials,
        'cat_title':cat_title,
    }
    return render(request, 'category.html', context) 

@login_required(login_url='signin')
def profile(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    
    context = {
        'profile_data':profile_data
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='signin')
def profileupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile update is successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profileupdate')
        
    context = {
            'form':form,
            'profile_data':profile_data,
        }
    return render(request, 'profileupdate.html', context)

def detail(request, id):
    categories = Category.objects.all()
    specials = Style.objects.filter(special=True)
    detail = Style.objects.get(pk=id)
    
    context = {
        'categories':categories,
        'specials':specials,
        'detail':detail,
    }
    return render(request, 'detail.html', context)
def signout(request):
    logout(request)
    messages.success(request, 'You have signed out successfully')
    return redirect('signin')

def signin(request):
    if request.method == "POST":
        myusername = request.POST['username']
        mypassword = request.POST['password']
        user = authenticate(request, username=myusername, password=mypassword)
        if user:
            login(request, user)
            messages.success(request, f'Dear {user.username}, your signin is successful, welcome!')
            return redirect('index')
        else:
            messages.warning(request, 'Username/Password is incorrect')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        form = SignupForm(request.POST)
        if form.is_valid():
            userform = form.save()
            newuser = Profile(user = userform)
            newuser.first_name = userform.first_name
            newuser.last_name = userform.last_name
            newuser.email = userform.email
            newuser.phone = phone
            newuser.save()
            messages.success(request, 'Signup is successful!')
            login(request, userform)
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')

@login_required(login_url='signin')
def passwordupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('passwordupdate')
    
    context = {
        'profile_data':profile_data,
        'form':form,
    }
    return render(request, 'profilepassword.html', context)

def ordermeal(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    cart_no = profile_data.id
    if request.method == 'POST':
        quantityselected = int(request.POST['mealquantity'])
        meal = request.POST['mealid']
        mealselected = Style.objects.get(pk=meal)
        cart = Shopcart.objects.filter(user__username=request.user.username, paid=False)
        if cart:
            basket = Shopcart.objects.filter(style=mealselected.id, user__username= request.user).first()
            if basket:
                basket.quantity += quantityselected
                basket.save()
                messages.success(request, 'Your order is being processed')
                return redirect('all_food')
            else:
                neworder = Shopcart()
                neworder.user = request.user
                neworder.style = mealselected
                neworder.c_name = mealselected.name
                neworder.quantity = quantityselected
                neworder.c_price = mealselected.price
                neworder.amount = mealselected.price * quantityselected
                neworder.cart_code = cart_no
                neworder.paid = False
                neworder.save()
                messages.success(request, 'Your meal is being processed')
                return redirect('all_food')       
        else:
            newitem = Shopcart()
            newitem.user = request.user
            newitem.style = mealselected
            newitem.c_name = mealselected.name
            newitem.quantity = quantityselected
            newitem.c_price = mealselected.price
            newitem.amount = mealselected.price * quantityselected
            newitem.cart_code = cart_no
            newitem.paid = False
            newitem.save()
            messages.success(request, 'Your meal is being processed')
    return redirect('all_food')

def shopcart(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = Shopcart.objects.filter(user__username=request.user.username, paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in cart:
        subtotal += item.c_price * item.quantity
        
    vat = 0.075 * subtotal
    total = vat + subtotal
    context = {
        'profile':profile,
        'cart':cart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
 
    return render(request, 'shopcart.html', context) 

def increase(request):
    if request.method=='POST':
        qty_item = request.POST['quant_id']
        newqty = int(request.POST['quantity'])
        new_qty = Shopcart.objects.get(pk=qty_item)
        new_qty.quantity = newqty
        new_qty.amount = new_qty.c_price * new_qty.quantity
        new_qty.save()
        messages.success(request, 'Quantity updated')
        return redirect('shopcart')
         
def delete(request):
    if request.method == 'POST':
        remove = request.POST['del_id']
        Shopcart.objects.filter(pk=remove).delete()
        messages.success(request, 'one item deleted')
        return redirect('shopcart')
    
def checkout(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = Shopcart.objects.filter(user__username=request.user.username, paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in cart:
        subtotal += item.c_price * item.quantity
        
    vat = 0.075 * subtotal
    total = vat + subtotal
    context = {
        'profile':profile,
        'cart':cart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
    return render(request, 'checkout.html', context)