from django.shortcuts import render, redirect, get_object_or_404
from jshop_app.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def Cartdetails(request, to=0, count=0, cart_items=None):
    if request.user.is_authenticated:

        ct_item = None
        try:
            ct = Cartlist.objects.get(cart_id=Cart_id(request))
            ct_item = Items.objects.filter(cart=ct, active=True)
            for i in ct_item:
                to += (i.prodt.price*i.quantity)
                count += i.quantity
        except ObjectDoesNotExist:
            pass
        return render(request, "cart.html", {'ci': ct_item, 'to': to, 'cn': count})
    else:
        return redirect('login')


def Cart_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def Add_items(request, product_id):
    prod = Product.objects.get(id=product_id)
    try:
        ct = Cartlist.objects.get(cart_id=Cart_id(request))

    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=Cart_id(request))
        ct.save()
    try:
        c_items = Items.objects.get(prodt=prod, cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(prodt=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartdetails')


def Delete_items(request, product_id):
    ct = Cartlist.objects.get(cart_id=Cart_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def Remove(request, product_id):
    ct = Cartlist.objects.get(cart_id=Cart_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetails')

def placeorder(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            address = request.POST['address']
            landmark = request.POST['landmark']
            state = request.POST['state']
            pincode = request.POST['pincode']
            ptm = request.POST['ptm']

            user = Address.objects.create(name=name, mobile=mobile, email=email, address=address, landmark=landmark, state=state, pincode=pincode, paymentmethod=ptm)
            user.save()
            return redirect('home')
        return render(request, 'place_order.html')
    else:
        return redirect('login')