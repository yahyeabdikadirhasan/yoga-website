import os
import django
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.core.files import File

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecom_project.settings")
django.setup()

from products.models import Product

def create_placeholder():
    # Ensure media directory exists
    media_root = settings.MEDIA_ROOT
    products_dir = os.path.join(media_root, 'products')
    os.makedirs(products_dir, exist_ok=True)
    
    image_path = os.path.join(products_dir, 'placeholder.png')
    
    # Create a simple image using Pillow
    img = Image.new('RGB', (600, 400), color='#f0f0f0')
    d = ImageDraw.Draw(img)
    
    # Draw some text or shapes (optional, just a colored block is fine too)
    # We'll just make a simple border
    d.rectangle([10, 10, 590, 390], outline='#d0d0d0', width=5)
    
    img.save(image_path)
    print(f"Created placeholder image at {image_path}")
    return 'products/placeholder.png'

def update_products(image_rel_path):
    products = Product.objects.all()
    count = 0
    for product in products:
        if not product.image:
            print(f"Updating product: {product.name}")
            product.image = image_rel_path
            product.save()
            count += 1
        else:
             print(f"Skipping {product.name}, already has image")
    print(f"Updated {count} products with placeholder image.")

if __name__ == "__main__":
    try:
        image_rel = create_placeholder()
        update_products(image_rel)
    except Exception as e:
        print(f"Error: {e}")
        # Fallback if PIL is somehow broken, though Django needs it.
