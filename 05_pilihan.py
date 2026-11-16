"""05 - Pilihan: Radiobutton, Combobox, Listbox, dan messagebox."""
import tkinter as tk
from tkinter import ttk, messagebox

jendela = tk.Tk()
jendela.title("Widget Pilihan")
jendela.geometry("340x330")

kelamin = tk.StringVar(value="L")
tk.Radiobutton(jendela, text="Laki-laki", variable=kelamin, value="L").pack()
tk.Radiobutton(jendela, text="Perempuan", variable=kelamin, value="P").pack()

matkul = tk.StringVar()
pilihan = ttk.Combobox(jendela, textvariable=matkul, state="readonly",
                       values=["Fisika Dasar", "Kalkulus", "Daspro"])
pilihan.current(0)
pilihan.pack(pady=8)

daftar = tk.Listbox(jendela, height=4)
for buah in ["Apel", "Jeruk", "Mangga", "Pisang"]:
    daftar.insert(tk.END, buah)
daftar.pack(pady=5)


def tampilkan():
    pilih = daftar.curselection()
    buah = daftar.get(pilih[0]) if pilih else "(belum dipilih)"
    messagebox.showinfo("Pilihanmu",
                        f"Kelamin: {kelamin.get()}\nMatkul: {matkul.get()}\nBuah: {buah}")


tk.Button(jendela, text="Tampilkan pilihan", command=tampilkan).pack(pady=8)
jendela.mainloop()
