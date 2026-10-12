
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    hasil = 1
    for i in range(1, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah bilangan 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                p = float(input("Panjang: "))
                l = float(input("Lebar: "))
                print("Luas persegi panjang:", luas_persegi_panjang(p, l))

            elif pilihan == "2":
                a = float(input("Alas: "))
                t = float(input("Tinggi: "))
                print("Luas segitiga:", luas_segitiga(a, t))

            elif pilihan == "3":
                n = int(input("Masukkan n: "))
                print("Jumlah 1 sampai", n, "=", jumlah_n(n))

            elif pilihan == "4":
                n = int(input("Masukkan n: "))
                print(n, "! =", faktorial(n))

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak tersedia.")

        except ValueError as error:
            print("Input tidak valid:", error)


if __name__ == "__main__":
    main()