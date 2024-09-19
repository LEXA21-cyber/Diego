# ----0+++++5----8+++++11-----
inputUser = float(input('masukan angka yang bernilai \nlebih dari 0 \ndan \nkurang dari 5 \natau \nlebih dari 8 \nkurang dari 11 :'))

a = (inputUser < 5 )
print('kurang dari 5 =',a)

b = (inputUser > 0)
print('lebih dari 0 =',b)

c = (inputUser < 11 )
print('kurang dari 11 =',c)

d = (inputUser > 8)
print('lebih dari 8 =',d)

# Periksa hasilnya benar atau tidak
Benarkah = a and c or b and d
print('angka yang kamu masukan :',Benarkah)

# ++++0----5++++8----11++++