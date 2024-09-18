
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

header = ["NIK", "NAMA", "UMUR", "GENDER", "PEKERJAAN", "DOMISILI"]
col_widths = [10, 15, 10, 15, 20, 10]

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

# READ

def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}}')

    print("-"*sum(col_widths))
    
    if (len(contacts) > 0):
        data = contacts.pop(0)
        #print(f"{labels[0]} \t {labels[1]} \t {labels[2]} \t\t {labels[3]} \t\t {labels[4]} \t\t {labels[5]}")
        for data in contacts:
            print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}}')
    else:
        print("Tidak ada data!")
    back_to_menu()

        
def create_contact():
    clear_screen()
    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        NIK = input("NIK (Harus Angka): ")
        if not NIK.isnumeric(): 
            print('Data Harus Berbentuk angka, ulang kembali!')
            back_to_menu()
        NAMA = input("Nama Lengkap: ")
        UMUR = input("Umur: ")
        GENDER = input("Jenis Kelamin: ")
        PEKERJAAN = input("Nama Pekerjaan (HR, IT, MARKETING, OPRATION, BUSINESS, LEGAL,FINANCE): ")
        listPekerjaan = ['HR','IT','MARKETING','OPRATION','BUSINESS','LEGAL','FINANCE']
        isPekerjaanValid = False
        if PEKERJAAN in listPekerjaan:
            isPekerjaanValid = True
            
        if isPekerjaanValid: 
            DOMISILI = input("Tempat Tinggal : ")
            writer.writerow({'NIK': NIK,'NAMA': NAMA,'UMUR': UMUR,'GENDER' : GENDER,'PEKERJAAN' : PEKERJAAN,'DOMISILI' : DOMISILI})
            print("Horeyyy Data Berhasil disimpan!")
            print("Benar")
        else: print("Salah! Silahkan input Kembali")
        
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
        print(f"DOMISILI: {data_found[5]}")
    else:
        print("Tidak ditemukan")
    back_to_menu()
    


def edit_contact():
    clear_screen()
    contacts = []

    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}}')

    print("-"*sum(col_widths))

    data = contacts.pop(0)
    for data in contacts:
        print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}}')

    print("-----------------------")
    NIK = input("NIK: ")
    NAMA = input("Nama Lengkap: ")
    UMUR = input("Umur: ")
    GENDER = input("Jenis Kelamin: ")
    PEKERJAAN = input("Nama Pekerjaan (HR, IT, MARKETING, OPRATION, BUSINESS, LEGAL, FINANCE): ")
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
            contacts[indeks][5] = DOMISILI

        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w", newline='') as csv_file:
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIK': new_data[0], 'NAMA': new_data[1], 'UMUR': new_data[2], 'GENDER': new_data[3], 'PEKERJAAN': new_data[4], 'DOMISILI': new_data[5]}) 

    back_to_menu()



def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    print(f'{header[0]:<{col_widths[0]}} {header[1]:<{col_widths[1]}} {header[2]:<{col_widths[2]}} {header[3]:<{col_widths[3]}} {header[4]:<{col_widths[4]}} {header[5]:<{col_widths[5]}}')

    print("-"*sum(col_widths))

    data = contacts.pop(0)
    for data in contacts:
        print(f'{data[0]:<{col_widths[0]}} {data[1]:<{col_widths[1]}} {data[2]:<{col_widths[2]}} {data[3]:<{col_widths[3]}} {data[4]:<{col_widths[4]}} {data[5]:<{col_widths[5]}}')

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
        fieldnames = ['NIK', 'NAMA','UMUR','GENDER','PEKERJAAN','DOMISILI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIK': new_data[0], 'NAMA': new_data[1], 'UMUR': new_data[2], 'GENDER': new_data[3], 'PEKERJAAN': new_data[4],'DOMISILI': new_data[5]}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()

