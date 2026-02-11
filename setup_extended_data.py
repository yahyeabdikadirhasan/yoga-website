import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django.setup()

from products.models import Product

def add_extended_products():
    products = [
        # Laptops & Tablets
        {'name': 'MacBook Pro 14 M3', 'price': 1599.99, 'description': 'The most advanced Mac laptop ever.'},
        {'name': 'iPad Pro 13-inch', 'price': 1299.99, 'description': 'The ultimate iPad experience with M4 chip.'},
        {'name': 'Dell XPS 15', 'price': 1499.00, 'description': 'High-performance laptop with 4K OLED display.'},
        
        # Smartphones (Android)
        {'name': 'Samsung Galaxy S24 Ultra', 'price': 1299.99, 'description': 'Galaxy AI is here. Epic titanium design.'},
        {'name': 'Google Pixel 8 Pro', 'price': 999.00, 'description': 'The all-pro phone engineered by Google.'},
        
        # Audio
        {'name': 'Sony WH-1000XM5', 'price': 348.00, 'description': 'Industry-leading noise canceling headphones.'},
        {'name': 'Sonos Era 300', 'price': 449.00, 'description': 'Next-level audio that hits from every direction.'},
        
        # Gaming
        {'name': 'PlayStation 5 Slim', 'price': 499.99, 'description': 'Play Has No Limits. Breathtaking immersion.'},
        {'name': 'Xbox Series X', 'price': 499.99, 'description': 'The fastest, most powerful Xbox ever.'},
        {'name': 'Nintendo Switch OLED', 'price': 349.99, 'description': '7-inch OLED screen for vivid handheld gaming.'},
        
        # Wearables
        {'name': 'Apple Watch Series 9', 'price': 399.00, 'description': 'Smarter. Brighter. Mightier. Double tap magic.'},
        {'name': 'Samsung Galaxy Watch 6', 'price': 299.99, 'description': 'Unlock your best self with personalized health insights.'},
        {'name': 'Garmin Fenix 7', 'price': 649.99, 'description': 'The ultimate multisport GPS watch.'},
        
        # Cameras & Drones
        {'name': 'GoPro Hero 12 Black', 'price': 399.99, 'description': 'Incredible image quality + even better HyperSmooth.'},
        {'name': 'DJI Mini 4 Pro', 'price': 759.00, 'description': 'Mini to the Max. 4K/60fps HDR video.'},
        
        # Accessories
        {'name': 'Logitech MX Master 3S', 'price': 99.99, 'description': 'An icon remastered. Quiet clicks and 8K DPI.'},
        {'name': 'Keychron Q1 Pro', 'price': 199.00, 'description': 'Wireless custom mechanical keyboard.'},
        {'name': 'Kindle Paperwhite', 'price': 149.99, 'description': 'Now with a 6.8" display and warmer light.'},
    ]

    print(f"Adding {len(products)} products...")
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
    add_extended_products()
