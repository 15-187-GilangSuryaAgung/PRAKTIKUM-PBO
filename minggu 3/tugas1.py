import math

class Kalkulator:
    def __init__(self, nilai):
        # Inisialisasi nilai
        self.nilai = float(nilai)

    # Overloading operator penjumlahan (+)
    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    # Overloading operator pengurangan (-)
    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)

    # Overloading operator perkalian (*)
    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)

    # Overloading operator pembagian (/)
    def __truediv__(self, other):
        if other.nilai == 0:
            raise ValueError("Pembagian oleh nol tidak diperbolehkan!")
        return Kalkulator(self.nilai / other.nilai)

    # Overloading operator pangkat (^)
    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)

    # Fungsi logaritma basis 10
    def log(self):
        if self.nilai <= 0:
            raise ValueError("Logaritma hanya didefinisikan untuk bilangan positif!")
        return Kalkulator(math.log10(self.nilai))

    # Representasi string dari objek
    def __str__(self):
        return str(self.nilai)


def tampilkan_menu():
    print("\n===== Kalkulator Sederhana =====")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (^)")
    print("6. Logaritma (log)")
    print("7. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-7): ").strip()

        if pilihan == "7":
            print("Terima kasih telah menggunakan kalkulator ini!")
            break

        try:
            if pilihan == "6":  # Logaritma
                nilai = float(input("Masukkan nilai: "))
                kalkulator = Kalkulator(nilai)
                hasil = kalkulator.log()
                print(f"Log({nilai}) = {hasil}")
            elif pilihan in ["1", "2", "3", "4", "5"]:  # Operasi biner
                angka1 = float(input("Masukkan bilangan pertama: "))
                angka2 = float(input("Masukkan bilangan kedua: "))

                kalkulator1 = Kalkulator(angka1)
                kalkulator2 = Kalkulator(angka2)

                if pilihan == "1":
                    hasil = kalkulator1 + kalkulator2
                    print(f"{angka1} + {angka2} = {hasil}")
                elif pilihan == "2":
                    hasil = kalkulator1 - kalkulator2
                    print(f"{angka1} - {angka2} = {hasil}")
                elif pilihan == "3":
                    hasil = kalkulator1 * kalkulator2
                    print(f"{angka1} * {angka2} = {hasil}")
                elif pilihan == "4":
                    hasil = kalkulator1 / kalkulator2
                    print(f"{angka1} / {angka2} = {hasil}")
                elif pilihan == "5":
                    hasil = kalkulator1 ** kalkulator2
                    print(f"{angka1} ^ {angka2} = {hasil}")
            else:
                print("Pilihan tidak valid! Silakan coba lagi.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    main()
 
