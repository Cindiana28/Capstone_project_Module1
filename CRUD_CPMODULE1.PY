import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Membuat list untuk menyimpan data karyawan
karyawan = [
    {"nik": "123456", "nama": "Andi", "umur": 30, "posisi": "Staf", "Department": "HR", "domisili": "Tangerang"},
    {"nik": "189101", "nama": "Budi", "umur": 25, "posisi": "Manager", "Department": "IT", "domisili": "Jakarta"},
    {"nik": "112131", "nama": "Citra", "umur": 28, "posisi": "Staf", "Department": "Finance", "domisili": "Bekasi"},
    {"nik": "116161", "nama": "Diana", "umur": 35, "posisi": "Supervisor", "Department": "Bisnis", "domisili": "Bekasi"},
    {"nik": "113161", "nama": "Surya", "umur": 32, "posisi": "Manager", "Department": "Finance", "domisili": "Jakarta"},
    {"nik": "115189", "nama": "Thia", "umur": 35, "posisi": "Staf", "Department": "Marketing", "domisili": "Bekasi"},
    {"nik": "111161", "nama": "Iren", "umur": 26, "posisi": "Staf", "Department": "Legal", "domisili": "Depok"},
    {"nik": "125461", "nama": "Cindi", "umur": 28, "posisi": "Manager", "Department": "Bisnis", "domisili": "Tangerang"},
]

# Fungsi untuk menampilkan semua data karyawan
def tampilkan_karyawan():
    
    clear_screen()
    print("\nData Karyawan:")
    if len(karyawan) == 0:
        print("Tidak ada data karyawan.")
    else:
        for data in karyawan:
            print(f"NIK: {data['nik']}, Nama: {data['nama']}, Umur: {data['umur']}, Posisi: {data['posisi']}, Department: {data['Department']}, Domisili: {data['domisili']}")
    back_to_menu()

# Menjalankan program menu utama
def menu():
    clear_screen()
    while True:
        print("=== Menu Utama ===")
        print("1. Tampilkan Data Karyawan")
        print("2. Tambah Data Karyawan")
        print("3. Edit Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Cari Data Karyawan")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_karyawan()
        elif pilihan == "2":
            tambah_karyawan()
        elif pilihan == "3":
            edit_karyawan()
        elif pilihan == "4":
            hapus_karyawan()
        elif pilihan == "5":
            cari_karyawan()
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
            back_to_menu()

def back_to_menu():
    input("Tekan Enter untuk kembali...")
    menu()


# Fungsi untuk menambah data karyawan baru
def tambah_karyawan():
    clear_screen()
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")
    umur = int(input("Masukkan Umur: "))
    posisi = input("Masukkan Posisi: ")
    department = input("Masukkan Department: ")
    domisili = input("Masukkan Domisili: ")
    
    karyawan_baru = {"nik": nik, "nama": nama, "umur": umur, "posisi": posisi, "Department": department, "domisili": domisili}
    karyawan.append(karyawan_baru)
    print("Data karyawan berhasil ditambahkan!\n")
    back_to_menu()

# Fungsi untuk mengedit data karyawan
def edit_karyawan():
    clear_screen()
    
    print("\nData Karyawan:")
    if len(karyawan) == 0:
        print("Tidak ada data karyawan.")
    else:
        for data in karyawan:
            print(f"NIK: {data['nik']}, Nama: {data['nama']}, Umur: {data['umur']}, Posisi: {data['posisi']}, Department: {data['Department']}, Domisili: {data['domisili']}")
    
    nik = input("\nMasukkan NIK karyawan yang akan diedit: ")
    for data in karyawan:
        if data['nik'] == nik:
            print(f"Data ditemukan: NIK: {data['nik']}, Nama: {data['nama']}, Umur: {data['umur']}, Posisi: {data['posisi']}, Department: {data['Department']}, Domisili: {data['domisili']}")
            data['nama'] = input("Masukkan Nama baru: ")
            data['umur'] = int(input("Masukkan Umur baru: "))
            data['posisi'] = input("Masukkan Posisi baru: ")
            data['Department'] = input("Masukkan Department baru: ")
            data['domisili'] = input("Masukkan Domisili baru: ")
            print("Data berhasil diperbarui!\n")
            back_to_menu()

    
    print(f"Karyawan dengan NIK {nik} tidak ditemukan.\n")
    back_to_menu()

# Fungsi untuk menghapus data karyawan
def hapus_karyawan():
    clear_screen()
    print("\nData Karyawan:")
    if len(karyawan) == 0:
        print("Tidak ada data karyawan.")
    else:
        for data in karyawan:
            print(f"NIK: {data['nik']}, Nama: {data['nama']}, Umur: {data['umur']}, Posisi: {data['posisi']}, Department: {data['Department']}, Domisili: {data['domisili']}")
    
    nik = input("\nMasukkan NIK karyawan yang akan dihapus: ")
    for data in karyawan:
        if data['nik'] == nik:
            karyawan.remove(data)
            print(f"Karyawan dengan NIK {nik} berhasil dihapus.\n")
            back_to_menu()
    
    print(f"Karyawan dengan NIK {nik} tidak ditemukan.\n")
    back_to_menu()

# Fungsi untuk mencari data karyawan
def cari_karyawan():
    clear_screen()
    nik = input("Masukkan NIK karyawan yang akan dicari: ")
    for data in karyawan:
        if data['nik'] == nik:
            print(f"Data ditemukan: NIK: {data['nik']}, Nama: {data['nama']}, Umur: {data['umur']}, Posisi: {data['posisi']}, Department: {data['Department']}, Domisili: {data['domisili']}")
            back_to_menu()
    
    print(f"Karyawan dengan NIK {nik} tidak ditemukan.\n")
    back_to_menu()

# Menjalankan program menu utama
menu()
