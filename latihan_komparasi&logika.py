# Latihan Komparasi dan Logika

# membuat gabungan area rentang dari angka

# ++++++3------10++++++

inputUser = float(input('masukan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10 :'))
# Periksa angka kurang dari 3 atau tidak
IyaKurangDari = (inputUser < 3)
print('kurang dari 3 =',IyaKurangDari)

#Periksa angka lebih dari 10 atau tidak
IyaLebihDari = (inputUser > 10)
print('lebih dari 10 =',IyaLebihDari)

# Periksa hasilnya benar atau tidak
IyaBener = IyaKurangDari or IyaLebihDari
print('angka yang kamu masukan :',IyaBener)

print("\n =====AND=======")
# ------3++++++10------
inputUser = float(input('masukan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10 :'))
# Periksa angka kurang dari 10 atau tidak
IyaKurangDari = (inputUser < 10)
print('kurang dari 10 =',IyaKurangDari)

#Periksa angka lebih dari 3 atau tidak
IyaLebihDari = (inputUser > 3)
print('lebih dari 3 =',IyaLebihDari)

# Periksa hasilnya benar atau tidak
Benarkah = IyaKurangDari and IyaLebihDari
print('angka yang kamu masukan :',Benarkah)


print("========")
# ----0+++++5----8+++++11-----
inputUser = float(input('masukan angka yang bernilai \nlebih dari 0 \ndan \nkurang dari 5 \natau \nlebih dari 8 \nkurang dari 11 :'))
# Periksa angka kurang dari 10 atau tidak
IyaKurangDari = (inputUser < 5 and 11)
print('kurang dari 10 =',IyaKurangDari)

#Periksa angka lebih dari 3 atau tidak
IyaLebihDari = (inputUser > 0 and 8)
print('lebih dari 3 =',IyaLebihDari)

# Periksa hasilnya benar atau tidak
Benarkah = IyaKurangDari or IyaLebihDari
print('angka yang kamu masukan :',Benarkah)