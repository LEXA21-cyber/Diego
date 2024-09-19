# TYPE-TYPE data yg ada di python

# TYPE data STANDAR
# type data angka satuan/bil.bulat (integer)
data_integer = 5
print("data",data_integer)
print("bertipe data ", type(data_integer))

print("=======")
# type data angka decimal (float)
data_float = 5.4
print("data",data_float)
print("bertipe data ", type(data_float))

print("=======")
# type data kumpulan karakter (string)
data_string = "joni joni yes bro"
print("data",data_string)
print("bertipe data ", type(data_string))

print("=======")
# type data biner true/false (boolean)
data_bool = True
print("data",data_bool)
print("bertipe data ", type(data_bool))

print("======")

# 2 type data khusus
# bilangan kompleks
data_complex = complex(4,5)
print("data",data_complex)

print("======")

# 3 type data dari bahasa c
# import data dari library c

from ctypes import c_double
data_c_double = c_double(3.178900876555555678998765432)
print("data",data_c_double)
print("bertipe data ", type(data_c_double))
