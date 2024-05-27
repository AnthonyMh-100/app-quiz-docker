from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.core.paginator import Paginator
from .forms import UserForm,RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product

# Create your views here.

def view_generate_pdf(request):
    
    del request.session['cart']
    
    return redirect('app:view_home')
    pass

def redirect_login(request):
    return redirect('app:view_login')

def view_cart(request):
    total = None
    carts = request.session.get('cart')
    if carts is not None:
        total = sum(item['total'] for item in carts.values())
    
    return render(request,'views/cart.html',{'carts':carts, 'total':total})

def view_del_cart(request,id):
    cart = request.session.get('cart')
    cart.pop(str(id), None)  
    request.session['cart'] = cart
    
    return redirect('app:view_cart')
    
def view_search_product(request):
    if request.method == 'POST':
        word = request.POST['search']
        products = Product.objects.filter(name__startswith=word)
        
        return render(request,'views/home.html',{'products':products})
        
    else:
        products = Product.objects.all()
        paginate = Paginator(products,4)
        page = request.GET.get('page',1)
        products_paginate = paginate.page(page)
        return render(request,'views/home.html',{'products':products_paginate})

def view_home(request):
    if request.method == 'POST':
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])
        
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        cart = request.session.get('cart', {})
        
        str_product_id = str(product_id)  
        
        if str_product_id in cart:
            cart[str_product_id]['quantity'] += quantity
            cart[str_product_id]['total'] += subtotal
        else:
            cart[str_product_id] = {
                "prod_id": product.id,
                "name": product.name,
                "imagen": product.imagen.url,
                "price": product.price,
                "quantity": quantity,
                "total": subtotal
            }
        
        request.session['cart'] = cart
        return redirect('app:view_cart')
    
    else:
        return redirect('app:view_search_product')
    

def view_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Éxito! Bienvenido a la plataforma')
            return redirect('app:view_home')
        else:
            return HttpResponse('Usuario no válido')
    else:
        form_user = UserForm()
    
    return render(request, 'auth/login.html', {'form': form_user})

def view_logout(request):
    logout(request)
    return redirect('app:view_login')

def view_register(request):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            data = register.cleaned_data
            user = User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
            login(request,user)
            return redirect('app:view_home')
        else:
            return HttpResponse('debe ser un formularoi valido')
    else:
        register = RegisterForm()
        return render(request,'auth/register.html',{'form':register})




