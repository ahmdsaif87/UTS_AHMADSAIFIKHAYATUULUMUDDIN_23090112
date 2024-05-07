jumlahBarang = int(input("Masukkan Jumlah Barang: "))
total = 0
for i in range (jumlahBarang):
    harga = int(input("Masukkan Harga: "))
    total += harga
    
print(f"Total Harga : {total}")