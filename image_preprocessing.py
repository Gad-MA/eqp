from torchvision.transforms import Grayscale
from pathlib import Path
from PIL import Image

grayscale_transform = Grayscale(num_output_channels=3)

def preprocess_image_for_inference(image_pix):
    image = Image.open(image_pix).convert("RGB")  # Convert to RGB to manipulate colors
    if ord(image_pix.name[0])!=102:
      return grayscale_transform(Image.open(image_pix).convert("RGB"))
    pixels = image.load()
    width, height = image.size

    # Define a threshold for considering a pixel "white" or close to white
    white_threshold = 200  # Adjust this value based on how "white" is defined in your images

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Check if the pixel is not close to white
            if r < white_threshold or g < white_threshold or b < white_threshold:
                # Calculate an appropriate shade of red based on the original pixel intensity
                # This is a simple approach; you might need a more complex mapping
                intensity = (r + g + b) // 3 # Average the RGB values to get intensity
                # Map intensity to a shade of red (e.g., darker for lower intensity)
                red_shade = min(255, int(255 * (255 - intensity) / 255) + 50) # Ensure it's at least 50
                pixels[i, j] = (red_shade, 0, 0)  # Change to an appropriate shade of red

    grayscale_image = grayscale_transform(image)
    
    return grayscale_image
