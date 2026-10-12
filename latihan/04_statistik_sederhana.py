
def statistik(data):
    if not data:
        raise ValueError("Data tidak boleh kosong")

    nilai_min = min(data)
    nilai_max = max(data)
    rata_rata = sum(data) / len(data)

    return nilai_min, nilai_max, rata_rata


if __name__ == "__main__":
    data = [80, 90, 75, 85, 95]

    minimum, maksimum, rata_rata = statistik(data)

    print("Data:", data)
    print("Nilai minimum:", minimum)
    print("Nilai maksimum:", maksimum)
    print("Rata-rata:", rata_rata)