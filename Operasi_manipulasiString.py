# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)

Nama_depan = "Vatian"
Nama_tengah = "D"
Nama_akhir = "'Ganz"

nama_lengkap = Nama_depan+ " "+ Nama_tengah+ " " +Nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string

PjgString = len(nama_lengkap)
print("panjang string nya adalah",PjgString)

# 3. Operator untuk string
# in : Untuk Mengecek apakah ada komponen char / string di dalam string

char = "b"
CekStatus = char in nama_lengkap
print("huruf " + char + " ada di" + nama_lengkap + "= " + str(CekStatus))

# not in : Untuk mengecek apakah tidak ada komponen char pada string tsb
char2 = "y"
CekStatus2 = char2 not in nama_lengkap
print("huruf " + char2 + " tidak ada di" + nama_lengkap + "= " + str(CekStatus2))

# Menggunakan (*) Untuk mengulang string
print("wk"*10)
print(15*"wk")
print("haha"*10)

# indexing
print("index ke-0 adalah : " + nama_lengkap[0])
print("index ke-1 adalah : " + nama_lengkap[1])
print("index ke-2 adalah : " + nama_lengkap[2])
print("index ke-3 adalah : " + nama_lengkap[3])
print("index ke-4 adalah : " + nama_lengkap[4])
print("index ke-5 adalah : " + nama_lengkap[5])
print("index ke-(-1) adalah : " + nama_lengkap[-1])
print("index ke-(-2) adalah : " + nama_lengkap[-2])
print("index ke-(-3) adalah : " + nama_lengkap[-3])
print("index ke-(-4) adalah : " + nama_lengkap[-4])
print("\nmengindex Rentang tertentu")
print("index ke-(0:7) adalah : " + nama_lengkap[0:7])
print("index ke-(0:7) adalah : " + "PTDARRAHMAN"[0:5])
print("\nmengindex index dengan pola deret tertentu")
print("index ke-(0,2,3,6,8,10) :" + "PTDARRAHMAN" [0:11:2])


# Mengecek item yang paling kecil
print("paling kecil :" + min("PTD ARRAHMAN"))
# Mengecek item yang paling besar
print("paling besar :" + max("PTD ARRAHMAN"))
# cek berapa besar suatu char
ascii_code = ord('T')
print("ASCII kode untuk t adalah :" + str(ascii_code))
# Cek angka tertentu jadi char apa?
data_int = 117
print("Char untuk ASCII 117 adalah : " + chr(data_int))
    
# 4.Operator dalam bentuk method
## Menghitung jumlah char tertentu pada satu set string
DataChar = "ucup marucup pararucup"
DataChar2 = "otong surotong pararotong"
ItungChar = DataChar.count("u")
ItungChar2 = DataChar2.count("o")
print("jumlah u pada " + DataChar + " = " + str(ItungChar))
print("jumlah o pada " + DataChar2 + " = " + str(ItungChar2))

## Mengubah cast pada string
# UPPERCASE
kata = "bro !"
print("normal case = "+ kata)
kata = kata.upper()
print("Uppercase = " + kata)

# lowercase
kataAlay = "CemMunguUD EaaahH"
print("normal case = "+ kataAlay)
kataAlay = kataAlay.lower()
print("Lowercase = " + kataAlay)

# Capitalized
print("===capital===")
capital = "pada suatu hari, ada orang \nganteng yaitu saya sendiri. finish."
print(capital)
capital = capital.capitalize()
print(capital)

## Pengecekan dengan isX method = bool

# contoh pengecekan lower case
salam = "assalamu'alaykum"
apakah_lower = salam.islower() # hasilnya itu boolean
print(salam + " is lower = " + str(apakah_lower)) # hasilnya akan true kalau semua isinya kecil/lower case

# contoh pengecekan uppercase
greet = "HALLO MAS BRO!"
apakah_upper = greet.isupper() # hasil nya juga boolean
print(greet + " is Upper = " + str(apakah_upper)) # hasilnya akan true kalau semua isinya capital/uppercase

# isalpha() --> untuk mengecek semuanya huruf
# isalnum() --> untuk mengecek huruf dan angka
# isdecimal() --> angka saja
# isspace() --> spasi,tab,new line \n

# istitle() --> semua kata dimulai dari huruf besar
judulfilm = "It Is Okay Not To Be Orkay"
cek_IsTitle = judulfilm.istitle()
print(judulfilm + " apakah judul ? = " + str(cek_IsTitle))


## Ngecek kompenen string | starswith() | endswith()
# starswith()
cek_start = "aku mau jadi hafidz qur'an".startswith("aku")
print('"kalimat "aku mau jadi hafidz quran" dimulai dengan kata "aku", apakah betul ? ' + str(cek_start))

# endswith()
cek_end = "aku mau jadi hafidz qur'an".endswith("qur'an")
print('"kalimat "aku mau jadi hafidz quran" diakhiri dengan kata "quran", apakah betul ? ' + str(cek_end))


## Penggabungan komponen | join() | split()

pisah = ['satu-satu','aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' ehm '.join(pisah)
print(gabungan)

print("\ncontoh split")
gabungan2 ="aku ehm sayang ehm kamu"
print(gabungan2.split(' ehm '))

# alokasi/alignment karakter | ljust() | rjust() | center()
print("\nalokasi karakter / aligment")
print("\n=====JUDUL=====")
print(5*"=" + "JUDUL" + 5*"=")

alokasi = "JUDUL".center(15,"=")
print(alokasi)

alokasi = "JUDUL".ljust(15,"=")
print(alokasi)

alokasi = "JUDUL".rjust(15,"=")
print(alokasi)


# Kebalikan nya -> strip()
alokasi = alokasi.strip("=") #  menghilangkan karakter yang ada di dalam method strip, dalam hal ini tanda(=)
print(alokasi)

# Mengubah string menjadi bytes dengan encoding tertentu. 
s = "hello"
alokasi = s.encode('utf-8') 
print(alokasi)

# Memformat string menggunakan placeholde|.format()
s = "Hello, {}!"
alokasi = s.format("Alice")  # Output: "Hello, Alice!"
print(alokasi)

# Memeriksa apakah semua karakter dalam string adalah alfanumerik|.isalnunm()
s = "hello123"
alokasi = s.isalnum() 
print(alokasi)

#.isdigit(): Memeriksa apakah semua karakter dalam string adalah digit.
s = "12345"
s.isdigit()  # Output: True

#.lstrip(chars): Menghapus karakter dari sisi kiri string
s = "   hello"
alokasi =s.lstrip() 
print(alokasi)

# .replace(old, new, count): Mengganti semua kemunculan substring old dengan new. Parameter count opsional, untuk membatasi jumlah penggantian.
s = "hello world"
alokasi =s.replace("world", "Python")
print(alokasi)

# .rtrim(chars): Menghapus karakter dari sisi kanan string.
s = "hello   "
alokasi= s.rstrip()  
print(alokasi)

#.expandtabs(tabsize): Mengganti tab dengan spasi. Parameter tabsize menentukan jumlah spasi untuk setiap tab.
s = "hello\tworld"
alokasi =s.expandtabs(2) 
print(alokasi)

# .removeprefix(prefix): Menghapus awalan tertentu dari string jika ada. Jika awalan tidak ada, string tidak berubah.
s = "TestHook"
alokasi = s.removeprefix("Test") 
print(alokasi)

# .removesuffix(suffix): Menghapus akhiran tertentu dari string jika ada. Jika akhiran tidak ada, string tidak berubah.
s = "MiscTests"
alokasi = s.removesuffix("Tests")  
print(alokasi)

# .partition(separator): Membagi string menjadi tuple berdasarkan separator. Mengembalikan tiga bagian: bagian sebelum separator, separator itu sendiri, dan bagian setelah separator.
s = "hello world"
alokasi = s.partition(" ") 
print(alokasi)

# .format_map(mapping): Memformat string menggunakan map (seperti dictionary) sebagai sumber pengganti.
s = "Hello {name}"
alokasi = s.format_map({"name": "Alice"})  
print(alokasi)

# .swapcase(): Mengubah semua huruf kapital menjadi huruf kecil dan sebaliknya.
s = "Hello World"
alokasi = s.swapcase()  
print(alokasi)

# .strip(chars): Menghapus karakter dari sisi kiri dan kanan string.
s = "   hello   "
alokasi = s.strip()
print(alokasi)