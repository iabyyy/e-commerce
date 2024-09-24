from django.shortcuts import render, redirect

from new_app.customer_views import customer_reg
from new_app.forms import LoginForm, SellerForm, ProductForm
from new_app.models import Seller, Products, Customer, Payment, Details


def seller_reg(request):
    form1 = LoginForm()
    form2 = SellerForm()
    if request.method =='POST':
        form1 = LoginForm(request.POST)
        form2 = SellerForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_seller = True
            user1.save()
            user2 = form2.save(commit=False)
            user2.User = user1
            user2.save()
            return redirect('login')
    return render(request,'seller/seller_reg.html',{'form1':form1,'form2':form2})



def seller_profile(request):
    u=request.user
    data = Seller.objects.filter(User=u)


def add_product(request ):
    u = request.user
    data = Seller.objects.get(User=u)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.seller = data
            obj.save()
            return redirect('product_view')
    return render(request,'seller/productpage.html',{'product':form})



def product_view(request):
    u = request.user
    data = Seller.objects.get(User=u)
    print(data)
    form = Products.objects.filter(seller=data)
    print(form)
    return render(request,'seller/product_view.html',{'product_view':form})


def product_delete(request,id):
    data = Products.objects.get(id=id)
    data.delete()
    return redirect('product_view')


def product_update(request,id):
    data = Products.objects.get(id=id)
    form = ProductForm(instance=data)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('product_view')
    return render(request,'seller/product_update.html',{'product_update':form})


def seller_orders(request):
    data = Payment.objects.all()
    return render(request,'seller/seller_orders.html',{'seller_orders':data})








