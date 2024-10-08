from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.models import Seller, Products, Payment, Details

@login_required(login_url='userlogin')
def seller_list(request):
    data = Seller.objects.all()
    return render(request,'admin/seller_list.html',{'seller':data})

@login_required(login_url='userlogin')
def admin_product_view(request):
    data = Products.objects.all()
    return render(request,'admin/admin_product_view.html',{'admin_product_view':data})


@login_required(login_url='userlogin')
def admin_orders(request):
    data = Payment.objects.all()
    return render(request,'admin/admin_orders.html',{'admin_orders':data})