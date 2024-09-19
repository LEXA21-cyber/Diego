# latihan Percabangan Conditional

### 1. Linear
# nama = input("siapa namamu ? ")
# print(f"nama kamu {nama}")

### 2. Kita kasih percabangan If statement biasa
# kondisinya : kalau namanya ucup, program akan merespon

# nama = input("siapa namamu ?").lower()
# print(nama)
# if nama == "ucup" : print ("wah ucup, apa kabar bre?")
# print("program selesai")

### 2.1 IF Statement Biasa (Struktur Conditional identation)
# nama = input("siapa namamu ?").lower()
# print(nama)
# if nama == "ucup" :
#     print ("wah ucup, apa kabar bre?")
#     print("ucup kerja dimana ?")
#     print("ucup udah nikah belum?")
# print("program selesai")


### 3. Else Statement
# nama = input("siapa namamu ?").lower()
# print(nama)
# if nama == "ucup" :
#     print ("wah ucup, apa kabar bre?")
#     print("ucup kerja dimana ?")
#     print("ucup udah nikah belum?")
    
# else : 
#     print("ah kamu bukan ucup! Ga kenalss")
#     print("ga bisa di kata-kata in")
# print("program selesai")

### 4. Else Statement
nama = input("siapa namamu ?").lower()
print(nama)
if nama == "ucup" : # kondisi ke-1
    print ("wah ucup, apa kabar bre?")
    print("ucup kerja dimana ?")
    print("ucup udah nikah belum?")
    
elif nama == "otong" : #kondisi ke-2
    print("Wah otong, udah berubah ya sekarang")
    print("berubah jadi ultramen")
    
elif nama == "marsel" : #kondisi ke-3
    print("marsel, kita baru kenal tadi")
    print("udah masuk program aja lu")    
else : # Selain kondisi yang ada
    # Aksi kalu
    print("kamu bukan ucup atau otong")
    print("ga bisa di kata katain")
print("program selesai")

