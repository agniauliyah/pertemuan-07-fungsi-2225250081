
def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    total = 0
    for angka in range(1, n + 1):
        total += angka

    return total


if __name__ == "__main__":
    print("Jumlah 1 sampai 10:", jumlah_n(10))
    print("Jumlah 1 sampai 5:", jumlah_n(5))
    print("Jumlah 1 sampai 0:", jumlah_n(0))
