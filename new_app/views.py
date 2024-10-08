from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def homepage(request):
    return render(request,'index.html')


# def userpage(request):
#     return render(request,'index2.html')


def profilelogin(request):
    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            if user.is_customer:
                return redirect('cust_product_view')
            if user.is_seller:
                return redirect('sellerpage')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

@login_required(login_url='userlogin')
def adminpage(request):
    return render(request,'admin/adminpage.html')

@login_required(login_url='userlogin')
def sellerpage(request):
    return render(request,'seller/sellerpage.html')


@login_required(login_url='userlogin')
def customerpage(request):
    return render(request,'customer/customerpage.html')


