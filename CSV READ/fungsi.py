import os
from pathlib import Path

class FileHandler:
    def bacafile(self, nama_file):
        try:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = Path(current_directory) / nama_file
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    def editfile(self, nama_file, data, mode='w'):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = Path(current_directory) / nama_file
        with open(file_path, mode) as file:
            file.write(data)


class DataItem:
    def __init__(self, file_name, jenis_data):
        self.file_name = file_name
        self.jenis_data = jenis_data
        self.file_handler = FileHandler()

    def parse_dictionary(self, data):
        dict_result = {}
        lines = data.splitlines()
        for line in lines[1:]:
            if ':' in line:
                key, value = line.split(':', 1)
                dict_result[key.strip()] = value.strip()
        return dict_result

    def tambah_data(self, value):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        new_id = max(map(int, data_dict.keys() or [0])) + 1
        data_dict[str(new_id)] = value
        self._tulis_kembali_data(data_dict)
        return new_id

    def hapus_data(self, id_hapus):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        if id_hapus in data_dict:
            del data_dict[id_hapus]
            self._tulis_kembali_data(data_dict)
            return True
        return False

    def tampilkan_data(self, data_dict):
        for key, value in data_dict.items():
            print(f"{key}: {value}")

    def _tulis_kembali_data(self, data_dict):
        content = f"ID_{self.jenis_data.upper()}\n"
        content += "\n".join(f"{id_item}:{info_item}" for id_item, info_item in data_dict.items())
        self.file_handler.editfile(self.file_name, content)

def data_mobil():
    file_output = 'data_mobil.txt'
    
    warna_data = baca_file('data_warna.txt')
    if warna_data is None:
        print("File data warna tidak ditemukan.")
        return
    warna_dict = parse_dictionary(warna_data)

    merek_data = baca_file('data_merek.txt')
    if merek_data is None:
        print("File data merek tidak ditemukan.")
        return
    merek_dict = parse_dictionary(merek_data)

    id_terakhir = baca_id_terakhir(file_output)
    
    while True:
        try:
            id_merek = input("Masukkan nomor merek: ")
            if id_merek not in merek_dict:
                print("Nomor merek tidak valid. Silakan coba lagi.")
                continue
            
            id_warna = input("Masukkan nomor warna: ")
            if id_warna not in warna_dict:
                print("Nomor warna tidak valid. Silakan coba lagi.")
                continue
            
            merek = merek_dict[id_merek]
            warna = warna_dict[id_warna]
            id_mobil = id_terakhir + 1
            
            # Simpan hasil ke file
            mode = 'a' if os.path.exists(file_output) else 'w'
            with open(file_output, mode) as file:
                if mode == 'w':
                    file.write("ID_MOBIL\n")
                file.write(f"{id_mobil}:{merek} {warna}\n")
            
            print(f"Data mobil berhasil disimpan dengan ID: {id_mobil}")
            return f"{id_mobil}:{merek} {warna}"
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

