from abc import ABC, abstractmethod  # Untuk abstraksi

# Custom exception untuk error tertentu
class InvalidAgeError(Exception):
    pass

class EmptyNameError(Exception):
    pass

# Kelas abstrak Animal sebagai dasar semua hewan
class Animal(ABC):
    def __init__(self, name, age):
        if not name.strip():  # Cek jika nama kosong
            raise EmptyNameError("Error: Nama hewan tidak boleh kosong.")
        if not isinstance(age, (int, float)) or age < 0:  # Cek usia valid
            raise InvalidAgeError("Error: Usia harus angka positif.")
        
        # Enkapsulasi: atribut privat dengan underscore
        self._name = name
        self._age = age

    # Metode getter untuk akses data
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Metode abstrak yang harus diimplementasikan oleh kelas turunan
    @abstractmethod
    def make_sound(self):
        pass

    # Metode tambahan (opsional) untuk contoh perilaku lain
    def info(self):
        return f"{self._name} (Usia: {self._age} tahun)"

# Kelas turunan untuk Anjing
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"  # Polimorfisme: suara anjing

    def fetch(self):  # Perilaku khusus anjing
        return f"{self._name} sedang mengambil bola!"

# Kelas turunan untuk Kucing
class Cat(Animal):
    def make_sound(self):
        return "Meow!"  # Polimorfisme: suara kucing

    def scratch(self):  # Perilaku khusus kucing
        return f"{self._name} sedang mencakar!"

# Kelas Zoo untuk mengelola hewan
class Zoo:
    def __init__(self):
        self.animals = []  # Daftar hewan

    def add_animal(self, animal):
        try:
            self.animals.append(animal)
            print(f"{animal.get_name()} berhasil ditambahkan ke kebun binatang!")
        except Exception as e:
            print(f"Gagal menambahkan hewan: {e}")

    def show_all_sounds(self):
        if not self.animals:
            print("Belum ada hewan di kebun binatang.")
        else:
            print("\nSuara Hewan di Kebun Binatang:")
            for animal in self.animals:
                print(f"- {animal.get_name()}: {animal.make_sound()}")

    def show_all_info(self):
        if not self.animals:
            print("Belum ada hewan di kebun binatang.")
        else:
            print("\nDaftar Hewan di Kebun Binatang:")
            for animal in self.animals:
                print(f"- {animal.info()}")

# Program utama
def main():
    zoo = Zoo()

    # Contoh penggunaan dengan error handling
    try:
        # Tambah hewan valid
        dog = Dog("Rex", 3)
        cat = Cat("Mimi", 2)
        
        zoo.add_animal(dog)
        zoo.add_animal(cat)

        # Tampilkan suara dan info
        zoo.show_all_sounds()
        zoo.show_all_info()

        # Contoh perilaku khusus
        print(f"\nPerilaku Khusus:")
        print(dog.fetch())
        print(cat.scratch())

        # Contoh error: nama kosong
        invalid_animal = Dog("", 5)
        zoo.add_animal(invalid_animal)  # Ini tidak akan tercapai karena error

    except EmptyNameError as e:
        print(e)
    except InvalidAgeError as e:
        print(e)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan program
if __name__ == "__main__":
    main()