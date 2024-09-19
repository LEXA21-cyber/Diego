# casting type data
# mengubah dari satu type data ke type daya lain
# type data = int, str, bool

## INTEGER
data_int = 12
print ("data ",data_int, "bertipe data =", type(data_int))

intFloat = float(data_int)
intStr = str(data_int)
intBool = bool(data_int)
print ("data ",intFloat, "bertipe data =", type(intFloat))
print ("data ",intStr, "bertipe data =", type(intStr))
print ("data ",intBool, "bertipe data =", type(intBool))

print("===FLOAT===")

## FLOAT 
data_float = 4.5
print ("data ",data_float, "bertipe data =", type(data_float))

floatInt = int(data_float)
floatStr = str(data_float)
floatBool = bool(data_float)
print ("data ",floatInt, "bertipe data =", type(floatInt))
print ("data ",floatStr, "bertipe data =", type(floatStr))
print ("data ",floatBool, "bertipe data =", type(floatBool))

print("===BOOLEAN===")
##BOOLEAN
data_bool = False
print ("data ",data_bool, "bertipe data =", type(data_bool))

boolInt = int(data_bool) #kalau boolean True, int=1,kalau False=0
boolStr = str(data_bool)
boolFloat = float(data_bool) #kalau boolean True, float=0, kalau false float =0
print ("data ",boolInt, "bertipe data =", type(boolInt))
print ("data ",boolStr, "bertipe data =", type(boolStr))
print ("data ",boolFloat, "bertipe data =", type(boolFloat))

print("===string===")

data_string = "12"
print ("data ",data_string, "bertipe data =", type(data_string))

stringInt = int(data_string) #tidak bisa di convert kalau nilai string bukan angka
stringBool = str(data_string) 
StringFloat = float(data_string) 
print ("data ",stringInt, "bertipe data =", type(stringInt))
print ("data ",stringBool, "bertipe data =", type(stringBool))
print ("data ",StringFloat, "bertipe data =", type(StringFloat))
