import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.determine_alleles()

    def determine_alleles(self):
        # Menentukan alel berdasarkan golongan darah ayah
        if self.blood_type == "A":
            return ["A", "O"]
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid!")

    def pass_allele(self):
        # Memilih satu alel secara acak
        return random.choice(self.alleles)


class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.determine_alleles()

    def determine_alleles(self):
        # Menentukan alel berdasarkan golongan darah ibu
        if self.blood_type == "A":
            return ["A", "O"]
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid!")

    def pass_allele(self):
        # Memilih satu alel secara acak
        return random.choice(self.alleles)


class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.allele_from_father = self.father.pass_allele()
        self.allele_from_mother = self.mother.pass_allele()
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        # Menentukan golongan darah anak berdasarkan alel
        alleles = sorted([self.allele_from_father, self.allele_from_mother])
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"
        else:
            raise ValueError("Kombinasi alel tidak valid!")

    def __str__(self):
        return f"Anak menerima alel {self.allele_from_father} dari ayah dan {self.allele_from_mother} dari ibu. Golongan darah anak: {self.blood_type}"


def main():
    print("===== Program Kemungkinan Golongan Darah Anak =====")
    father_blood = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
    mother_blood = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()

    try:
        father = Father(father_blood)
        mother = Mother(mother_blood)
        child = Child(father, mother)
        print(child)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()