username_asli = "Awaliyah Rahman"
password_asli = "2509106107"

print("=== MASUK  ===")
percobaan = 0
login_sukses = False

while percobaan < 3:
    username = input("Input Nama: ")
    password = input("Input NIM: ")
    if username == username_asli and password == password_asli:
        print("\nLogin berhasil! Selamat datang di BIOSKOP Awaliyah", username)
        login_sukses = True
        break
    else:
        percobaan += 1
        print("Login anda gagal", percobaan)

if not login_sukses:
    print("\nAnda gagal login sebanyak 3 kali. program ini berhenti")
else:
    while True:
        print("\n=== MENU PEMBELIAN TIKET BIOSKOP AWaliyah ===")
        print("1. Tiket Reguler - Rp 50.000")
        print("2. Tiket VIP     - Rp 100.000")
        print("3. Tiket VVIP    - Rp 150.000")
        print("4. Keluar dari web/aplikasi BIOSKOP")
        
        pilihan = input("Pilih jenis tiket (1-4): ")

        if pilihan == "4":
            print("\nTerima kasih telah menggunakan web/aplikasi Awaliyah!")
            break

        if pilihan == "1":
            jenis = "Reguler"
            harga = 50000
        elif pilihan == "2":
            jenis = "VIP"
            harga = 100000
        elif pilihan == "3":
            jenis = "VVIP"
            harga = 150000
        else:
            print("Pilihan tidak ada, coba lagi.")
            continue

        jumlah = input(f"Masukkan jumlah tiket {jenis} yang ingin anda dibeli: ")

        if not jumlah.isdigit() or int(jumlah) <= 0:
            print("Input jumlah tiket tidak valid. atau bukan angka")
            continue

        jumlah = int(jumlah)

        total_bayar = 0
        total_bayar += harga

        bonus = "Tidak ada"
        if total_bayar >= 300000:
            potongan = 0.12 * total_bayar
            total_bayar -= potongan
            bonus = "Diskon 12%"
        elif total_bayar >= 200000:
            potongan = 0.08 * total_bayar
            total_bayar -= potongan
            bonus = "Diskon 8%"
        elif total_bayar >= 150000:
            bonus = "Poster Film Eksklusif"

        print("\n=== STRUK PEMBELIAN  TIKET BIOSKOP AWALIYAH===")
        print("Jenis Tiket   :", jenis)
        print("Jumlah Tiket  :", jumlah)
        print("Total Bayar   : Rp", int(total_bayar))
        print("Bonus/Diskon  :", bonus)
        print("=========================")