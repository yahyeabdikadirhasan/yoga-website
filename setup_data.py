import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecom_project.settings")
django.setup()

from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print('Superuser created')
else:
    print('Superuser already exists')

if not Product.objects.exists():
    Product.objects.create(name='Laptop', price=999.99, description='A high-performance laptop')
    Product.objects.create(name='Smartphone', price=499.99, description='A latest generation smartphone')
    Product.objects.create(name='Headphones', price=199.99, description='Noise-cancelling headphones')
    Product.objects.create(name='Smart Watch', price=299.99, description='Fitness tracker and smart watch')
    Product.objects.create(name='Tablet', price=599.99, description='10-inch screen tablet')
    Product.objects.create(name='Gaming Console', price=499.99, description='Next-gen gaming console')
    Product.objects.create(name='Wireless Earbuds', price=129.99, description='True wireless earbuds')
    Product.objects.create(name='4K Monitor', price=349.99, description='27-inch 4K UHD monitor')
    Product.objects.create(name='Mechanical Keyboard', price=89.99, description='RGB mechanical keyboard')
    Product.objects.create(name='Gaming Mouse', price=59.99, description='High DPI gaming mouse')
    print('Products created')
else:
    print('Products already exist')
