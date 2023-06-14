import tkinter as tk
from tkinter import messagebox
import tkinter.colorchooser as colorchooser
from PIL import ImageGrab

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=700, height=700)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = tk.Button(self.root, text="Tamamını Sil", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        self.erase_button = tk.Button(self.root, text="Silgi", command=self.use_eraser)
        self.erase_button.pack(side=tk.LEFT)

        self.color_button = tk.Button(self.root, text="Renk Değiştir", command=self.change_color)
        self.color_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.root, text="Fotoğrafı Kaydet", command=self.save_photo)
        self.save_button.pack(side=tk.LEFT)

        self.current_color = "black"
        self.eraser_mode = False

    def draw(self, event):
        x, y = event.x, event.y
        if self.eraser_mode:
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='white')
        else:
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.current_color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def use_eraser(self):
        self.eraser_mode = not self.eraser_mode

    def change_color(self):
        color = colorchooser.askcolor(title="Renk Seçin")
        if color[1] is not None:
            self.current_color = color[1]

    def save_photo(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        image = ImageGrab.grab((x, y, x1, y1))
        file_path = "drawing.png"  # Kaydedilecek dosya adı ve yolunu istediğiniz şekilde ayarlayabilirsiniz
        image.save(file_path)
        messagebox.showinfo("Başarılı", "Fotoğraf kaydedildi: {}".format(file_path))

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
