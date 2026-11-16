"""
08 - Tur widget dasar tkinter dalam satu jendela.
Jalankan untuk melihat bentuk tiap widget.
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tur Widget Tkinter")
root.geometry("420x430")

tk.Label(root, text="Label: teks biasa", font=("Arial", 12)).pack(pady=4)
tk.Entry(root, width=30).pack(pady=4)
tk.Button(root, text="Button: tombol", command=lambda: print("diklik!")).pack(pady=4)

pilih = tk.StringVar(value="L")
bingkai = tk.Frame(root)
bingkai.pack(pady=4)
tk.Radiobutton(bingkai, text="Laki-laki", variable=pilih, value="L").pack(side="left")
tk.Radiobutton(bingkai, text="Perempuan", variable=pilih, value="P").pack(side="left")

tk.Checkbutton(root, text="Checkbutton: saya setuju").pack(pady=4)
ttk.Combobox(root, values=["Fisika", "Kimia", "Biologi"], state="readonly").pack(pady=4)
tk.Scale(root, from_=0, to=100, orient="horizontal", label="Scale: nilai").pack(pady=4)
lb = tk.Listbox(root, height=3)
for item in ["Listbox baris 1", "Listbox baris 2", "Listbox baris 3"]:
    lb.insert("end", item)
lb.pack(pady=4)
tk.Text(root, height=3, width=35).pack(pady=4)

root.mainloop()
