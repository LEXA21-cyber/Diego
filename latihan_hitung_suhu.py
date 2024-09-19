#Kalkulator Konveresi Suhu (Temperatur)

#kalkulator celcius
celcius = int(input('masukan celcius:'))
C2reamur = (4*celcius)/5
C2fahrenheit = ((9*celcius)/5)+32
C2kelvin = celcius + 273

print('suhu',celcius,' Derajat celcius adalah:',C2reamur, 'derajat reamur ')
print('suhu',celcius,' Derajat celcius adalah:',C2fahrenheit, 'derajat fahrenheit ')
print('suhu',celcius,' Derajat celcius adalah:',C2kelvin, 'derajat kelvin ')

#kalkulator reamur
print("======")
reamur = int(input('masukan reamur:'))
R2celcius = (5*reamur)/4
R2fahrenheit = ((9*reamur)/4)+32
R2kelvin = R2celcius+273

print('suhu',reamur,' Derajat celcius adalah:',R2celcius, 'derajat celcius ')
print('suhu',reamur,' Derajat celcius adalah:',R2fahrenheit, 'derajat fahrenheit ')
print('suhu',reamur,' Derajat celcius adalah:',R2kelvin, 'derajat kelvin ')

#kalkulator fahrenheit
print("======")
fahrenheit = int(input('masukan farenheit:'))
F2celcius = (5/9) *(fahrenheit-32)
F2reamur = (4/9) * (fahrenheit-32)
F2kelvin = F2celcius + 273

print('suhu',fahrenheit,' Derajat celcius adalah:',F2celcius, 'derajat celcius ')
print('suhu',fahrenheit,' Derajat celcius adalah:',F2reamur, 'derajat reamur ')
print('suhu',fahrenheit,' Derajat celcius adalah:',F2kelvin, 'derajat kelvin ')

print("======")
kelvin = int(input('masukan kelvin:'))
K2celcius = kelvin-273
K2reamur= (4/5)* (K2celcius)
K2fahrenheit = ((9/5)*K2celcius)+32

print('suhu',fahrenheit,' Derajat celcius adalah:',K2celcius, 'derajat celcius ')
print('suhu',fahrenheit,' Derajat celcius adalah:',K2reamur, 'derajat reamur ')
print('suhu',fahrenheit,' Derajat celcius adalah:',K2fahrenheit, 'derajat fahrenheit ')
