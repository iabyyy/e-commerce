from django.shortcuts import render, redirect

from new_app.models import Seller, Products, Payment, Details


def seller_list(request):
    data = Seller.objects.all()
    return render(request,'admin/seller_list.html',{'seller':data})

def seller_delete(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('seller_list')


def admin_product_view(request):
    data = Products.objects.all()
    return render(request,'admin/admin_product_view.html',{'admin_product_view':data})



def admin_orders(request):
    data = Payment.objects.all()
    return render(request,'admin/admin_orders.html',{'admin_orders':data})