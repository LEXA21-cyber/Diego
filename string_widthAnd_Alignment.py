# String widht dan Alignment

# Data

data_nama= "ujang"
data_umur= 17
data_tinggi= 150.4
data_nomor_sepatu= 45

# string normal
print("===string 1===")
data_gabungan = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_nomor_sepatu}"
print(data_gabungan)

# string multiline
print("\n===string 2===")
data_gabungan = f"nama          = {data_nama}\nUmur          = {data_umur}\nTinggi        = {data_tinggi}\nUkuran sepatu = {data_nomor_sepatu}"
print(data_gabungan)

# String multiline pakai kutip X """..."""
print("\n===string 3===")
data_gabungan = f"""nama          = {data_nama}
Umur          = {data_umur}
Tinggi        = {data_tinggi}
Ukuran sepatu = {data_nomor_sepatu}
"""
print(data_gabungan)

# Mengatur lebar
print("\n===string 4===")
data_nama = "Ujang Jajang"
data_gabungan = f"""
nama          = {data_nama:>12}
Umur          = {data_umur:>12}
Tinggi        = {data_tinggi:>12}
Ukuran sepatu = {data_nomor_sepatu:>12}
"""
print(data_gabungan)
