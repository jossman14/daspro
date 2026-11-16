"""
10 - Kalkulator BMI
Versi DESAIN RAPI: memakai ttk (themed tkinter), Frame, padding, font, dan warna.
Tidak perlu install apa pun (ttk sudah bawaan Python).
"""
import tkinter as tk
from tkinter import ttk, messagebox

WARNA_LATAR = "#F4F7F5"
WARNA_UTAMA = "#0B5D3B"
FONT = ("Segoe UI", 12)


def hitung_bmi():
    try:
        berat = float(var_berat.get())
        tinggi = float(var_tinggi.get()) / 100
        if berat <= 0 or tinggi <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input salah", "Isi berat dan tinggi dengan angka > 0")
        return
    bmi = berat / tinggi ** 2
    kategori = ("Kurus" if bmi < 18.5 else "Normal" if bmi < 25
                else "Gemuk" if bmi < 30 else "Obesitas")
    var_hasil.set(f"{bmi:.1f}")
    var_kategori.set(kategori)


jendela = tk.Tk()
jendela.title("Kalkulator BMI - ttk")
jendela.geometry("380x330")
jendela.configure(bg=WARNA_LATAR)

gaya = ttk.Style()
gaya.theme_use("clam")                       # tema bawaan yang lebih modern
gaya.configure("TFrame", background=WARNA_LATAR)
gaya.configure("TLabel", background=WARNA_LATAR, font=FONT)
gaya.configure("Judul.TLabel", font=("Segoe UI", 18, "bold"), foreground=WARNA_UTAMA)
gaya.configure("Hasil.TLabel", font=("Segoe UI", 28, "bold"), foreground=WARNA_UTAMA)
gaya.configure("TButton", font=FONT, padding=8)
gaya.configure("Utama.TButton", background=WARNA_UTAMA, foreground="white")
gaya.map("Utama.TButton", background=[("active", "#127A50")])

var_berat, var_tinggi = tk.StringVar(), tk.StringVar()
var_hasil, var_kategori = tk.StringVar(value="-"), tk.StringVar(value="")

bingkai = ttk.Frame(jendela, padding=20)
bingkai.pack(fill="both", expand=True)

ttk.Label(bingkai, text="Kalkulator BMI", style="Judul.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 15))
ttk.Label(bingkai, text="Berat (kg)").grid(row=1, column=0, sticky="w", pady=5)
ttk.Entry(bingkai, textvariable=var_berat, font=FONT, width=15).grid(row=1, column=1, pady=5)
ttk.Label(bingkai, text="Tinggi (cm)").grid(row=2, column=0, sticky="w", pady=5)
ttk.Entry(bingkai, textvariable=var_tinggi, font=FONT, width=15).grid(row=2, column=1, pady=5)
ttk.Button(bingkai, text="Hitung BMI", style="Utama.TButton",
           command=hitung_bmi).grid(row=3, column=0, columnspan=2, sticky="ew", pady=15)
ttk.Label(bingkai, textvariable=var_hasil, style="Hasil.TLabel").grid(row=4, column=0, columnspan=2)
ttk.Label(bingkai, textvariable=var_kategori).grid(row=5, column=0, columnspan=2)

jendela.mainloop()
