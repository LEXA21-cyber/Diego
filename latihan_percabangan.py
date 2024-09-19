# LATIHAN PERCABANGAN

angka_1 = float(input("masukan angka ke-1 :"))
operator = (input("masukan operator (+ - x / ):"))
angka_2 = float(input("masukan angka ke-2 :"))

if operator == "+":
    #aksi penjumlahan
    hasil = angka_1 + angka_2
    print(f"hasilnya penjumlahan nya adalah :",hasil)
elif operator == "-" :
    # Operasi Pengurangan
    hasil = angka_1 - angka_2
    print(f"hasilnya pengurangan nya adalah :",hasil)
elif operator == "x":
    # Operator Perkalian
    hasil = angka_1 * angka_2
    print(f"hasilnya perkalian nya adalah :",hasil)
elif operator == "/":
    #Operasi Pembagaian
    hasil = angka_1 / angka_2
    print(f"hasilnya pembagian nya adalah :",hasil)

else:
    print("Hei, bukan operator yang bisa saya kerjain\nSaya belum pinter")

print("program selesai")