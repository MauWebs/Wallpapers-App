import ctypes
import os
import tkinter as tk

from PIL import Image, ImageTk


class MyApp:

    def __init__(self, app):

        self.root = app
        app.title("Wallpaper Changer")

        self.img_folder = "C:\\Users"

        for i in range(1, 5):
            img_path = os.path.join(self.img_folder, f'img{i}.jpg')
            photo = ImageTk.PhotoImage(Image.open(img_path).resize((150, 150)))
            label = tk.Label(
                app, image=photo, compound=tk.BOTTOM, bg='#fff')
            label.photo = photo
            label.bind("<Button-1>", lambda event, i=i: self.on_image_click(i))

            row_num = (i - 1) // 3
            col_num = (i - 1) % 3

            label.grid(row=row_num, column=col_num, padx=10, pady=10)

    def on_image_click(self, image_number):
        img_path = os.path.join(self.img_folder, f'img{image_number}.jpg')

        if not ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3):
            print("Failed to change wallpaper")

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("525x180")
    my_app = MyApp(app)
    app.mainloop()