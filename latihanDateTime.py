# Date and time (latihan)

import datetime as tanggal_waktu
# cara buat ngambil waktu data waktu hari ini
hari_ini = tanggal_waktu.date.today()
print(F"hari ini adalah hari = {hari_ini:%A}")


# Cara buat bikin tanggal 
tanggal_custom = tanggal_waktu.date(2007,3,7)
print(f"tanggal trs adalah hari = {tanggal_custom:%A}")

# cara membuat inputan masukan tanggal
print("\nSilakan masukan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = tanggal_waktu.date(tahun,bulan,tanggal)
#print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"Anda lahir pada : {tanggal_lahir:%A}, {tanggal_lahir}")

# Hitung usia
print("\n")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_sisa_bulan = (umur_hari.days % 365)// 30
umur_sisa_hari = (umur_hari.days % 365) % 30
#print(f"umur anda adalah {umur_hari}")
print(f"umur anda adalah {umur_tahun} tahun, {umur_sisa_bulan} bulan, {umur_sisa_hari} hari")
