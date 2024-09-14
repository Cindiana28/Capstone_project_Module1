
import csv # Untuk menyimpan data
import os # 

csv_filename = 'Data_Karyawan.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== DATA KARYAWAN PERUSAHAAN PT CITRA BUANA ===")
    print("[1] Lihat Daftar karyawan")
    print("[2] Buat Data Karyawan Baru")
    print("[3] Edit Data Karyawan")
    print("[4] Hapus Data Karyawan")
    print("[5] Cari Data Karyawan")
    print("[0] Keluar")
    print("------------------------")
    selected_menu = input("Pilih Menu > ")
    
    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        edit_contact()
    elif(selected_menu == "4"):
        delete_contact()
    elif(selected_menu == "5"):
        search_contact()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

header = ["NIK", "NAMA", "UMUR", "GENDER", "PEKERJAAN", "JABATAN", "STATUS", "DOMISILI"]
col_widths = [10, 15, 10, 15, 20, 10, 20, 15]

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}} {header[6]:<{col_widths[6]}} {header[7]:<{col_widths[7]}}')

    print("-"*sum(col_widths))
    
    if (len(contacts) > 0):
        data = contacts.pop(0)
        #print(f"{labels[0]} \t {labels[1]} \t {labels[2]} \t\t {labels[3]} \t\t {labels[4]} \t\t {labels[5]} \t\t {labels[6]} \t\t {labels[7]} \t\t {labels[8]}")
        for data in contacts:
            print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}} {data[6]:<{col_widths[6]}} {data[7]:<{col_widths[7]}}')
    else:
        print("Tidak ada data!")
    back_to_menu()

def contains_all(value, array):
    """
    Memeriksa apakah nilai mengandung semua elemen dari array.

    :param value: String yang akan diperiksa.
    :param array: List dari string yang dicari.
    :return: True jika nilai mengandung semua elemen dari array, False sebaliknya.
    """
    return all(element in value for element in array)


def create_contact():
    clear_screen()
    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','JABATAN','STATUS','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        NIK = input("NIK: ").isnumeric()
        NAMA = input("Nama Lengkap: ")
        UMUR = input("Umur: ")
        GENDER = input("Jenis Kelamin: ")
        PEKERJAAN = input("Nama Pekerjaan (HR, IT, MARKETING, OPRATION, BUSINESS, LEGAL): ")
        listPekerjaan = ['HR','IT','MARKETING','OPRATION','BUSINESS','LEGAL']
        isPekerjaanValid = contains_all(PEKERJAAN, listPekerjaan)
        if isPekerjaanValid: 
            JABATAN = input("Jabatan (Officer, Supervisor, Manager, Vice President): ")
            STATUS = input("Status Karyawan (KARYAWAN TETAP, KONTRAK, MAGANG): ")
            DOMISILI = input("Tempat Tinggal : ")
            writer.writerow({'NIK': NIK,'NAMA': NAMA,'UMUR': UMUR,'GENDER' : GENDER,'PEKERJAAN' : PEKERJAAN,'JABATAN' : JABATAN,'STATUS' : STATUS,'DOMISILI' : DOMISILI})
            print("Horeyyy Data Berhasil disimpan!")
            print("Benar")
        else: print("Salah")
        PEKERJAAN = input("Nama Pekerjaan (HR, IT, MARKETING, OPRATION, BUSINESS, LEGAL): ")
        

    back_to_menu()


def search_contact():
    clear_screen()
    contacts = []

    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    NIK = input("Cari berdasarkan NIK>")

    data_found = []

    # mencari contact
    data = contacts.pop(0)
    indeks = 0
    for data in contacts:
        if (data[0] == NIK):
            data_found = contacts[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"NAMA: {data_found[1]}")
        print(f"UMUR: {data_found[2]}")
        print(f"GENDER: {data_found[3]}")
        print(f"PEKERJAAN: {data_found[4]}")
        print(f"JABATAN: {data_found[5]}")
        print(f"STATUS: {data_found[6]}")
        print(f"DOMISILI: {data_found[7]}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    


def edit_contact():
    clear_screen()
    contacts = []

    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}} {header[6]:<{col_widths[6]}} {header[7]:<{col_widths[7]}}')

    print("-"*sum(col_widths))

    data = contacts.pop(0)
    for data in contacts:
        print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}} {data[6]:<{col_widths[6]}} {data[7]:<{col_widths[7]}}')

    print("-----------------------")
    NIK = input("NIK: ")
    NAMA = input("Nama Lengkap: ")
    UMUR = input("Umur: ")
    GENDER = input("Jenis Kelamin: ")
    PEKERJAAN = input("Nama Pekerjaan (HR, IT, MARKETING, OPRATION, BUSINESS, LEGAL): ")
    JABATAN = input("Jabatan (Officer, Supervisor, Manager, Vice President): ")
    STATUS = input("Status Karyawan (KARYAWAN TETAP, KONTRAK, MAGANG): ")
    DOMISILI = input("Tempat Tingga: ")


    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data[0] == NIK):
            contacts[indeks][1] = NAMA
            contacts[indeks][2] = UMUR
            contacts[indeks][3] = GENDER
            contacts[indeks][4] = PEKERJAAN
            contacts[indeks][5] = JABATAN
            contacts[indeks][6] = STATUS
            contacts[indeks][7] = DOMISILI


        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w", newline='') as csv_file:
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','JABATAN','STATUS','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIK': new_data[0], 'NAMA': new_data[1], 'UMUR': new_data[2], 'GENDER': new_data[3], 'PEKERJAAN': new_data[4], 'JABATAN': new_data[5], 'STATUS': new_data[6], 'DOMISILI': new_data[7]}) 

    back_to_menu()



def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}} {header[6]:<{col_widths[6]}} {header[7]:<{col_widths[7]}}')

    print("-"*sum(col_widths))

    data = contacts.pop(0)
    for data in contacts:
        print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}} {data[6]:<{col_widths[6]}} {data[7]:<{col_widths[7]}}')

    print("-----------------------")
    NIK = input("Hapus NIK> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data[0] == NIK):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w", newline='') as csv_file:
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','JABATAN','STATUS','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIK': new_data[0], 'NAMA': new_data[1], 'UMUR': new_data[2], 'GENDER': new_data[3], 'PEKERJAAN': new_data[4], 'JABATAN': new_data[5], 'STATUS': new_data[6], 'DOMISILI': new_data[7]}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()