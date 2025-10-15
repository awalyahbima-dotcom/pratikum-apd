import os

user = [[1, "admin", "123", "admin"],
        [2, "user", "123", "user"]]

buah = [[1, "Apel", 25000, 25]]
id_counter = 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TOKO BUAH AWALIYAH RAHMAN ===")
    print("1. Menu Login")
    print("2. Menu Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        users = None
        for a in user:
            if a[1] == username and a[2] == password:
                users = a
                break

        if users is None:
            print("Username atau password salah! silahkan coba lagi")
            input("Tekan Enter untuk kembali...")
            continue

        if users[3] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
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
                        print("Belum ada data buah. silahkan menambahkan buah terlebih dahulu")
                    else:
                        print("ID\tBuah\t\tHarga\tStok")
                        print("-"*40)
                        for b in buah:
                            print(f"{b[0]}\t{b[1]:15}\tRp{b[2]}\t{b[3]}")
                    input("\nTekan Enter untuk kembali...")

                elif pilih == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH BUAH ===")
                    nama_buah = input("Buah: ")
                    harga_buah = input("Harga buah: ")
                    stok_buah = input("Stok buah: ")

                    if not (harga_buah.isdigit() and stok_buah.isdigit()):
                        print("Harga dan stok harus angka tidak boleh huruf!")
                        input("Tekan Enter untuk kembali ke menu tambah buah...")
                        continue

                    for b in buah:
                        if b[0] == id_counter:
                            id_counter += 1  # tambah 1 jika id sudah digunakan

                    buah.append([id_counter, nama_buah, int(harga_buah), int(stok_buah)])
                    id_counter += 1
                    print("Buah berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                elif pilih == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE BUAH ===")
                    if len(buah) == 0:
                        print("Belum ada data buah. silahkan menambahkan buah terlebih dahulu")
                        input("Tekan Enter untuk kembali...")
                        continue

                    for b in buah:
                        print(f"{b[0]}\t{b[1]:15}\tRp{b[2]}\t{b[3]}")
                    print("-"*40)

                    id_update = input("Masukkan ID buah yang ingin diupdate: ")
                    if not id_update.isdigit():
                        print("ID harus berupa angka!, tidak boleh huruf")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_update = int(id_update)
                    ditemukan = False

                    for b in buah:
                        if b[0] == id_update:
                            ditemukan = True
                            print(f"Update buah: {b[1]}")
                            buah_baru = input("Buah baru (kosongkan jika anda tidak ingin mengubah): ")
                            harga_baru = input("Harga baru buah (kosongkan jika anda tidak ingin mengubah): ")
                            stok_baru = input("Stok baru buah (kosongkan jika anda tidak ingin mengubah): ")

                            if buah_baru == "" and harga_baru == "" and stok_baru == "":
                                print("Tidak ada yang diupdate.")
                                break

                            if buah_baru != "":
                                b[1] = buah_baru
                            if harga_baru != "" and harga_baru.isdigit():
                                b[2] = int(harga_baru)
                            elif harga_baru != "" and not harga_baru.isdigit():
                                print("Error: Harga harus angka!")

                            if stok_baru != "" and stok_baru.isdigit():
                                b[3] = int(stok_baru)
                            elif stok_baru != "" and not stok_baru.isdigit():
                                print("Error: Stok harus angka!")

                            print("Data buah berhasil diperbarui!")
                            break

                    if not ditemukan:
                        print("ID buah tidak ditemukan!")

                    input("Tekan Enter untuk kembali...")

                elif pilih == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS BUAH ===")
                    if len(buah) == 0:
                        print("Belum ada data buah.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    for b in buah:
                        print(f"{b[0]}\t{b[1]:15}\tRp{b[2]}\t{b[3]}")
                    print("-"*40)

                    id_hapus = input("Masukkan ID buah yang akan dihapus: ")
                    if not id_hapus.isdigit():
                        print("ID harus angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hapus = int(id_hapus)
                    hapus = False
                    for b in buah:
                        if b[0] == id_hapus:
                            buah.remove(b)
                            hapus = True
                            print("Buah berhasil dihapus!")
                            break
                    if not hapus:
                        print("ID tidak ditemukan!")

                    input("Tekan Enter untuk kembali...")

                elif pilih == "5":
                    break

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU PENGGUNA ===")
                print("1. Lihat Daftar Buah")
                print("2. Logout")
                pilih_user = input("Pilih menu: ")

                if pilih_user == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR BUAH ===")
                    if len(buah) == 0:
                        print("Belum ada data buah.")
                    else:
                        print("ID\tNama Buah\t\tHarga Buah\tStok")
                        print("-"*40)
                        for b in buah:
                            print(f"{b[0]}\t{b[1]:15}\tRp{b[2]}\t{b[3]}")
                    input("\nTekan Enter untuk kembali...")

                elif pilih_user == "2":
                    break

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SILAHKAN REGISTER AKUN BARU ANDA===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        ada = False
        for u in user:
            if u[1] == username:
                ada = True
                break

        if ada:
            print("Username sudah digunakan!")
            input("Tekan Enter untuk kembali...")
            continue

        new_id = user[-1][0] + 1 if user else 1
        user.append([new_id, username, password, "user"])

        print(f"Akun berhasil didaftarkan dengan ID User: {new_id}")
        input("Tekan Enter untuk kembali...")

    elif menu_awal == "3":
        print("Terima kasih telah menggunakan Aplikasi Toko Buah Awaliyah Rahman!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")

      

   