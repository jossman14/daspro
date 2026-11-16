"""04 - Variabel Tkinter: StringVar dan BooleanVar terikat ke widget."""
import tkinter as tk
from tkinter import messagebox

jendela = tk.Tk()
jendela.title("Variabel Tkinter")
jendela.geometry("320x220")

nama = tk.StringVar()
setuju = tk.BooleanVar(value=False)

tk.Label(jendela, text="Nama:").pack(pady=(15, 0))
tk.Entry(jendela, textvariable=nama).pack()
tk.Label(jendela, text="Pratinjau:").pack(pady=(10, 0))
tk.Label(jendela, textvariable=nama, fg="blue").pack()   # ikut berubah otomatis
tk.Checkbutton(jendela, text="Saya setuju", variable=setuju).pack(pady=5)


def kirim():
    if not setuju.get():
        messagebox.showwarning("Ups", "Centang persetujuan dulu")
    else:
        messagebox.showinfo("Terkirim", f"Halo, {nama.get()}!")


tk.Button(jendela, text="Kirim", command=kirim).pack()
jendela.mainloop()
