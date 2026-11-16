"""01 - Program Tkinter pertama: jendela + satu label."""
import tkinter as tk          # 1. ambil pustaka

jendela = tk.Tk()             # 2. buat jendela utama
jendela.title("Halo Fisika")  #    judul jendela
jendela.geometry("320x150")   #    lebar x tinggi (piksel)

salam = tk.Label(jendela, text="Halo, mahasiswa Fisika!", font=("Arial", 14))
salam.pack(pady=40)           # 3. tempelkan ke jendela

jendela.mainloop()            # 4. jalankan dan tunggu aksi pengguna
