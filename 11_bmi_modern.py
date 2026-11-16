"""
11 - Kalkulator BMI
Versi DESAIN MODERN: memakai CustomTkinter (sudut membulat, mode gelap/terang).
Install dulu:  pip install customtkinter
"""
import customtkinter as ctk

ctk.set_appearance_mode("light")         # "light", "dark", atau "system"
ctk.set_default_color_theme("green")     # "blue", "green", "dark-blue"


class AplikasiBMI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator BMI - Modern")
        self.geometry("400x470")

        kartu = ctk.CTkFrame(self, corner_radius=20)
        kartu.pack(padx=25, pady=25, fill="both", expand=True)

        ctk.CTkLabel(kartu, text="Kalkulator BMI",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(25, 15))

        self.berat = ctk.CTkEntry(kartu, placeholder_text="Berat (kg)",
                                  height=42, corner_radius=12, font=ctk.CTkFont(size=15))
        self.berat.pack(padx=30, pady=8, fill="x")
        self.tinggi = ctk.CTkEntry(kartu, placeholder_text="Tinggi (cm)",
                                   height=42, corner_radius=12, font=ctk.CTkFont(size=15))
        self.tinggi.pack(padx=30, pady=8, fill="x")

        ctk.CTkButton(kartu, text="Hitung", height=44, corner_radius=12,
                      font=ctk.CTkFont(size=16, weight="bold"),
                      command=self.hitung).pack(padx=30, pady=15, fill="x")

        self.hasil = ctk.CTkLabel(kartu, text="–", font=ctk.CTkFont(size=40, weight="bold"))
        self.hasil.pack()
        self.kategori = ctk.CTkLabel(kartu, text="Masukkan data lalu tekan Hitung",
                                     font=ctk.CTkFont(size=14))
        self.kategori.pack(pady=(0, 10))

        self.saklar = ctk.CTkSwitch(kartu, text="Mode gelap", command=self.ganti_mode)
        self.saklar.pack(pady=10)

    def hitung(self):
        try:
            b = float(self.berat.get())
            t = float(self.tinggi.get()) / 100
            bmi = b / t ** 2
        except (ValueError, ZeroDivisionError):
            self.kategori.configure(text="Input harus angka > 0", text_color="#D64545")
            return
        kategori, warna = (("Kurus", "#E0A800") if bmi < 18.5 else
                           ("Normal", "#2E9E5B") if bmi < 25 else
                           ("Gemuk", "#E07B00") if bmi < 30 else ("Obesitas", "#D64545"))
        self.hasil.configure(text=f"{bmi:.1f}", text_color=warna)
        self.kategori.configure(text=kategori, text_color=warna)

    def ganti_mode(self):
        ctk.set_appearance_mode("dark" if self.saklar.get() else "light")


if __name__ == "__main__":
    AplikasiBMI().mainloop()
