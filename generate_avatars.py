"""
Generate simple avatar images for PyChat
Creates 6 colorful avatar images with emoji faces
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_avatar(size, bg_color, emoji, filename):
    """Create a simple avatar image with background color and emoji"""
    # Create a new image with the specified background color
    img = Image.new('RGBA', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw a circle
    draw.ellipse([0, 0, size, size], fill=bg_color)
    
    # Try to use a system font for the emoji
    try:
        # For Windows, try to use Segoe UI Emoji
        font = ImageFont.truetype("seguiemj.ttf", size//2)
    except:
        try:
            # Fallback to Arial
            font = ImageFont.truetype("arial.ttf", size//2)
        except:
            # Use default font if no TrueType fonts available
            font = ImageFont.load_default()
    
    # Get text size and position it in center
    bbox = draw.textbbox((0, 0), emoji, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw the emoji
    draw.text((x, y), emoji, font=font, fill='white')
    
    # Save the image
    img.save(filename, 'PNG')
    print(f"Created {filename}")

def main():
    """Generate all avatar images"""
    avatars_dir = "static/images"
    os.makedirs(avatars_dir, exist_ok=True)
    
    # Avatar configurations (color, emoji)
    avatars = [
        ((102, 126, 234), "😊", "avatar1.png"),  # Blue gradient
        ((240, 147, 251), "😎", "avatar2.png"),  # Pink gradient  
        ((79, 172, 254), "🤓", "avatar3.png"),   # Light blue
        ((67, 233, 123), "😄", "avatar4.png"),   # Green
        ((250, 112, 154), "🙂", "avatar5.png"),  # Pink
        ((168, 237, 234), "😍", "avatar6.png"),  # Teal
    ]
    
    size = 100  # Avatar size in pixels
    
    for bg_color, emoji, filename in avatars:
        filepath = os.path.join(avatars_dir, filename)
        create_avatar(size, bg_color, emoji, filepath)
    
    print("All avatars created successfully!")

if __name__ == "__main__":
    main()
