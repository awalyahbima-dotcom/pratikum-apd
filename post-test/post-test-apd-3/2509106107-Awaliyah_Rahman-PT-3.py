NAMA_BENAR = "Awaliyah Rahman"
NIM_BENAR = "2509106107"

BIAYA_LANGGANAN = 1500000

print("=== MEMASUKI WEB STREAMING MUSIK ===")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM : ")

if nama == NAMA_BENAR and nim == NIM_BENAR:
    print("\nLogin berhasil!\n")
    print("=== PILIH PAKET LANGGANAN ===")
    print("1. Bronze diskon (1%)")
    print("2. Silver  (3%)")
    print("3. Gold  (5%)")
    print("4. Platinum  (7%)")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        admin = 0.01
        total = BIAYA_LANGGANAN + (BIAYA_LANGGANAN * admin)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket       : Bronze")
        print("Biaya Admin : 1%")
        print(f"Total Bayar : Rp {total:,.0f}".replace(",", "."))
        print("Keuntungan  : Akses dasar ke lagu-lagu populer")

    elif pilihan == "2":
        admin = 0.03
        total = BIAYA_LANGGANAN + (BIAYA_LANGGANAN * admin)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket       : Silver")
        print("Biaya Admin : 3%")
        print(f"Total Bayar : Rp {total:,.0f}".replace(",", "."))
        print("Keuntungan  : Akses lagu premium dan playlist kustom")

    elif pilihan == "3":
        admin = 0.05
        total = BIAYA_LANGGANAN + (BIAYA_LANGGANAN * admin)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket       : Gold")
        print("Biaya Admin : 5%")
        print(f"Total Bayar : Rp {total:,.0f}".replace(",", "."))
        print("Keuntungan  : Akses lagu premium, playlist kustom, dan mode offline")

    elif pilihan == "4":
        admin = 0.07
        total = BIAYA_LANGGANAN + (BIAYA_LANGGANAN * admin)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket       : Platinum")
        print("Biaya Admin : 7%")
        print(f"Total Bayar : Rp {total:,.0f}".replace(",", "."))
        print("Keuntungan  : Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")

    else:
        print("Pilihan tidak valid!")

else:
    print("\nLogin gagal! Nama atau NIM salah.")
