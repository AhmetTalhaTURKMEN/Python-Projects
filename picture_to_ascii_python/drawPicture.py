import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

def draw_and_save_image(file_path, save_file_name):
    with open(file_path, 'rb') as image_file:
        image_data = image_file.read()

    width = 100  # Output width (number of characters)
    height = 50  # Output height (number of characters)

    image = Image.open(BytesIO(image_data))
    image = image.resize((width, height))
    image = image.convert('L')  # Grayscale image

    ascii_characters = '@%#*+=-:. '  # Characters sorted by intensity

    ascii_image = ''

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            intensity = pixel // 32  # Divides 256 color levels by 8
            ascii_image += ascii_characters[intensity]
        ascii_image += '\n'

    save_directory = 'txt-file'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    save_file_path = os.path.join(save_directory, save_file_name)
    with open(save_file_path, 'w') as save_file:
        save_file.write(ascii_image)

    print("ASCII text saved to file: " + save_file_path)

def create_ascii_png(ascii_text, save_file_name):
    character_width = 8  # Width of each character (in pixels)
    character_height = 12  # Height of each character (in pixels)
    spacing = 10  # Spacing between characters (in pixels)

    lines = ascii_text.strip().split('\n')
    width = (len(lines[0]) * (character_width + spacing)) - spacing
    height = (len(lines) * (character_height + spacing)) - spacing

    image = Image.new('RGB', (width, height), color='white')
    font = ImageFont.truetype('arial.ttf', 12)
    draw = ImageDraw.Draw(image)

    y = 0
    for line in lines:
        x = 0
        for character in line:
            draw.text((x, y), character, font=font, fill='black')
            x += character_width + spacing
        y += character_height + spacing

    save_directory = 'png-file'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    new_save_file_name = os.path.splitext(save_file_name)[0] + ' ascii.png'
    new_save_file_path = os.path.join(save_directory, new_save_file_name)
    image.save(new_save_file_path)
    print("PNG file saved: " + new_save_file_path)


def select_image():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    if file_name:
        file_extension = os.path.splitext(file_name)[1].lower()
        allowed_extensions = ['.jpeg', '.png', '.jpg']
        if file_extension in allowed_extensions:
            file_path = file_name
            save_file_name = os.path.splitext(os.path.basename(file_name))[0] + '.txt'
            draw_and_save_image(file_path, save_file_name)
            ascii_text = open(os.path.join('txt-file', save_file_name)).read()
            create_ascii_png(ascii_text, save_file_name)

# Create the main window
root = tk.Tk()
root.title("ASCII Image Converter")

# Image selection button
image_select_button = tk.Button(root, text="Select Image", command=select_image)
image_select_button.pack(pady=20)


# Start app
root.mainloop()