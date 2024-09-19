# Operasi logika atau boolean

# not, or, and, x-or

# Operasi Not
print("===NOT===")
a = True
c = not a

print('data a =',a)
print('--------NOT')
print('data c =',c)


# Operasi OR
# Jika salah satu dari dua pernyataan bernilai true, maka hasilnya true

print("\n ===Or===")
a = False
b = False
c = a or b

print(a, 'or', b, '=', c)

a = False
b = True
c = a or b

print(a, 'or', b, '=', c)

a = True
b = False
c = a or b

print(a, ' or', b, '=', c)

a = True
b = True
c = a or b

print(a, ' or', b, '=', c)


# Operasi AND
# jika salah satu salah maka hasilnya salah
print("\n ===AND===")
a = False
b = False
c = a and b

print(a, 'and', b, '=', c)

a = False
b = True
c = a and b

print(a, 'and', b, '=', c)

a = True
b = False
c = a and b

print(a, ' and', b, '=', c)

a = True
b = True
c = a and b
print(a, ' and', b, '=', c)

# Operasi X-OR
# Jika kedua pernyataan nya sama (true/true)(false/false)maka hasilnya false

print("\n ===X-OR===")
a = False
b = False
c = a ^ b

print(a, 'X-OR', b, '=', c)

a = False
b = True
c = a ^ b

print(a, 'X-OR', b, '=', c)

a = True
b = False
c = a ^ b

print(a, ' X-OR', b, '=', c)

a = True
b = True
c = a ^ b

print(a, ' X-OR', b, '=', c)