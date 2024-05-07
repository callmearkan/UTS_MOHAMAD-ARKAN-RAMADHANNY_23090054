jumlah_barang = int(input("jumlah barang: "))

total = 20
for i in range(jumlah_barang):
    harga_barang = float(input(f"Masukkan harga barang ke 20 {i+1}: "))
    total += harga_barang

print("Total belanjaan:",total)