import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django.setup()

from products.models import Product

def add_more_products():
    products = [
        # VR & AR
        {'name': 'Meta Quest 3', 'price': 499.99, 'description': 'Breakthrough mixed reality. Powerful performance.'},
        {'name': 'Apple Vision Pro', 'price': 3499.00, 'description': 'Welcome to the era of spatial computing.'},
        
        # Smart Home
        {'name': 'Philips Hue Starter Kit', 'price': 199.99, 'description': 'White and Color Ambiance smart light bulbs.'},
        {'name': 'Dyson V15 Detect', 'price': 749.99, 'description': 'Laser reveals microscopic dust. Powerful cleaning.'},
        
        # Gaming Components
        {'name': 'NVIDIA GeForce RTX 4090', 'price': 1599.00, 'description': 'The ultimate GeForce GPU. Beyond fast.'},
        {'name': 'Steam Deck OLED', 'price': 549.00, 'description': 'High dynamic range screen, longer battery life.'},
        
        # Audio
        {'name': 'Bose QuietComfort Ultra', 'price': 429.00, 'description': 'World-class noise cancellation, quieter than ever.'},
        
        # Computing
        {'name': 'ASUS ROG Zephyrus G14', 'price': 1599.99, 'description': 'World\'s most powerful 14-inch gaming laptop.'},
        {'name': 'Samsung Galaxy Tab S9 Ultra', 'price': 1199.99, 'description': 'The new standard for premium tablets.'},
        
        # Photography
        {'name': 'Fujifilm X100VI', 'price': 1599.00, 'description': 'The one and only compact digital camera.'},
    ]

    print(f"Adding {len(products)} additional products...")
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
    add_more_products()
