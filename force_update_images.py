import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecom_project.settings")
django.setup()

from products.models import Product

def force_update_products(image_rel_path):
    products = Product.objects.all()
    count = 0
    for product in products:
        try:
            print(f"Forcing update for product: {product.name}")
            product.image = image_rel_path
            product.save()
            count += 1
        except Exception as e:
            print(f"Error updating {product.name}: {e}")
    print(f"Force updated {count} products with placeholder image.")

if __name__ == "__main__":
    # Ensure placeholder exists (we assume setup_images.py created it)
    media_root = settings.MEDIA_ROOT
    placeholder_exists = os.path.exists(os.path.join(media_root, 'products', 'placeholder.png'))
    
    if placeholder_exists:
        image_rel = 'products/placeholder.png'
        force_update_products(image_rel)
    else:
        print("Placeholder image does not exist. Please run setup_images.py first or ensure the file is present.")
