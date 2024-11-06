from fungsi import Mobil, Merek, Warna, Transaksi

class DataManager:
    def __init__(self):
        self.warna = Warna()
        self.merek = Merek()
        self.mobil = Mobil()
        self.transaksi = Transaksi()

    def get_data_object(self, data_type):
        if data_type == 'warna':
            return self.warna
        elif data_type == 'merek':
            return self.merek
        elif data_type == 'mobil':
            return self.mobil
        elif data_type == 'transaksi':
            return self.transaksi
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
        elif data_type == 'transaksi':
            return data_object.list_transaksi()

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
    
    def tambah_transaksi(self, transaksi_data):
        # transaksi_data should be in the format "id_mobil_jarak_tanggal"
        return self.transaksi.tambah_transaksi(transaksi_data)
    
    def get_mobil_by_merek(self, id_merek):
        mobil_list = []
        mobil_dict = self.get_data_object('mobil').list_mobil()
        for id_mobil, data in mobil_dict.items():
            nama_mobil, id_merek_mobil, id_warna = data.split(':')
            if id_merek_mobil == id_merek:
                mobil_list.append((id_mobil, nama_mobil))
        return mobil_list

    def get_mobil_by_warna(self, id_warna):
        mobil_list = []
        mobil_dict = self.get_data_object('mobil').list_mobil()
        for id_mobil, data in mobil_dict.items():
            nama_mobil, id_merek, id_warna_mobil = data.split(':')
            if id_warna_mobil == id_warna:
                mobil_list.append((id_mobil, nama_mobil))
        return mobil_list
    