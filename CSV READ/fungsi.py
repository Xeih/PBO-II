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
        print(f"Data written to {file_path}")  # Debug print

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

    def edit_data(self, id_edit, new_value):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        if id_edit in data_dict:
            data_dict[id_edit] = new_value
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
    def __init__(self):
        super().__init__('data_warna.txt', 'warna')

    def list_warna(self):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        return data_dict

    def tambah_warna(self, warna):
        return self.tambah_data(warna)

    def hapus_warna(self, id_warna):
        return self.hapus_data(id_warna)

    def edit_warna(self, id_warna, new_warna):
        return self.edit_data(id_warna, new_warna)

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

    def edit_merek(self, id_merek, new_merek):
        return self.edit_data(id_merek, new_merek)

class Mobil(DataItem):
    def __init__(self):
        super().__init__('data_mobil.txt', 'NAMA_MOBIL')
        self.data_warna = Warna()
        self.data_merek = Merek()

    def list_mobil(self):
        data = self.file_handler.bacafile(self.file_name)
        if not data:
            return {}
        lines = data.splitlines()
        mobil_dict = {}
        for line in lines[1:]:  # Skip the header line
            parts = line.split(':')
            if len(parts) == 4:
                id_mobil, nama_mobil, id_merek, id_warna = parts
                mobil_dict[id_mobil] = f"{nama_mobil}:{id_merek}:{id_warna}"
        return mobil_dict

    def tambah_mobil(self, nama_mobil, id_merek, id_warna):
        warna_dict = self.data_warna.list_warna()
        merek_dict = self.data_merek.list_merek()

        if id_merek not in merek_dict:
            raise ValueError("Nomor merek tidak valid.")
        if id_warna not in warna_dict:
            raise ValueError("Nomor warna tidak valid.")

        return self.tambah_data(f"{nama_mobil}:{id_merek}:{id_warna}")

    def hapus_mobil(self, id_mobil):
        return self.hapus_data(id_mobil)

    def edit_mobil(self, id_mobil, nama_mobil, id_merek, id_warna):
        warna_dict = self.data_warna.list_warna()
        merek_dict = self.data_merek.list_merek()

        if id_merek not in merek_dict:
            raise ValueError("Nomor merek tidak valid.")
        if id_warna not in warna_dict:
            raise ValueError("Nomor warna tidak valid.")

        return self.edit_data(id_mobil, f"{nama_mobil}:{id_merek}:{id_warna}")

    def get_detail_mobil(self, id_mobil):
        mobil_dict = self.list_mobil()
        if id_mobil in mobil_dict:
            nama_mobil, id_merek, id_warna = mobil_dict[id_mobil].split(':')
            merek = self.data_merek.list_merek().get(id_merek, "Merek tidak ditemukan")
            warna = self.data_warna.list_warna().get(id_warna, "Warna tidak ditemukan")
            return {
                'nama_mobil': nama_mobil,
                'merek': merek,
                'warna': warna
            }
        return None

class Transaksi(DataItem):
    def __init__(self):
        super().__init__('data_transaksi.txt', 'transaksi')

    def list_transaksi(self):
        data_dict = self.parse_dictionary(self.file_handler.bacafile(self.file_name) or "")
        return data_dict

    def tambah_transaksi(self, transaksi_data):     
        return self.tambah_data(transaksi_data)

    def hapus_transaksi(self, id_transaksi):
        return self.hapus_data(id_transaksi)

    def edit_transaksi(self, id_transaksi, transaksi_data):
        return self.edit_data(id_transaksi, transaksi_data)

    def get_detail_transaksi(self, id_transaksi):
        transaksi_dict = self.list_transaksi()
        if id_transaksi in transaksi_dict:
            id_mobil, jarak, tanggal = transaksi_dict[id_transaksi].split('_')
            return {
                'id_mobil': id_mobil,
                'jarak': jarak,
                'tanggal': tanggal
            }
        return None
