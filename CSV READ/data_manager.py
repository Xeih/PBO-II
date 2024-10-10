from fungsi import Mobil, Merek, Warna

class DataManager:
    def __init__(self):
        self.warna = Warna()
        self.merek = Merek()
        self.mobil = Mobil()

    def get_data_object(self, data_type):
        if data_type == 'warna':
            return self.warna
        elif data_type == 'merek':
            return self.merek
        elif data_type == 'mobil':
            return self.mobil
        else:
            raise ValueError(f"Unknown data type: {data_type}")

    def list_data(self, data_type):
        data_object = self.get_data_object(data_type)
        if data_type == 'warna':
            return data_object.list_warna()
        elif data_type == 'merek':
            return data_object.list_merek()
        elif data_type == 'mobil':
            return data_object.list_mobil()

    def delete_data(self, data_type, item_id):
        data_object = self.get_data_object(data_type)
        if data_type == 'warna':
            return data_object.hapus_warna(item_id)
        elif data_type == 'merek':
            return data_object.hapus_merek(item_id)
        elif data_type == 'mobil':
            return data_object.hapus_mobil(item_id)

    def edit_data(self, data_type, item_id, new_value):
        data_object = self.get_data_object(data_type)
        if data_type == 'warna':
            return data_object.edit_warna(item_id, new_value)
        elif data_type == 'merek':
            return data_object.edit_merek(item_id, new_value)
        elif data_type == 'mobil':
            nama_mobil, id_merek, id_warna = new_value.split(':')
            return data_object.edit_mobil(item_id, nama_mobil, id_merek, id_warna)

    def tambah_warna(self, warna_baru):
        return self.warna.tambah_warna(warna_baru)
        
    def tambah_merek(self, merek_baru):
        return self.merek.tambah_merek(merek_baru)
        
    def tambah_mobil(self, nama_mobil, id_merek, id_warna):
        return self.mobil.tambah_mobil(nama_mobil, id_merek, id_warna)