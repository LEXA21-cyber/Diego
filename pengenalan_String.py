data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''
    1. Dengan menggunakan single qoute '....'
    2. Dengan menggunakan double qoute "...."
'''

data = 'menggunakan single qoute'
print(data)

data2 = "menggunakan double qoute"
print(data2)


# Contoh menulis kalimat langsung
# "hallo apa kabar", ucup berkata pada otong
print('"hallo apa kabar", ucup berkata pada otong')

print('"halo apa kabar?"')
print("'halo apa kabar?'")
print("ini hari jum'at")

# 2. menggunakan Tanda backslash (\)
# Untuk menandai karakter spesial

# Membuat tanda (') menjadi string
print('ini hari jum\'at')
print('g\'day, is\'it?')
print('no i don\'t')

# Membuat tanda (\) menjadi string

print('C:\\user\\public\\Newfolder')

# Tab
print('ucup \t\totong, semakin jauhan')

# backspase
print('ucup \botong')

# Newline
print('baris pertama. \nbaris kedua.') # -> LF Line Fieed => unix, mac os, linux
print('baris pertama. \rbaris kedua.') # -> CR Carriage Return => commod
print('baris pertama. \r\nbaris kedua.') # -> CRLF => windows

# 3. String Literal atau RAW

# Warning / hati hati
print(r'C:\User\NewFolder')

# Kita menggunakan RAW string
print(r'C\User\NewFolde\New1\New2')

# Multiline Literal Sring
print('''
  Nama : Ucup
  Hobi : Boxing
  Cita Cita : Menjadi raja bajak laut
  kelas : 3 SD    

      ''')

# Multiline Literal Sring dan RAW 
print(r'''
  Nama : Ucup
  Hobi : Boxing
  Cita Cita : Menjadi raja bajak laut
  kelas : 3 SD    
  tempat nyimpe rahasia di PC: 
  C:\user\public\hidden
      ''')