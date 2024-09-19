# Operasi yang dapat di lakukan dengan penyingkatan
# Operasi yang di tambah dengan assigment
# Mengoperasikan nilai dari variable itu sendiri dengan nilai lain

a = 5 # ini adalah assigment
print('nilai a adalah :',a)

a = a + 1
print('nilai a adalah',a)

a += 1 # Artinya adalah a = a+1
print('nilai a adalah :',a)

a -= 2 # Artinya adalah a = a - 2
print('nilai a -= 2 adalah :',a)

a *= 5 # Artinya adalah a = a * 2
print('nilai a *= 2 adalah :',a)

a /= 2 # Artinya adalah a = a / 2
print('nilai a /= 2 adalah :',a)

b = 10
print('\nNilai b adalah :',b)

b %= 3
print('Nilai dari b %= 3 adalah :',b)

print('nilai b sekarang adalah :',b)

b += 1
print('nilai b sekarang setelah b+=1 adalah :',b)

b **= 8
print('Nilai dari b **= 8 adalah :',b)

b //= 5
print('Nilai dari b //= 5 adalah :',b)

# Bisa di lakukan untuk operasi bitwise
# OR

c = True
print ('\nNilai c adalah :',c)
c |= False
print('nilai c |= false adalah :',c)

c = False
c |= False
print('nilai c(false) |= false adalah :',c)

# AND
c = True

c &= True
print('\nNilai c &= true hasilnya adalah :',c)

c &= False
print('Nilai c &= false hasilnya adalah :',c)

c &= True
print('Nilai c &= true hasilnya adalah :',c)

c &= False
print('Nilai c &= false hasilnya adalah :',c)

# X-OR
c = True
print('\nNilai c sekarang adalah :',c)

c ^= False
print('nilai c ^= false adalah :',c)

c ^= True
print('nilai c ^= true adalah :',c)

c ^= False
print('nilai c ^= false adalah :',c)

c ^= True
print('nilai c ^= true adalah :',c)

# SHIFTING / geser-geser bit

d = 0b0100
print('\nNilai d adalah :',format(d,'04b'))

d >>= 2
print('nilai d adalah :',d, '\nbinernya :',format(d,'04b'))


d <<= 3
print('nilai d adalah :',d, '\nbinernya :',format(d,'04b'))
