import os
from PIL import Image, ImageOps

# Configuration
MAX_SIZE = 1920  # Max width or height (whichever is larger)
QUALITY = 85  # JPEG/WebP quality (1-100)

def optimize_image(image_path):
    """ Optimize image by correcting orientation, resizing, and converting to WebP format """
    with Image.open(image_path) as img:
        img = ImageOps.exif_transpose(img)  # Fix image rotation based on EXIF
        is_png = image_path.lower().endswith(".png")
        img_format = "WEBP"

        # Resize if width or height exceeds MAX_SIZE
        width, height = img.size
        if width > MAX_SIZE or height > MAX_SIZE:
            scale = MAX_SIZE / max(width, height)  # Scale by the larger dimension
            new_size = (int(width * scale), int(height * scale))
            img = img.resize(new_size, Image.LANCZOS)
            print(f"Resized: {image_path} → {new_size}")

        # Save as WebP (lossless for PNG, quality setting for others)
        new_path = os.path.splitext(image_path)[0] + ".webp"
        if is_png:
            img.save(new_path, img_format, lossless=True)  # Preserve transparency for PNG
        else:
            img = img.convert("RGB")  # Convert non-PNG images to RGB
            img.save(new_path, img_format, quality=QUALITY)

        print(f"Optimized: {image_path} → {new_path}")

def process_images(folder):
    """ Recursively find and optimize all images in a folder (including subfolders) """
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(('png', 'jpg', 'jpeg')):
                image_path = os.path.join(root, filename)
                optimize_image(image_path)

if __name__ == "__main__":
    input_folder = "."  # Change this to your folder
    process_images(input_folder)
    print("All images optimized successfully!")
