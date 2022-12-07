from django.contrib.auth.models import User, auth
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from jshop_app.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def Shop(request):
    prodt = Product.objects.all().filter(available=True)
    ct = Category.objects.all()
    paginator = Paginator(prodt, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, "home.html", {'pr': prodt, 'ct': ct, 'pg': pro})


def shop(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, available=True)
    else:
        prodt = Product.objects.all().filter(available=True)
    cat = Category.objects.all()
    paginator = Paginator(prodt, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, "home.html", {'pr': prodt, 'ct': cat, 'pg': pro})


def Productdetails(request, c_slug, p_slug):
    try:
        prodt = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'detail.html', {'pr': prodt})


def Search(request):
    prod = None
    query = None
    cat = Category.objects.all()
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod, 'ct': cat})


def Signup(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        uname = request.POST['uname']
        passwd = request.POST['pwd']
        cpasswd = request.POST['cpwd']

        if passwd == cpasswd:
            if User.objects.filter(username=uname).exists():
                messages.Error(request, "username already exists")

            elif User.objects.filter(email=email).exists():
                messages.Error(request, "email already exists")

            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=passwd)
                user.set_password(passwd)
                user.save()
                return redirect('login')
        else:
            print("password doesnot match")
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['pwd']

        user = auth.authenticate(username=uname, password=passwd)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')

            else:
                messages.Info(request, "User is disabled.contact admin.")
        
        else:
            messages.Info(request, "invalid user")
            return redirect('login')
    else:
        return render(request, "login.html")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render('/')

def About(request):
    if request.user.is_authenticated:
        return render(request, "about.html")
    else:
        return render('/')
    


def logout(request):
    auth.logout(request)
    return redirect('login')
