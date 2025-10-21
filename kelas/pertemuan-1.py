
# Membuat set 
buah = {"apel", "jeruk", "mangga", "apel"}  
print(buah)

angka_ganjil = {1, 3, 5, 7, 9} 
for angka in angka_ganjil: 
print(angka) 

Daftar_buku = { 
"Buku1" : "Bumi Manusia", 
"Buku2" : "Laut Bercerita", 
"Buku3" : "Anak semua bangsa"
}

print(Daftar_buku["Buku1"]){
print(Daftar_buku) 
for Lea in Daftar buku:
    print(Lea) 
}

Biodata = { 
"Nama" : "Ananda Daffa Harahap", 
"NIM" : 2409106050, 
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
"Mahasiswa_Aktif" : True, 
"Social Media" : ("instagram" : "daffahrhap" )
}


print(f"nama saya adalah {Biodata["Nama"]}") 
print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
print(f"nama saya adalah {Biodata.get("Nama")}") 
print(Biodata.get("Nama")) 

print(f"nama saya adalah {Biodata["Nama"]}") 
print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
print(f"nama saya adalah {Biodata.get("Nama")}") 
print(Biodata.get("Nama")) 

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 
 
#Sebelum Dihapus 
print(data) 
 
data.clear() 
 
#Setelah dihapus 
print(data) 
 
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
{}

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 

print("Jumlah Data = ", len(data)) 
 
Jumlah Data = 3 

buku = { 
 "Buku1" : "Bumi Manusia", 
 "Buku2" : "Laut Bercerita" 
} 
 
pinjam = buku.copy() 
 
print("Dictionary yang telah disalin : ", pinjam) 
 
Dictionary yang telah disalin : {"Buku1" : "Bumi Manusia", "Buku2" : "Laut 
Bercerita"} 

key = "apel", "jeruk", "mangga" 
 value = 1 
 buah = dict.fromkeys(key, value) 
 print(buah) 
 {'apel': 1, 'jeruk': 1, 'mangga': 1}

 Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for penyanyi, album in Musik.items(): 
 print(f"Musik milik {i} adalah : ") 
 for song in j: 
  print(song) 
 print("") 
 
Musik milik The Chainsmoker adalah : 
All we Know 
The Paris 
 
Musik milik Alan Walker adalah : 
Alone 
Lily 
 
Musik milik Neffex adalah : 
Best of Me 
Memories