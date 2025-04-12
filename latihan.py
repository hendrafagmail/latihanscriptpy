def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def main():
    print("Selamat datang di kalkulator sederhana!")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    print(f"Hasil penjumlahan: {tambah(angka1, angka2)}")
    print(f"Hasil pengurangan: {kurang(angka1, angka2)}")

if __name__ == "__main__":
    main()
