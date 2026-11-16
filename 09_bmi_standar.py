"""
09 - Kalkulator BMI (Body Mass Index / Indeks Massa Tubuh)
Versi DESAIN STANDAR: hanya memakai widget bawaan tkinter.
Rumus: BMI = berat (kg) / tinggi (m)^2
"""
import tkinter as tk
from tkinter import messagebox


def hitung_bmi():
    try:
        berat = float(entry_berat.get())
        tinggi_cm = float(entry_tinggi.get())
        if berat <= 0 or tinggi_cm <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input salah", "Berat dan tinggi harus angka lebih dari 0")
        return

    bmi = berat / (tinggi_cm / 100) ** 2
    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi < 25:
        kategori = "Normal"
    elif bmi < 30:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    label_hasil.config(text=f"BMI = {bmi:.1f}  ({kategori})")


def reset():
    entry_berat.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    label_hasil.config(text="Hasil akan muncul di sini")


jendela = tk.Tk()
jendela.title("Kalkulator BMI - Standar")
jendela.geometry("360x220")

tk.Label(jendela, text="Berat (kg)").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_berat = tk.Entry(jendela)
entry_berat.grid(row=0, column=1, padx=10, pady=10)

tk.Label(jendela, text="Tinggi (cm)").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tinggi = tk.Entry(jendela)
entry_tinggi.grid(row=1, column=1, padx=10, pady=10)

tk.Button(jendela, text="Hitung", command=hitung_bmi).grid(row=2, column=0, pady=10)
tk.Button(jendela, text="Reset", command=reset).grid(row=2, column=1, pady=10)

label_hasil = tk.Label(jendela, text="Hasil akan muncul di sini")
label_hasil.grid(row=3, column=0, columnspan=2, pady=10)

jendela.mainloop()
