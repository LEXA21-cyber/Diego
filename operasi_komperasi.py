# Operasi Komperasi (Perbandingan)
# Bahwa setiap hasil dari komparasi adalah bool (biner) (True/False)

# Lebih dari (>)
# Kurang dari (<)
# Lebih dari sama dengan (>=)
# Kurang dari sama dengan (<=)
# Sama dengan (==)
# Tidak sama dengan (!=)
# Is
# Is not 

a = 4
b = 2

# Lebih Besar dari (>)

hasil = a > 3
print(a,'>', '3 =',hasil )

hasil = b > 3
print(b,'>', '3 =', hasil)

hasil = b > 2
print(b,'>', '2 =', hasil)


# Kurang dari (<)
print('======= Kurang dari <')

hasil = a < 3
print(a,'<', '3 =', hasil)

hasil = b < 3
print(b,'<', '3 =', hasil)

hasil = b < 2
print(b,'<', '2 =', hasil)


# Lebih dari sama dengan (>=)
print('======= Lebih dari atau sama dengan >=')

hasil = a >= 3
print(a,'>=', '3 =', hasil)

hasil = b >= 3
print(b,'>=', '3 =', hasil)

hasil = b >= 2
print(b,'>=', '2 =', hasil)


# kurang dari sama dengan (<=)
print('======= Kurang dari atau sama dengan <=')

hasil = a <= 3
print(a,'<=', '3 =', hasil)

hasil = b <= 3
print(b,'<=', '3 =', hasil)

hasil = b <= 2
print(b,'<=', '2 =', hasil)

# sama dengan (==)
print('======= sama dengan ==')

hasil = a == 4
print(a,'==', '4 =', hasil)

hasil = b == 2
print(b,'==', '2 =', hasil)


# Tidak sama dengan (!=)
print('======= Tidak sama dengan !=')

hasil = a != 4
print(a,'!=', '4 =', hasil)

hasil = b != 4
print(b,'!=', '4 =', hasil)

# 'is' sebagai komperasi object identity
print('======= Object Identity (is)')

x = 5 # ini adalah assigment membuat object
y = 5

print('nilai x =,',x, ', id =', hex(id(x)))
print('nilai y =,',y, ', id =', hex(id(y)))

hasil = x is 5
print('x is 5 adalah =', hasil)

print('======= Object Identity (is not)')

x = 5 # ini adalah assigment membuat object
y = 6

print('nilai x =,',x, ', id =', hex(id(x)))
print('nilai y =,',y, ', id =', hex(id(y)))

hasil = x is not y
print('x is not y adalah =', hasil)