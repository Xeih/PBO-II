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

class Warna(DataItem):
    def __ini__(self):
        super().__init__('data_warna.txt', 'warna')

    def list_warna(self):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")

    def tambah_warna(self, warna):
        return self.tambah_data(warna)

    def hapus_warna(self, id_warna):
        return self.hapus_data(id_warna)

class Merek(DataItem):
    def __init__(self):
        super().__init__('data_merek.txt', 'merek')

    def list_merek(self):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        return data_dict

    def tambah_merek(self, merek):
        return self.tambah_data(merek)

    def hapus_merek(self, id_merek):
        return self.hapus_data(id_merek)


class Mobil(DataItem):
    def __init__(self):
        super().__init__('data_mobil.txt', 'mobil')
        self.data_warna = Warna()
        self.data_merek = Merek()

    def list_mobil(self):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        return data_dict
    
    def tambah_mobil(self, id_merek, id_warna):
        warna_dict = self.data_warna.parse_dictionary(self.data_warna.file_handler.bacafile(self.data_warna.file_name) or "")
        merek_dict = self.data_merek.parse_dictionary(self.data_merek.file_handler.bacafile(self.data_merek.file_name) or "")

        if id_merek not in merek_dict:
            raise ValueError("Nomor merek tidak valid.")
        if id_warna not in warna_dict:
            raise ValueError("Nomor warna tidak valid.")

        merek = merek_dict[id_merek]
        warna = warna_dict[id_warna]

        mobil_data = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        new_id = max(map(int, mobil_data.keys() or [0])) + 1
        mobil_data[str(new_id)] = f"{merek} {warna}"

        self._tulis_kembali_data(mobil_data)
        return f"{new_id}:{merek} {warna}"

    def hapus_mobil(self, id_mobil):
        return self.hapus_data(id_mobil)




    
    

