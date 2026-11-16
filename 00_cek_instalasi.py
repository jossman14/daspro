"""00 - Cek apakah Python dan Tkinter sudah siap dipakai.
Jalankan: python 00_cek_instalasi.py"""
import sys
print("Versi Python :", sys.version.split()[0])
try:
    import tkinter as tk
    print("Tkinter      : OK, versi Tk", tk.TkVersion)
    jendela = tk.Tk()
    jendela.title("Tkinter siap!")
    tk.Label(jendela, text="Selamat, Tkinter berhasil terpasang!",
             font=("Arial", 14), padx=30, pady=30).pack()
    jendela.mainloop()
except ImportError:
    print("Tkinter BELUM terpasang. Lihat slide langkah instalasi.")
try:
    import customtkinter
    print("CustomTkinter: OK, versi", customtkinter.__version__)
except ImportError:
    print("CustomTkinter: belum ada  ->  pip install customtkinter")
