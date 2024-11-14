from fungsi import Mobil, Merek, Warna, Transaksi
import tkinter as tk
from tkinter import ttk

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
    
# First, make sure to include the SortableTreeview class definition at the top of your file
class SortableTreeview(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Dictionary untuk menyimpan arah sorting
        self._sort_direction = {}
        
        # Bind fungsi sort ke event klik pada heading
        self.bind('<Button-1>', self._handle_click)
    
    def _handle_click(self, event):
        region = self.identify_region(event.x, event.y)
        if region == "heading":
            # Dapatkan kolom yang diklik
            column = self.identify_column(event.x)
            column_index = int(column[1]) - 1  # Convert '#1' to 0
            column_id = self['columns'][column_index]
            
            # Toggle arah sorting
            if column_id not in self._sort_direction:
                self._sort_direction[column_id] = 'asc'
            else:
                self._sort_direction[column_id] = 'desc' if self._sort_direction[column_id] == 'asc' else 'asc'
            
            # Ambil semua item
            items = [(self.set(item, column_id), item) for item in self.get_children('')]

            # Cek apakah kolom yang disort adalah ID dan konversi ke integer jika perlu
            if column_id == 'id':  # Ganti 'id' dengan ID kolom yang sesuai
                items = [(int(value), item) for value, item in items]  # Konversi ke integer

            # Sorting items
            items.sort(key=lambda x: x[0], reverse=self._sort_direction[column_id] == 'desc')

            # Reorder items di treeview
            for index, (_, item) in enumerate(items):
                self.move(item, '', index)
                        
            # Update tampilan header untuk menunjukkan arah sorting
            for col in self['columns']:
                if col == column_id:
                    direction = ' ↑' if self._sort_direction[col] == 'asc' else ' ↓'
                    self.heading(col, text=f"{col}{direction}")
                else:
                    # Remove arrow if exists in text
                    current_text = self.heading(col)['text']
                    clean_text = current_text.replace(' ↑', '').replace(' ↓', '')
                    self.heading(col, text=clean_text)
    