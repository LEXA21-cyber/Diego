# Format string

# Contoh Umum
nama = "ucup"
nama_tengah = "van"
nama_akhir = "java"
keturunan = 12

# String
sambung = nama + nama_tengah + nama_akhir + str(keturunan)
print(sambung)
sambung2 = f"{nama}{nama_tengah}{nama_akhir}{keturunan}"
print(sambung2)

##ANGKA
#angka biasa
angka = 2024.5
format_str = f"angkanya adalah {angka}"
print(format_str)

# Boolean
boolean = False
format_str = f"boleean nya adalah {boolean}"
print(format_str)

# Bilangan bulat
angka = 15
format_str= f"bilangan bulat = {angka:d}"
print(format_str)

#Bilangan ribuan
angka = 2000000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

# Bilangan decimal (koma di belakang nol)
angka = 2024.56789
format_str = f"desimalnya = {angka:.2f}"
# :.2f artinya 2 angka di belakang koma formatnya float
print(format_str)

# menampilkan bilangan leading zero
angka = 2024.56789
format_str = f"desimalnya = {angka:08.2f}"
print(format_str)

# Menampilkan tanda (+) dan (-)
angka_minus = -10
angka_plus = 10.5678
format_minus = f"minus = {angka_minus:-d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# Memformat persen
persentase = 0.045
format_persen = f"persen {persentase:.1%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam kurawal / placeholder
harga_basreng = 10000
jumlah = 5

itung_jajan = f"total bayar = {harga_basreng*jumlah:,} $"
print(itung_jajan)

# Format angka lain (binary, octal, hexadecimal)

angka = 255
format_binery = f"binernya adalah {bin(angka)}"# {bin(angka)} angka:b
format_octal = f"octalnya adalah {oct(angka)}" # oct(angka) angka:o
format_hexa = f"hexadicimalnya adalah {hex(angka)}" # hex(angka) angka:x
print(format_binery)
print(format_octal)
print(format_hexa)

# Masih banyak format untuk sting yg lain...
# bisa di cari di w3school dkk