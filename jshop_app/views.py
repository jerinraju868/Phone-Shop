from django.contrib.auth.models import User, auth
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from jshop_app.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def Shop(request):
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
        email = request.POST['email']
        uname = request.POST['uname']
        passwd = request.POST['passwd']
        cpasswd = request.POST['cpasswd']
        if passwd == cpasswd:
            if User.objects.filter(username=uname).exists():
                messages.Info(request, "username already exists")
                return render(request, 'signuperror.html')
            elif User.objects.filter(email=email).exists():
                messages.Info(request, "email already exists")
                return render(request, 'signuperror.html')
            else:
                user = User.objects.create_user(first_name=fname, email=email, username=uname, password=passwd)
                user.save()
                return redirect('/')
        else:
            print("password doesnot match")
            return render(request, 'signuperror.html')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['passwd']
        user = auth.authenticate(username=uname, password=passwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.Info("invalid user")
            return redirect('/')
    else:
        return render(request, "login.html")


def About(request):
    return render(request, "about.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
