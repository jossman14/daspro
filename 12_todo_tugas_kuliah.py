"""
12 - Daftar Tugas Kuliah (To-Do List) dengan tkinter + ttk
Fitur: tambah, tandai selesai, hapus, simpan & baca otomatis dari file JSON.
Widget: Entry, Combobox, Button, Treeview (tabel), Scrollbar, messagebox.
"""
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

NAMA_FILE = "tugas.json"


# ---------- bagian DATA (tanpa tampilan) ----------
def baca_data():
    if not os.path.exists(NAMA_FILE):
        return []
    with open(NAMA_FILE, encoding="utf-8") as f:
        return json.load(f)


def simpan_data():
    with open(NAMA_FILE, "w", encoding="utf-8") as f:
        json.dump(daftar_tugas, f, indent=2, ensure_ascii=False)


# ---------- bagian TAMPILAN ----------
def muat_ulang_tabel():
    tabel.delete(*tabel.get_children())          # kosongkan tabel
    for i, t in enumerate(daftar_tugas):
        status = "Selesai" if t["selesai"] else "Belum"
        tabel.insert("", "end", iid=str(i),
                     values=(t["matkul"], t["judul"], t["deadline"], status),
                     tags=("selesai",) if t["selesai"] else ())
    label_info.config(text=f"{sum(not t['selesai'] for t in daftar_tugas)} tugas belum selesai")


def tambah():
    judul = var_judul.get().strip()
    deadline = var_deadline.get().strip()
    if not judul or not deadline:
        messagebox.showwarning("Belum lengkap", "Judul dan deadline wajib diisi")
        return
    daftar_tugas.append({"matkul": var_matkul.get(), "judul": judul,
                         "deadline": deadline, "selesai": False})
    simpan_data()
    muat_ulang_tabel()
    var_judul.set("")
    var_deadline.set("")


def indeks_terpilih():
    pilih = tabel.selection()
    if not pilih:
        messagebox.showinfo("Pilih dulu", "Klik salah satu baris tugas")
        return None
    return int(pilih[0])


def tandai_selesai():
    i = indeks_terpilih()
    if i is not None:
        daftar_tugas[i]["selesai"] = not daftar_tugas[i]["selesai"]
        simpan_data()
        muat_ulang_tabel()


def hapus():
    i = indeks_terpilih()
    if i is not None and messagebox.askyesno("Hapus", f"Hapus '{daftar_tugas[i]['judul']}'?"):
        daftar_tugas.pop(i)
        simpan_data()
        muat_ulang_tabel()


# ---------- MEMBANGUN JENDELA ----------
daftar_tugas = baca_data()

root = tk.Tk()
root.title("Daftar Tugas Kuliah")
root.geometry("820x460")

gaya = ttk.Style()
gaya.theme_use("clam")
gaya.configure("Treeview", rowheight=28, font=("Segoe UI", 11))
gaya.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"),
               background="#0B5D3B", foreground="white")
gaya.configure("TButton", font=("Segoe UI", 11), padding=6)

# Frame atas: form input
form = ttk.LabelFrame(root, text=" Tugas baru ", padding=10)
form.pack(fill="x", padx=12, pady=10)

var_matkul = tk.StringVar(value="Daspro")
var_judul = tk.StringVar()
var_deadline = tk.StringVar()

ttk.Label(form, text="Mata kuliah").grid(row=0, column=0, sticky="w")
ttk.Combobox(form, textvariable=var_matkul, state="readonly", width=12,
             values=["Daspro", "Fisika Dasar", "Kalkulus", "Kimia Dasar"]).grid(row=1, column=0, padx=4)
ttk.Label(form, text="Judul tugas").grid(row=0, column=1, sticky="w")
ttk.Entry(form, textvariable=var_judul, width=30).grid(row=1, column=1, padx=4)
ttk.Label(form, text="Deadline (dd-mm-yyyy)").grid(row=0, column=2, sticky="w")
ttk.Entry(form, textvariable=var_deadline, width=16).grid(row=1, column=2, padx=4)
ttk.Button(form, text="+ Tambah", command=tambah).grid(row=1, column=3, padx=4)

# Frame tengah: tabel + scrollbar
tengah = ttk.Frame(root)
tengah.pack(fill="both", expand=True, padx=12)
kolom = ("matkul", "judul", "deadline", "status")
tabel = ttk.Treeview(tengah, columns=kolom, show="headings", selectmode="browse")
for k, lebar in zip(kolom, (120, 300, 130, 90)):
    tabel.heading(k, text=k.capitalize())
    tabel.column(k, width=lebar)
tabel.tag_configure("selesai", foreground="#8A8A8A")
gulir = ttk.Scrollbar(tengah, orient="vertical", command=tabel.yview)
tabel.configure(yscrollcommand=gulir.set)
tabel.pack(side="left", fill="both", expand=True)
gulir.pack(side="right", fill="y")

# Frame bawah: tombol aksi
bawah = ttk.Frame(root, padding=10)
bawah.pack(fill="x")
label_info = ttk.Label(bawah, text="")
label_info.pack(side="left")
ttk.Button(bawah, text="Hapus", command=hapus).pack(side="right", padx=4)
ttk.Button(bawah, text="Tandai selesai", command=tandai_selesai).pack(side="right", padx=4)

muat_ulang_tabel()
root.mainloop()
