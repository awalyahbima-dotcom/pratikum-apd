nama =input("Masukkan nama lengkap :")
nim = input("Masukkan NIM: ")
harga = int(input("Masukkan Harga Laptop (Rp): "))

diskon_laptop = {
    "Acer": 5,
    "Asus": 7,
    "Lenovo": 10
}

print("\n" + "="*50)
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp {harga:,}")
print("="*50)

print(f"{'Merek':<10} {'Diskon':<10} {'Harga Akhir (Rp)':>20}")
print("-"*50)

for merek, persen in diskon_laptop.items() :
    diskon = harga * (persen / 100)
    harga_akhir = harga - diskon
    print(f"{merek:<10} {persen:<10}% {harga_akhir:>20,.0f}")