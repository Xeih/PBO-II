import os
def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

def parse_array(data):
    #misah berdasarkan koma
    if ',' in data:
        array = [item.strip() for item in data.split(',')]
    else:
        #misahin berdasarkan baris baru
        array = [item.strip() for item in data.splitlines() if item.strip()]
    return array

def parse_dictionary(data):
    dict_result = {}
    lines = data.splitlines()   
    for line in lines[1:]:
        if ':' in line:
            key, value = line.split(':')
            dict_result[key.strip()] = value.strip()
    if '=>' in data:
        pairs = data.split(',')
    else:
        pairs = []
    for pair in pairs:
        if '=>' in pair:
            key, value = pair.split('=>')
        else:
            continue
        dict_result[key.strip()] = value.strip()
    return dict_result

def tambah_data(nama_file):
    # Membaca file untuk mencari ID terakhir
    try:
        with open(nama_file, 'r') as file:
            lines = file.readlines()
            if len(lines) > 1:  # Pastikan file tidak kosong dan memiliki header
                # Cari ID terakhir dari data
                last_id = max(int(line.split(':')[0]) for line in lines[1:] if ':' in line)
            else:
                last_id = 0
    except FileNotFoundError:
        print("File Tidak Ditemukan")
    # Meminta input dari pengguna untuk nama warna
    value = input("Masukkan nama data: ") 
    # Tentukan ID baru
    new_id = last_id + 1   
    # Menulis ID dan warna baru ke dalam file
    with open(nama_file, 'a') as file:
        file.write(f"{new_id}:{value}\n")   
    print(f"Data '{new_id}:{value}' berhasil ditambahkan ke {nama_file}")

def baca_id_terakhir(nama_file):
    if not os.path.exists(nama_file):
        return 0
    with open(nama_file, 'r') as file:
        lines = file.readlines()
        if len(lines) > 1:
            last_line = lines[-1].strip()
            if ':' in last_line:
                return int(last_line.split(':')[0])

def data_mobil():
    file_output = 'data_mobil.txt'

    warna_data = baca_file('data_warna.txt')
    if warna_data is None:
        print("File data warna tidak ditemukan")
        
    warna_dict = parse_dictionary(warna_data)

    merek_data = baca_file('data_merek.txt')
    if merek_data is None :
        print ("file ddata merek tidak ditemukan")

    merek_dict = parse_dictionary(merek_data)

    id_terakhir = baca_id_terakhir(file_output)

    



def hapus_data(nama_file):

    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan.")
        return
    data = baca_file(nama_file)
    if data is None:
        print(f"Gagal membaca file {nama_file}.")
        return
    data_dict = parse_dictionary(data)

    #Mengetahui Jenis Data apa yang dihapus
    jenis_data = "item"
    if "warna" in nama_file.lower():
        jenis_data = "warna"
    elif "merek" in nama_file.lower():
        jenis_data = "merek"
    elif "mobil" in nama_file.lower():
        jenis_data = "mobil"

    #Menampilkan list data yang ada
    print(f"Data {jenis_data} yang tersedia:")
    for id_item, info_item in data_dict.items():
        print(f"ID: {id_item}, {jenis_data.capitalize()}: {info_item}")

    id_hapus = input(f"Masukkan ID {jenis_data} yang akan dihapus: ")

    if id_hapus not in data_dict:
        print(f"ID {id_hapus} tidak ditemukan.")
        return
    #Menhapus data dan menulis kembali data yang ada
    del data_dict[id_hapus]
    tulis_kembali_data(nama_file, data_dict, jenis_data)

    print(f"Data {jenis_data} dengan ID {id_hapus} berhasil dihapus.")

def tulis_kembali_data(nama_file, data_dict, jenis_data):
    with open(nama_file, 'w') as file:#Membuka File dengan mode "Write" 
        file.write(f"ID_{jenis_data.upper()}\n")  # Tulis header
        for id_item, info_item in data_dict.items():
            file.write(f"{id_item}:{info_item}\n")