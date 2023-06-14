from PIL import Image

# Resmi yükleyin
image_path = "source-png/resim.jpeg"  # Çizmek istediğiniz resmin dosya yolu
image = Image.open(image_path)

# Resmi boyutlandırın
width, height = image.size
aspect_ratio = height / width / 2
new_width = 200
new_height = int(new_width * aspect_ratio)
image = image.resize((new_width, new_height))

# Resmi çizin
pixels = image.load()
for y in range(new_height):
    for x in range(new_width):
        r, g, b = pixels[x, y][:3]
        average_brightness = (r + g + b) // 3
        if average_brightness < 128:
            print("█", end="")
        else:
            print("░", end="")
    print()