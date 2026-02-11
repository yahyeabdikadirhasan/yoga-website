import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django.setup()

from products.models import Product

def add_products():
    products = [
        {'name': 'iPhone 17', 'price': 1199.99, 'description': 'The latest iPhone 17 with revolutionary features.'},
        {'name': 'iPhone 16', 'price': 999.99, 'description': 'iPhone 16 with A18 Bionic chip.'},
        {'name': 'iPhone 15 Plus', 'price': 899.99, 'description': 'iPhone 15 Plus with dynamic island.'},
        {'name': 'AirPods Pro 2', 'price': 249.99, 'description': 'Active Noise Cancellation and Transparency mode.'},
    ]

    for p in products:
        obj, created = Product.objects.get_or_create(
            name=p['name'],
            defaults={
                'price': p['price'],
                'description': p['description']
            }
        )
        if created:
            print(f"Created {p['name']}")
        else:
            print(f"Found {p['name']}")

if __name__ == '__main__':
    add_products()
