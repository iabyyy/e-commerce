from itertools import product

from django.contrib import messages
from django.shortcuts import redirect, render

from new_app.forms import LoginForm, CustomerForm, ProductForm, CartItemForm, PaymentForm, DetailsForm
from new_app.models import Customer, Products, CartItem, Payment, Details


def customer_reg(request):
    form1 = LoginForm()
    form2 = CustomerForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = CustomerForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_customer = True
            user1.save()
            user2 = form2.save(commit=False)
            user2.User = user1
            user2.save()
            return redirect('login')
    return render(request,'customer/customer_reg.html',{'form1':form1,'form2':form2})


def customer_profile(request):
    u=request.user
    print(u)
    data = Customer.objects.filter(User=u)
    print(data)

def cust_product_view(request):
    data = Products.objects.all()
    return render(request,'customer/cust_product_view.html',{'cust_product_view':data})




def add_to_cart(request,id):
    user = Customer.objects.get(User=request.user)
    print(user)
    data = Products.objects.get(id=id)
    print(data)
    cart_item = CartItem.objects.filter(product=data,User=user)
    print(cart_item)
    if cart_item.exists():
        messages.info(request,'already added')
        # return redirect('view_cart')
    else:
        obj = CartItem()
        obj.User = user
        obj.product = data
        obj.save()
        return redirect('view_cart')
    return redirect('view_cart')




def view_cart(request):
    data = CartItem.objects.all()
    return render(request,'customer/cart.html',{'customer_cart':data})

def remove_from_cart(request,id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('view_cart')


def customer_details(request,id):
    data = CartItem.objects.get(id=id)
    print(data)
    form = DetailsForm()
    if request.method =='POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.cart = data
            obj.save()
            return redirect('customer_payment',id = obj.id)
    return render(request,'customer/customer_details.html',{'customer_details':form})


def customer_payment(request,id):
    details = Details.objects.get(id=id)
    product =  details.cart.product
    print(product)
    qty = details.cart.product.quantity
    print(qty)
    qnty = details.quantity
    print(qnty)
    total_price = (details.cart.product.price * details.quantity)
    print(total_price)
    form=PaymentForm()
    if request.method =='POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.details = details
            obj.save()
            details.status = 1
            details.save()
            qty= int(qty-qnty)
            product.quantity = qty
            product.save()
            return redirect('customer_orders')
    return render(request,'customer/payment.html',{'customer_payment':form,'total_price':total_price})



def customer_orders(request):
    data = Payment.objects.all()
    return render(request,'customer/customer_orders.html',{'customer_orders':data})


def cancel_order(request,id):
    data = Payment.objects.get(id=id)
    print(data)
    product = data.details.cart.product
    print(product)
    qty = data.details.cart.product.quantity
    print(qty)
    qnty = data.details.quantity
    print(qnty)
    qty = int(qty + qnty)
    product.quantity = qty
    product.save()
    data.delete()
    return redirect('customer_orders')



