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