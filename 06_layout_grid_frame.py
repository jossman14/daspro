"""06 - Layout: grid untuk formulir, pack untuk Frame."""
import tkinter as tk

jendela = tk.Tk()
jendela.title("grid dan Frame")
jendela.geometry("360x260")

# Frame atas memakai grid (formulir)
atas = tk.Frame(jendela, bg="#E6F2EC", padx=10, pady=10)
atas.pack(fill="x")
tk.Label(atas, text="Nama", bg="#E6F2EC").grid(row=0, column=0, sticky="w", pady=4)
tk.Entry(atas).grid(row=0, column=1, padx=10)
tk.Label(atas, text="NIM", bg="#E6F2EC").grid(row=1, column=0, sticky="w", pady=4)
tk.Entry(atas).grid(row=1, column=1, padx=10)
tk.Button(atas, text="Simpan").grid(row=2, column=0, columnspan=2, sticky="ew", pady=6)

# Frame bawah memakai pack (daftar)
bawah = tk.Frame(jendela, padx=10, pady=10)
bawah.pack(fill="both", expand=True)
tk.Label(bawah, text="Daftar mahasiswa:").pack(anchor="w")
tk.Listbox(bawah).pack(fill="both", expand=True)

jendela.mainloop()
