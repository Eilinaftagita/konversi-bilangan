# Fungsi untuk mengonversi bilangan dari basis N ke desimal menggunakan algoritma yang diberikan
def convert_to_decimal_algorithm(number, base):
    """
    Mengonversi bilangan dari basis N ke sistem desimal sesuai dengan algoritma yang diberikan.
    
    Args:
        number (int/str): Bilangan yang ingin dikonversi.
        base (int): Basis dari bilangan tersebut.
    
    Returns:
        int: Bilangan dalam sistem desimal.
    """
    # Mengubah bilangan ke dalam bentuk string untuk memproses setiap digit
    number_str = str(number)
    
    # Tentukan jumlah panjang digit d
    d = len(number_str)
    
    # Inisialisasi array a[i] yang akan menampung setiap digit
    a = [int(digit) for digit in number_str]  # Membuat daftar a[i] yang berisi setiap digit bilangan
    
    # Inisialisasi hasil
    hasil = 0
    
    # Proses konversi sesuai dengan algoritma
    for i in range(d):
        hasil = a[i] + hasil * base
        
    return hasil

# Fungsi utama untuk menampilkan hasil konversi
def main():
    # Daftar bilangan dan basis yang akan dikonversi
    numbers_and_bases = [
        (11011, 2),   # Bilangan biner
        (3214, 5),    # Bilangan basis 5
        (678, 9)      # Bilangan basis 9
    ]

    # Lakukan konversi dan tampilkan hasilnya
    for number, base in numbers_and_bases:
        result = convert_to_decimal_algorithm(number, base)
        print(f"{number} (basis {base}) ke desimal: {result}")

# Jalankan program utama
if __name__ == "__main__":
    main()
