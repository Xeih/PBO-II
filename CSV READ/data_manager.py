from fungsi import Mobil, Merek, Warna, Transaksi
import tkinter as tk
from tkinter import ttk
from typing import Any, Union, Tuple
from collections import defaultdict
from datetime import datetime

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

            # Fungsi konversi yang lebih robust untuk handling angka
            def safe_convert(value):
                try:
                    # Coba konversi ke float terlebih dahulu untuk mendukung angka desimal
                    return float(value)
                except ValueError:
                    # Jika tidak bisa dikonversi, kembalikan value asli
                    return value

            # Sorting dengan konversi yang lebih aman
            items.sort(
                key=lambda x: safe_convert(x[0]), 
                reverse=self._sort_direction[column_id] == 'desc'
            )

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


class LineGraphFrame(tk.Frame):
    def __init__(self, parent, data_manager):
        super().__init__(parent)
        self.data_manager = data_manager
        
        #Mengatur frame agar mengisi bagian bawah
        self.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        #Canvas yang lebih kecil dan lebih proporsional
        self.canvas = tk.Canvas(self, width=350, height=200, bg="white")
        self.canvas.pack(pady=5)
        
        self.data = self.parse_transaction_data()
        self.draw_line_graph()
    
    def parse_transaction_data(self):
        transactions = self.data_manager.list_data('transaksi')
        monthly_transactions = defaultdict(int)
        
        for transaction_id, transaction_data in transactions.items():
            date_str = transaction_data.split('_')[-1]
            date = datetime.strptime(date_str, '%Y-%m-%d')
            month = date.month
            monthly_transactions[month] += 1
        
        return sorted(monthly_transactions.items())
        
    def draw_line_graph(self):
        self.canvas.delete("all")
        
        #Margin dan area grafik yang lebih compact
        x_offset = 35
        y_offset = 170
        width = 300
        height = 150
        
        #Hitung skala
        max_transactions = max(count for _, count in self.data) if self.data else 1
        x_scale = width / (len(self.data) + 1)
        y_scale = height / (max_transactions + 1)
        
        #Gambar sumbu dengan ukuran yang lebih tipis
        self.canvas.create_line(x_offset, y_offset, x_offset + width, y_offset, width=1)
        self.canvas.create_line(x_offset, y_offset, x_offset, y_offset - height, width=1)
        
        #Label sumbu dengan font yang lebih kecil
        self.canvas.create_text(width//2 + x_offset, y_offset + 20, 
                              text="Bulan", font=("Arial", 7, 'bold'))
        self.canvas.create_text(x_offset - 20, y_offset - height//2,
                              text="Jumlah Transaksi", font=("Arial", 7, 'bold'), angle=90)
        
        #Dictionary nama bulan
        month_names = {
            1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "Mei", 6: "Jun",
            7: "Jul", 8: "Ags", 9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"
        }
        
        #Grid dan label sumbu y yang lebih tipis
        for i in range(max_transactions + 1):
            y = y_offset - i * y_scale
            self.canvas.create_line(x_offset, y, x_offset + width, y, 
                                  fill="lightgray", dash=(1, 3))
            self.canvas.create_text(x_offset - 5, y, text=str(i), 
                                  anchor="e", font=("Arial", 6))
        
        #Gambar data dengan ukuran yang lebih kecil
        for i in range(len(self.data)):
            month, count = self.data[i]
            x1 = x_offset + (i + 1) * x_scale
            y1 = y_offset - count * y_scale
            
            #Titik data
            self.canvas.create_oval(x1-2, y1-2, x1+2, y1+2, fill="blue")
            
            #Label bulan
            self.canvas.create_text(x1, y_offset + 10, 
                                  text=month_names[month], font=("Arial", 6))
            
            #Label nilai
            self.canvas.create_text(x1, y1 - 8, 
                                  text=str(count), font=("Arial", 6))
            
            #Garis penghubung
            if i < len(self.data) - 1:
                next_month, next_count = self.data[i + 1]
                x2 = x_offset + (i + 2) * x_scale
                y2 = y_offset - next_count * y_scale
                self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=1)
    
    def refresh(self):
        self.data = self.parse_transaction_data()
        self.draw_line_graph()