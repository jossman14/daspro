"""03 - Entry: mengambil isian pengguna, menghitung kuadrat."""
import tkinter as tk


def proses():
    teks = entri.get()                    # isi Entry selalu berupa teks
    try:
        angka = float(teks)
        hasil.config(text=f"Kuadrat = {angka ** 2}", fg="darkgreen")
    except ValueError:
        hasil.config(text="Harus angka!", fg="red")
    entri.delete(0, tk.END)               # kosongkan kotak


jendela = tk.Tk()
jendela.title("Entry")
jendela.geometry("320x180")

tk.Label(jendela, text="Masukkan angka:", font=("Arial", 12)).pack(pady=5)
entri = tk.Entry(jendela, font=("Arial", 12), width=15)
entri.pack()
entri.focus()
tk.Button(jendela, text="Proses", command=proses).pack(pady=10)
hasil = tk.Label(jendela, text="", font=("Arial", 13))
hasil.pack()

jendela.mainloop()
