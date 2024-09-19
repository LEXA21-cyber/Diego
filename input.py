# Belajar Input 

Data1 =input("Masukan angka :")#apapun yang di input langsung tanpa di casting, type datanya pasti string
print("angka yang di input adalah",Data1)

print('angka data dari inputan tadi sebenernya bertype ', type(Data1))

#harus di casting dulu menjadi angka
Data1 = int(input("Masukan angka :"))
print("angka yang di input adalah",Data1)

print('angka data dari inputan tadi sebenernya bertype ', type(Data1))