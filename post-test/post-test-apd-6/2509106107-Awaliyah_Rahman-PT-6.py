import os

users = {
    1: {"username": "admin", "password": "123", "role": "admin"},
    2: {"username": "user", "password": "123", "role": "user"}
}

buah = {
    1: {"nama": "Apel", "harga": 25000, "stok": 25}
}

id_baru_buah = max(buah.keys()) + 1 if buah else 1
id_baru_user = max(users.keys()) + 1 if users else 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TOKO BUAH AWALIYAH RAHMAN ===")
    print("1. Menu Login")
    print("2. Menu Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA")
        username = input("Username: ")
        password = input("Password: ")

        user_login = None
        for id_user, data_user in users.items():
            if data_user["username"] == username and data_user["password"] == password:
                user_login = data_user
                break

        if user_login is None:
            print("\nUsername atau password salah!, silahkan kembali ke menu login")
            input("Tekan Enter untuk kembali...")
            continue

        if user_login["role"] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("SELAMAT DATANG DI MENU ADMIN")
                print("1. Lihat Data Buah")
                print("2. Tambah Buah")
                print("3. Update Buah")
                print("4. Hapus Buah")
                print("5. Logout")
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DATA BUAH ===")
                    if len(buah) == 0:
                        print("Data buah kosong")
                    else:
                        print("ID\tNama Buah\tHarga\tStok")
                        print("-"*40)
                        for id_buah, data in buah.items():
                            print(f"{id_buah}\t{data['nama']:15}\tRp{data['harga']}\t{data['stok']}")
                    input("\nTekan Enter untuk kembali...")

                elif pilih == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("SILAHKAN TAMBAH BUAH")
                    nama_buah = input("Nama buah: ")
                    harga_buah = input("Harga: ")
                    stok_buah = input("Stok: ")

                    if not (harga_buah.isdigit() and stok_buah.isdigit()):
                        print("Harga dan stok harus berupa angka!, tidak boleh huruf")
                        input("Tekan Enter untuk kembali...")
                        continue

                    buah[id_baru_buah] = {
                        "nama": nama_buah,
                        "harga": int(harga_buah),
                        "stok": int(stok_buah)
                    }
                    id_baru_buah += 1

                    print("Data buah berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                elif pilih == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("SILAHKAN UPDATE BUAH")
                    if len(buah) == 0:
                        print("Data buah kosong")
                        input("Tekan Enter untuk kembali...")
                        continue

                    for id_buah, data in buah.items():
                        print(f"{id_buah}\t{data['nama']:15}\tRp{data['harga']}\t{data['stok']}")
                    print("-"*40)

                    id_update = input("Masukkan ID buah yang ingin anda update: ")
                    if not id_update.isdigit():
                        print("ID harus berupa angka!, bukan huruf")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_update = int(id_update)
                    if id_update not in buah:
                        print("ID buah tidak ditemukan!, silahkan kembali ke menu update buah")
                        input("Tekan Enter untuk kembali...")
                        continue

                    buah_baru = input("Nama buah baru (kosongkan jika tidak ingin diubah oleh anda): ")
                    harga_baru = input("Harga baru (kosongkan jika tidak ingin diubah oleh anda): ")
                    stok_baru = input("Stok baru (kosongkan jika tidak ingin diubah oleh anda): ")

                    if buah_baru == "" and harga_baru == "" and stok_baru == "":
                        print("Tidak ada perubahan di dalam data buah!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    if buah_baru != "":
                        buah[id_update]["nama"] = buah_baru
                    if harga_baru != "" and harga_baru.isdigit():
                        buah[id_update]["harga"] = int(harga_baru)
                    if stok_baru != "" and stok_baru.isdigit():
                        buah[id_update]["stok"] = int(stok_baru)

                    print("Data buah berhasil diperbarui!")
                    input("Tekan Enter untuk kembali...")

                elif pilih == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("SILAHKAN HAPUS BUAH")
                    if len(buah) == 0:
                        print("Belum ada data buah.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    for id_buah, data in buah.items():
                        print(f"{id_buah}\t{data['nama']:15}\tRp{data['harga']}\t{data['stok']}")
                    print("-"*40)

                    id_hapus = input("Masukkan ID buah yang ingin anda hapus: ")
                    if not id_hapus.isdigit():
                        print("ID harus angka!, bukan berupa huruf")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hapus = int(id_hapus)
                    if id_hapus in buah:
                        del buah[id_hapus]
                        print("Data buah berhasil dihapus!")
                    else:
                        print("ID tidak ditemukan!, silahkan kembali ke menu hapus")
                    input("Tekan Enter untuk kembali...")

                elif pilih == "5":
                    break
                else:
                    print("Pilihan tidak valid!, silahkan kembali ke menu hapus")
                    input("Tekan Enter untuk kembali...")

        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("ANDA MASUK SEBAGAI PENGGUNA USER")
                print("1. Lihat Daftar Buah")
                print("2. Logout")
                pilih_user = input("Pilih menu: ")

                if pilih_user == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR BUAH ===")
                    if len(buah) == 0:
                        print("Belum ada data buah.")
                    else:
                        print("ID\tNama Buah\tHarga\tStok")
                        print("-"*40)
                        for id_buah, data in buah.items():
                            print(f"{id_buah}\t{data['nama']:15}\tRp{data['harga']}\t{data['stok']}")
                    input("\nTekan Enter untuk kembali...")

                elif pilih_user == "2":
                    break
                else:
                    print("Pilihan tidak valid!, silahkan input kembali")
                    input("Tekan Enter untuk kembali...")

    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SILAHKAN REGISTER AKUN BARU ANDA")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")

        sudah_ada = False
        for data_user in users.values():
            if data_user["username"] == username:
                sudah_ada = True
                break

        if sudah_ada:
            print("Username sudah digunakan!, silahkan buat username baru")
        else:
            users[id_baru_user] = {
                "username": username,
                "password": password,
                "role": "user"
            }
            print(f"Akun berhasil dibuat dengan ID {id_baru_user}")
            id_baru_user += 1

        input("Tekan Enter untuk kembali...")

    elif menu_awal == "3":
        print("Terima kasih telah menggunakan Aplikasi Toko Buah Awaliyah Rahman!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")