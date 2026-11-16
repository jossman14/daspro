"""02 - Label dan Button: tombol mengubah teks label."""
import tkinter as tk

jumlah_klik = 0


def sapa():
    global jumlah_klik
    jumlah_klik += 1
    label.config(text=f"Tombol sudah diklik {jumlah_klik} kali")


jendela = tk.Tk()
jendela.title("Label dan Button")
jendela.geometry("340x160")

label = tk.Label(jendela, text="Belum diklik", font=("Arial", 14), fg="darkgreen")
label.pack(pady=20)

tombol = tk.Button(jendela, text="Klik saya", font=("Arial", 12), command=sapa)
tombol.pack()

jendela.mainloop()
