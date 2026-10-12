
x = 10


def tampilkan_scope(x):
    print("Nilai x di dalam fungsi:", x)


if __name__ == "__main__":
    print("Nilai x global:", x)
    tampilkan_scope(20)
    print("Nilai x global setelah fungsi:", x)
