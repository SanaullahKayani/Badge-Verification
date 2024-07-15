from PIL import Image, ImageDraw
import numpy as np
import colorsys

def is_happy_color(r, g, b):
    """Check if the color is 'happy' based on its hue."""
    h, s, v = colorsys.rgb_to_hsv(r / 255., g / 255., b / 255.)
    # Define happy colors as those with bright and warm hues (yellow, orange, etc.)
    return (0.05 <= h <= 0.15 or 0.9 <= h <= 1) and v > 0.6

def is_within_circle(x, y, center, radius):
    """Check if a pixel is within the circle."""
    return (x - center) ** 2 + (y - center) ** 2 <= radius ** 2

def verify_badge(image_path):
    """Verify the badge image."""
    # Load the image
    img = Image.open(image_path).convert("RGBA")
    
    # Check size
    if img.size != (512, 512):
        return False, "Image size is not 512x512"
    
    # Prepare to check pixels
    pixels = np.array(img)
    width, height = img.size
    center = width // 2
    radius = width // 2
    
    # Check if only non-transparent pixels are within the circle
    for y in range(height):
        for x in range(width):
            pixel = pixels[y, x]
            if pixel[3] != 0:  # Non-transparent pixel
                if not is_within_circle(x, y, center, radius):
                    return False, "Non-transparent pixels found outside the circle"
                if not is_happy_color(pixel[0], pixel[1], pixel[2]):
                    return False, "Colors do not give a happy feeling"
    
    return True, "The badge is valid"

def convert_image_to_badge(image_path, output_path):
    """Convert any image to the specified badge format."""
    # Load the image
    img = Image.open(image_path).convert("RGBA")
    
    # Resize to 512x512
    img = img.resize((512, 512), Image.LANCZOS)
    
    # Create a new image with transparent background
    badge = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    
    # Create mask and draw circle
    mask = Image.new("L", (512, 512), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 512, 512), fill=255)
    
    # Apply the mask to make sure pixels outside the circle are transparent
    img.putalpha(mask)
    
    # Paste the circular image onto the transparent badge
    badge.paste(img, (0, 0), mask)
    badge.save(output_path)

# Example usage
input_image_path = "./woman.png"
output_image_path = "./output_woman.png"

# Convert image to badge
convert_image_to_badge(input_image_path, output_image_path)

# Verify the badge
is_valid, message = verify_badge(output_image_path)
print(message)
