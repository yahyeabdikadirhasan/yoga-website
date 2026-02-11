from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Product, Order
from .forms import UserRegistrationForm, ProductForm, CustomAuthenticationForm

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def create_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        Order.objects.create(
            customer=request.user,
            product=product
        )
        return render(request, 'order_confirmation.html', {'product': product})
    return redirect('product_detail', pk=pk)

def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    cart.append(pk)
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    # Calculate quantities and total price
    cart_items = []
    total_price = 0
    for product in products:
        quantity = cart.count(product.pk)
        total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })
        total_price += total
    
    # Remove duplicates from cart_items for display
    # This logic is slightly flawed as it iterates query set which is unique, so cart.count is correct.
    # However, filtering products by pk__in returns unique products. 
    # So we loop through Unique Products and count their occurrences in the session list.
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, pk):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item != pk]
    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('product_list')
    
    products = Product.objects.filter(pk__in=cart)
    for product in products:
        quantity = cart.count(product.pk)
        total_price = product.price * quantity
        Order.objects.create(
            customer=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price,
            status='Pending'
        )
    
    request.session['cart'] = []
    return render(request, 'order_confirmation.html', {'message': "Your order has been placed successfully!"})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def customer_dashboard(request):
    orders = Order.objects.filter(customer=request.user).order_by('-date_ordered')
    return render(request, 'customer_dashboard.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-date_ordered')[:10]  # Get recent 10 orders
    return render(request, 'admin_dashboard.html', {'products': products, 'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'title': 'Add Product'})

@user_passes_test(lambda u: u.is_staff)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'title': 'Edit Product'})

@user_passes_test(lambda u: u.is_staff)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    return render(request, 'product_confirm_delete.html', {'product': product})
