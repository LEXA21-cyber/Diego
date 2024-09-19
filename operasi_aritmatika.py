# Operator aritmatika dasar python

a = 10
b = 3

# 1.operator penjumlahan (+)
hasil = a+b
print("hasil dari ",a,"+",b, "adalah",hasil)

# 2.operator pengurangan (-)
hasil = a-b
print("hasil dari ",a,"-",b, "adalah",hasil)

# 3.operator perkalian (*)
hasil = a*b
print("hasil dari ",a,"x",b, "adalah",hasil)

# 4.operator pembagian (/)
hasil = a/b
print("hasil dari ",a,":",b, "adalah",hasil)

# 5.operator Eksponen (pangkat) (**)
hasil = a**b
print("hasil dari ",a,"pangkat",b, "adalah",hasil)

# 5.operator Modulus (%)
hasil = a%b
print("hasil dari ",a,"mod",b, "adalah",hasil)

# 5.operator Floor division (//)
hasil = a//b
print("hasil dari ",a,"//",b, "adalah",hasil)

print("==========")
# Prioritas Operator / Operational Precedence
'''
    1. tanda kurung ()
    2. Exponen **
    3. Perkalian dan teman teman (* / % //)
    4. Penjumlahan dan Pengurangan (+ -)
'''

x = 3
y = 2
z = 4
hasil = x** y * z  + x / y - y % z // x
print("hasilnya adalah ",hasil)

print("======")
celcius = int(input('masukan celcius'))
reamur = (4*celcius)/5
fahrenheit = ((5*celcius)/9)+32
kelvin = celcius + 273

print('suhu dalam reamur adalah :',reamur)
print('suhu dalam Farenheit adalah :',fahrenheit)
print('suhu dalam kelvin adalah :',kelvin)

print("======")
reamur = int(input('masukan reamur'))
celcius = (5*reamur)/4
fahrenheit = ((9*reamur)/4)+32
kelvin = (5*reamur)/4 +273

print('suhu dalam celcius adalah :',celcius)
print('suhu dalam Farenheit adalah :',fahrenheit)
print('suhu dalam kelvin adalah :',kelvin)

print("======")
fahrenheit = int(input('masukan farenheit'))
celcius = (5*fahrenheit-9)-32
reamur = ((4*fahrenheit/9))-32
kelvin = (5*fahrenheit)/9-32 +273

print('suhu dalam celcius adalah :',celcius)
print('suhu dalam Farenheit adalah :',reamur)
print('suhu dalam kelvin adalah :',kelvin)

print("======")
kelvin = int(input('masukan kelvin'))
celcius = kelvin-273
reamur= ((4*kelvin)/5)-732
fahrenheit = (9*kelvin)/5-273+32

print('suhu dalam celcius adalah :',celcius)
print('suhu dalam Farenheit adalah :',fahrenheit)
print('suhu dalam kelvin adalah :',reamur)