import tkinter as tk
import os
from PIL import Image, ImageTk 

def Kirby_Victory():
    win = tk.Tk()
    win.title("CONGRATULATIONS")
    win.geometry("1000x1000")
    win.configure(bg = "#FFB7C5")


    title = tk.Label(win, text = "AWESOME!, AMAZING!, GREAT!, COOL!", font =("Arial", 23, "bold"), bg = "#FFB7C5")

    title.pack(pady=20)

    try:
        route = os.path.dirname(__file__)
        margen = os.path.join(route, "Kirby Feliz.png")


        imagen = Image.open(margen)
        imagen = imagen.resize((700, 480))
        img = ImageTk.PhotoImage(imagen)

        panel = tk.Label(win, image=img, bg="#FFB7C5")
        panel.image = img
        panel.pack()

    except Exception as e:
           print(f"Error real: {e}")
           tk.Label(win, text="[Foto no encontrada]", bg="#FFB7C5").pack()


    
    btn = tk.Button(win, text="POYO", command=win.destroy, width=25, bg="Red", fg="White")
    
    btn.pack(pady=30)
    win.mainloop()

if __name__ == "__main__":
     Kirby_Victory()