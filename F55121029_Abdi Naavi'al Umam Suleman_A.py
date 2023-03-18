import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        master.title("Image Processor")

        self.image_frame = tk.Frame(master)
        self.image_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.controls_frame = tk.Frame(master)
        self.controls_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.original_image_label = tk.Label(self.image_frame)
        self.original_image_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.grayscale_image_label = tk.Label(self.image_frame)
        self.grayscale_image_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.binarized_image_label = tk.Label(self.image_frame)
        self.binarized_image_label.pack(side=tk.LEFT, padx=10, pady=10)

        correction_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5)
        correction_box.place(x=350, y=20, width=300, height=70)

        button_frame = tk.Frame(correction_box)
        button_frame.pack(side=tk.LEFT, padx=5)

        self.load_image_button = tk.Button(button_frame, text="Masukkan gambar", command=self.load_image)
        self.load_image_button.pack(side=tk.LEFT, padx=5)

        self.grayscale_button = tk.Button(button_frame, text="Grayscale", command=self.grayscale)
        self.grayscale_button.pack(side=tk.LEFT, padx=5)

        self.binarize_button = tk.Button(button_frame, text="Binarize", command=self.binarize)
        self.binarize_button.pack(side=tk.LEFT, padx=5)

        def show_creator():
            creator_label = tk.Label(root, text='Nama : Abdi Naavial Umam Suleman    NIM : F55121029    Kelas : A')
            creator_label.place(x=320, y=570)

        creator_box = tk.LabelFrame(root, text='Pembuat', padx=5, pady=5)
        creator_box.place(x=290, y=540, width=400, height=70)

        show_creator()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

        if file_path:
            self.image = Image.open(file_path)

            original_photo = ImageTk.PhotoImage(self.image)
            self.original_image_label.configure(image=original_photo)
            self.original_image_label.image = original_photo

    def grayscale(self):
        if not hasattr(self, 'image'):
            return

        grayscale_image = self.image.convert('L')

        grayscale_photo = ImageTk.PhotoImage(grayscale_image)
        self.grayscale_image_label.configure(image=grayscale_photo)
        self.grayscale_image_label.image = grayscale_photo

    def binarize(self):
        if not hasattr(self, 'image'):
            return

        grayscale_image = self.image.convert('L')

        grayscale_array = np.array(grayscale_image)

        binarized_array = np.where(grayscale_array > 128, 255, 0)

        binarized_image = Image.fromarray(binarized_array)

        binarized_photo = ImageTk.PhotoImage(binarized_image)
        self.binarized_image_label.configure(image=binarized_photo)
        self.binarized_image_label.image = binarized_photo

root = tk.Tk()
root.geometry('1400x1000')
image_processor = ImageProcessor(root)
root.mainloop()
