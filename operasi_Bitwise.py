# Operasi Bitwise, Operasi Biner/Binary

a= 9
b = 5

# Bitwise OR (|) : Melakukan operasi OR terhadap bilangan biner

c = a | b
print("===(|)====")
print("nilai",a," binernya :", format(a,'08b'))
print("nilai",b," binernya :", format(b,'08b'))
print('---------------------------(&)')
print("nilai",c, "binernya :", format(c,'08b'))

# Bitwise And (&) : melakukan operasi AND Terhadap bilangan biner
c = a & b
print("\n===(&)====")
print("nilai",a," binernya :", format(a,'08b'))
print("nilai",b," binernya :", format(b,'08b'))
print('---------------------------(&)')
print("nilai",c, " binernya :", format(c,'08b'))

# Bitwise XOR (^) : melakukan operasi XOR Terhadap bilangan biner
c = a ^ b
print("\n===(^)====")
print("nilai",a," binernya :", format(a,'08b'))
print("nilai",b," binernya :", format(b,'08b'))
print('---------------------------(^)')
print("nilai",c, "binernya :", format(c,'08b'))

# Bitwise NOT (~) : melakukan operasi Negasi Terhadap bilangan biner
print("\n===(NOT 1)====")
c = ~ a
print("nilai",c, "binernya :", format(c,'08b'))

print("\n===(NOT 2)====") # untuk Flip

d = 0b00001001
e = 0b11111111 # di X-OR in dengan biner 255 sbg trick untuk flip biner apapun 
f = d^e

print("nilai",f, "binernya :", format(f,'08b'))

print("\n===(NOT 3)====") # untuk Flip pakai 0xff
c = ~a
f = c & 0xff # di AND-kan dengan 0xff untuk flip biner
print("nilai",f, "binernya :", format(f,'08b'))

# SHIFTING

# Shift Right (>>) : Melakukan operasi penggeseran bit ke kanan pada bilangan biner
print("\n===(>>)====")
print("nilai",a," binernya :", format(a,'08b'))

c = a >> 2

print("nilai",c," binernya :", format(c,'08b'))

# Shift Right (<<) : Melakukan operasi penggeseran bit ke kiri pada bilangan biner
print("\n===(<<)====")
print("nilai",a," binernya :", format(a,'08b'))

c = a << 1

print("nilai",c,"binernya :", format(c,'08b'))