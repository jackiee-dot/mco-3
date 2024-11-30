from PIL import Image

# Load the uploaded logo image
image_path = '/mnt/data/BACHELOR OF TECHNOLOGY AND LIVELIHOOD EDUCATION-modified (1).png'
logo_image = Image.open(image_path)

# Resize the image to speed up processing and get the most common colors
small_image = logo_image.resize((100, 100))
colors = small_image.getcolors(10000)  # Count and list all colors in the image

# Sort colors by frequency (most used colors at the top)
sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)

# Extract the top 5 most dominant colors
dominant_colors = [color[1] for color in sorted_colors[:5]]
dominant_colors

# Refine the dominant colors to exclude transparency (e.g., (0, 0, 0, 0)) and pick the most relevant ones
# Manually include the visible colors from the logo: orange, white, and blue-purple

# Known logo colors for reference (approximations)
primary_colors = [
    (255, 127, 0),    # Orange
    (82, 88, 255),    # Blue-purple
    (255, 255, 255)   # White
]

# Convert colors to hex codes for web usage
def rgb_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

hex_colors = [rgb_to_hex(color) for color in primary_colors]
hex_colors
