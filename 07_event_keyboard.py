"""07 - Event: tekan Enter untuk menghitung, Esc untuk menutup."""
import tkinter as tk


def hitung(event=None):              # event=None agar bisa dipanggil tombol juga
    try:
        c = float(entri.get())
        hasil.config(text=f"{c} °C = {c * 9 / 5 + 32:.1f} °F")
    except ValueError:
        hasil.config(text="Masukkan angka")


jendela = tk.Tk()
jendela.title("Event Keyboard")
jendela.geometry("320x170")

tk.Label(jendela, text="Suhu (°C), lalu tekan Enter").pack(pady=8)
entri = tk.Entry(jendela, font=("Arial", 12))
entri.pack()
entri.focus()
tk.Button(jendela, text="Konversi", command=hitung).pack(pady=8)
hasil = tk.Label(jendela, text="", font=("Arial", 13))
hasil.pack()

entri.bind("<Return>", hitung)                          # Enter = hitung
jendela.bind("<Escape>", lambda e: jendela.destroy())   # Esc = tutup
jendela.mainloop()
