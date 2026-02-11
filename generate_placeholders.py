import os
import django
from PIL import Image, ImageDraw, ImageFont

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django.setup()

from django.conf import settings
from products.models import Product

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def create_placeholder(filename, text, start_color, end_color):
    # Ensure directory exists
    media_root = settings.MEDIA_ROOT
    products_dir = os.path.join(media_root, 'products')
    os.makedirs(products_dir, exist_ok=True)
    
    filepath = os.path.join(products_dir, filename)
    
    # Create gradient image
    img = create_gradient(800, 800, start_color, end_color)
    d = ImageDraw.Draw(img)
    
    # Add text
    try:
        # Try to load a font, otherwise use default
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
        
    # Calculate text size using textbbox (for Pillow >= 8.0.0)
    try:
        left, top, right, bottom = d.textbbox((0, 0), text, font=font)
        text_width = right - left
        text_height = bottom - top
    except AttributeError:
        # Fallback for older Pillow versions
        text_width, text_height = d.textsize(text, font=font)

    position = ((800 - text_width) / 2, (800 - text_height) / 2)
    
    # Draw text in white with shadow
    shadow_offset = 2
    d.text((position[0] + shadow_offset, position[1] + shadow_offset), text, fill=(0, 0, 0), font=font)
    d.text(position, text, fill=(255, 255, 255), font=font)
    
    img.save(filepath)
    print(f"Created {filename}")
    return f"products/{filename}"

def update_products():
    products_to_update = [
        {'name': 'iPhone 17', 'start_color': '#2c3e50', 'end_color': '#4ca1af', 'filename': 'iphone_17.png', 'text': 'iPhone 17'},
        {'name': 'iPhone 16', 'start_color': '#00c6ff', 'end_color': '#0072ff', 'filename': 'iphone_16.png', 'text': 'iPhone 16'},
        {'name': 'iPhone 15 Plus', 'start_color': '#ff9a9e', 'end_color': '#fecfef', 'filename': 'iphone_15_plus.png', 'text': 'iPhone 15 Plus'},
        {'name': 'AirPods Pro 2', 'start_color': '#e0eafc', 'end_color': '#cfdef3', 'filename': 'airpods_pro_2.png', 'text': 'AirPods Pro 2'},
        
        # New Tech Products
        {'name': 'MacBook Pro 14 M3', 'start_color': '#bdc3c7', 'end_color': '#2c3e50', 'filename': 'macbook_pro_m3.png', 'text': 'MacBook Pro M3'},
        {'name': 'iPad Pro 13-inch', 'start_color': '#cac531', 'end_color': '#f3f9a7', 'filename': 'ipad_pro_13.png', 'text': 'iPad Pro 13"'},
        {'name': 'Dell XPS 15', 'start_color': '#eacda3', 'end_color': '#d6ae7b', 'filename': 'dell_xps_15.png', 'text': 'Dell XPS 15'},
        {'name': 'Samsung Galaxy S24 Ultra', 'start_color': '#8e9eab', 'end_color': '#eef2f3', 'filename': 's24_ultra.png', 'text': 'S24 Ultra'},
        {'name': 'Google Pixel 8 Pro', 'start_color': '#cc2b5e', 'end_color': '#753a88', 'filename': 'pixel_8_pro.png', 'text': 'Pixel 8 Pro'},
        {'name': 'Sony WH-1000XM5', 'start_color': '#232526', 'end_color': '#414345', 'filename': 'sony_xm5.png', 'text': 'Sony XM5'},
        {'name': 'Sonos Era 300', 'start_color': '#000000', 'end_color': '#434343', 'filename': 'sonos_era.png', 'text': 'Sonos Era 300'},
        {'name': 'PlayStation 5 Slim', 'start_color': '#2980b9', 'end_color': '#6dd5fa', 'filename': 'ps5_slim.png', 'text': 'PS5 Slim'},
        {'name': 'Xbox Series X', 'start_color': '#11998e', 'end_color': '#38ef7d', 'filename': 'xbox_series_x.png', 'text': 'Xbox Series X'},
        {'name': 'Nintendo Switch OLED', 'start_color': '#ff416c', 'end_color': '#ff4b2b', 'filename': 'switch_oled.png', 'text': 'Switch OLED'},
        {'name': 'Apple Watch Series 9', 'start_color': '#fc4a1a', 'end_color': '#f7b733', 'filename': 'apple_watch_9.png', 'text': 'Watch Series 9'},
        {'name': 'Samsung Galaxy Watch 6', 'start_color': '#1f4037', 'end_color': '#99f2c8', 'filename': 'galaxy_watch_6.png', 'text': 'Galaxy Watch 6'},
        {'name': 'Garmin Fenix 7', 'start_color': '#3a1c71', 'end_color': '#d76d77', 'filename': 'garmin_fenix_7.png', 'text': 'Garmin Fenix 7'},
        {'name': 'GoPro Hero 12 Black', 'start_color': '#000000', 'end_color': '#0f9b0f', 'filename': 'gopro_12.png', 'text': 'GoPro 12'},
        {'name': 'DJI Mini 4 Pro', 'start_color': '#d3cce3', 'end_color': '#e9e4f0', 'filename': 'dji_mini_4.png', 'text': 'DJI Mini 4'},
        {'name': 'Logitech MX Master 3S', 'start_color': '#4b6cb7', 'end_color': '#182848', 'filename': 'mx_master_3s.png', 'text': 'MX Master 3S'},
        {'name': 'Keychron Q1 Pro', 'start_color': '#0f2027', 'end_color': '#203a43', 'filename': 'keychron_q1.png', 'text': 'Keychron Q1'},
        {'name': 'Kindle Paperwhite', 'start_color': '#ffafbd', 'end_color': '#ffc3a0', 'filename': 'kindle_paperwhite.png', 'text': 'Kindle'},
        
        # Additional 10 Products
        {'name': 'Meta Quest 3', 'start_color': '#ECE9E6', 'end_color': '#FFFFFF', 'filename': 'meta_quest_3.png', 'text': 'Meta Quest 3'},
        {'name': 'Apple Vision Pro', 'start_color': '#8e9eab', 'end_color': '#eef2f3', 'filename': 'vision_pro.png', 'text': 'Vision Pro'},
        {'name': 'Philips Hue Starter Kit', 'start_color': '#ff00cc', 'end_color': '#333399', 'filename': 'hue_starter.png', 'text': 'Philips Hue'},
        {'name': 'Dyson V15 Detect', 'start_color': '#f12711', 'end_color': '#f5af19', 'filename': 'dyson_v15.png', 'text': 'Dyson V15'},
        {'name': 'NVIDIA GeForce RTX 4090', 'start_color': '#76b852', 'end_color': '#8DC26F', 'filename': 'rtx_4090.png', 'text': 'RTX 4090'},
        {'name': 'Steam Deck OLED', 'start_color': '#000046', 'end_color': '#1CB5E0', 'filename': 'steam_deck.png', 'text': 'Steam Deck'},
        {'name': 'Bose QuietComfort Ultra', 'start_color': '#141E30', 'end_color': '#243B55', 'filename': 'bose_qc_ultra.png', 'text': 'Bose QC Ultra'},
        {'name': 'ASUS ROG Zephyrus G14', 'start_color': '#20002c', 'end_color': '#cbb4d4', 'filename': 'rog_zephyrus.png', 'text': 'ROG Zephyrus'},
        {'name': 'Samsung Galaxy Tab S9 Ultra', 'start_color': '#1c92d2', 'end_color': '#f2fcfe', 'filename': 'tab_s9_ultra.png', 'text': 'Tab S9 Ultra'},
        {'name': 'Fujifilm X100VI', 'start_color': '#232526', 'end_color': '#414345', 'filename': 'fuji_x100vi.png', 'text': 'Fujifilm X100VI'},
    ]

    for p_data in products_to_update:
        try:
            product = Product.objects.get(name=p_data['name'])
            image_path = create_placeholder(p_data['filename'], p_data['text'], p_data['start_color'], p_data['end_color'])
            product.image = image_path
            product.save()
            print(f"Updated {product.name} with {image_path}")
        except Product.DoesNotExist:
            print(f"Product {p_data['name']} not found")

if __name__ == '__main__':
    update_products()
