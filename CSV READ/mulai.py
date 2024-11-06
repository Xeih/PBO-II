import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas,ttk
from data_manager import DataManager
from datetime import datetime
from tkcalendar import DateEntry

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Mobil")
        self.geometry("500x500")
        self.data_manager = DataManager()
        self.current_data_type = 'warna'

        self.create_frames()
        self.create_widgets()
        self.show_home()

    def create_frames(self):
        self.home_frame = tk.Frame(self)
        self.mobil_frame = tk.Frame(self)
        self.warna_frame = tk.Frame(self)
        self.merk_frame = tk.Frame(self)
        self.warna_tambah_frame = tk.Frame(self)
        self.merk_tambah_frame = tk.Frame(self)
        self.mobil_tambah_frame = tk.Frame(self)
        self.detail_frame = tk.Frame(self)
        self.transaksi_frame = tk.Frame(self)
        self.transaksi_history_frame = tk.Frame(self)

    def create_widgets(self):
        # Home frame widgets
        canvas = Canvas(self.home_frame, width=500, height=150, bg="#FFA559", highlightthickness=0)
        canvas.create_text(250, 75, text="DATA MOBIL", font=("Helvetica", 24, "bold"), fill="white")
        canvas.pack()

        frame = tk.Frame(self.home_frame)
        frame.pack(pady=20)

        button_mobil = tk.Button(frame, text="MOBIL", font=("Helvetica", 12), compound=tk.TOP, bg="#377477", fg="white", padx=20, pady=10, command=lambda: self.show_data('mobil'))
        button_mobil.grid(row=0, column=0, padx=20)

        button_merk = tk.Button(frame, text="MERK", font=("Helvetica", 12), compound=tk.TOP, bg="#800408", fg="white", padx=20, pady=10, command=lambda: self.show_data('merek'))
        button_merk.grid(row=0, column=1, padx=20)

        button_warna = tk.Button(frame, text="WARNA", font=("Helvetica", 12), compound=tk.TOP, bg="#ca696a", fg="white", padx=20, pady=10, command=lambda: self.show_data('warna'))
        button_warna.grid(row=0, column=2, padx=20)

        #frame = self.home_frame.winfo_children()[1]  # Assuming the frame is the second child of home_frame
        button_transaksi = tk.Button(frame, text="TRANSAKSI", font=("Helvetica", 12), compound=tk.TOP, bg="#664344", fg="white", padx=20, pady=10, command=self.show_transaksi)
        button_transaksi.grid(row=1, column=1, padx=20, pady=10)  # Adjust the row and column as needed

        # Create a frame to contain the Treeview and scrollbar
        tree_frame = tk.Frame(self.transaksi_history_frame)
        tree_frame.pack(pady=10, fill="both", expand=True)

        # Data frames (mobil, warna, merk)
        for frame, title in [(self.mobil_frame, "List Mobil"), (self.warna_frame, "List Warna"), (self.merk_frame, "List Merk")]:
            label = tk.Label(frame, text=title, font=("Helvetica", 16))
            label.pack(pady=10)
            
            listbox = tk.Listbox(frame, width=30, height=10)
            listbox.pack(pady=10)

            if frame == self.mobil_frame:
                detail_button = tk.Button(frame, text="Tampilkan Detail", command=self.show_mobil_detail)
                detail_button.pack(side=tk.TOP)
                
            back_button = tk.Button(frame, text="Kembali", command=self.show_home)
            back_button.pack(side=tk.BOTTOM, pady=10)
            
            edit_button = tk.Button(frame, text="Edit", command=lambda f=frame: self.show_edit_dialog(f))
            edit_button.pack(side=tk.TOP)

            if frame == self.warna_frame:
                add_button = tk.Button(frame, text="+",font=("Helvetica", 12), command=self.show_tambah_warna)
                add_button.pack(side=tk.RIGHT, padx=5, pady=15)
                
                delete_button = tk.Button(frame, text="-",font=("Helvetica", 12), command=lambda: self.delete_action('warna'))
                delete_button.pack(side=tk.LEFT, padx=5, pady=15)

                show_mobil_button = tk.Button(frame, text="View", command=self.show_mobil_by_warna)
                show_mobil_button.pack(side=tk.BOTTOM, pady=5)
                
            if frame == self.merk_frame:
                add_button = tk.Button(frame, text="+", command=self.show_tambah_merek)
                add_button.pack(side=tk.RIGHT, padx=5, pady=5)
                
                delete_button = tk.Button(frame, text="-", command=lambda: self.delete_action('merek'))
                delete_button.pack(side=tk.LEFT, padx=5, pady=5)

                show_mobil_button = tk.Button(frame, text="View ", command=self.show_mobil_by_merek)
                show_mobil_button.pack(side=tk.BOTTOM, pady=5)
                
            if frame == self.mobil_frame:
                add_button = tk.Button(frame, text="+", command=self.show_tambah_mobil)
                add_button.pack(side=tk.RIGHT, padx=5, pady=5)

                delete_button = tk.Button(frame, text="-", command=lambda: self.delete_action('mobil'))
                delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Warna tambah frame
        label_tambah = tk.Label(self.warna_tambah_frame, text="Tambah Warna Baru", font=("Helvetica", 12))
        label_tambah.pack(pady=5)
        
        self.warna_entry = tk.Entry(self.warna_tambah_frame, width=30)
        self.warna_entry.pack(pady=5)
        
        tambah_button = tk.Button(self.warna_tambah_frame, text="Tambah Warna", command=self.tambah_warna)
        tambah_button.pack(pady=10)
        
        back_button = tk.Button(self.warna_tambah_frame, text="Kembali", command=lambda: self.show_data('warna'))
        back_button.pack(pady=10)
        
        # Merk tambah frame
        label_tambah = tk.Label(self.merk_tambah_frame, text="Tambah Merek Baru", font=("Helvetica", 12))
        label_tambah.pack(pady=5)
        
        self.merek_entry = tk.Entry(self.merk_tambah_frame, width=30)
        self.merek_entry.pack(pady=5)
        
        tambah_button = tk.Button(self.merk_tambah_frame, text="Tambah Merek", command=self.tambah_merek)
        tambah_button.pack(pady=10)
        
        back_button = tk.Button(self.merk_tambah_frame, text="Kembali", command=lambda: self.show_data('merek'))
        back_button.pack(pady=10)
        
        # Mobil tambah frame
        label_tambah = tk.Label(self.mobil_tambah_frame, text="Tambah Mobil Baru", font=("Helvetica", 12))
        label_tambah.pack(pady=5)
        
        self.nama_mobil_entry = tk.Entry(self.mobil_tambah_frame, width=30)
        self.nama_mobil_entry.pack(pady=5)

        self.merek_var = tk.StringVar()
        self.warna_var = tk.StringVar()

        label_merek = tk.Label(self.mobil_tambah_frame, text="Pilih Merek", font=("Helvetica", 10))
        label_merek.pack(pady=5)
        
        self.merek_option = tk.OptionMenu(self.mobil_tambah_frame, self.merek_var, *self.data_manager.list_data('merek').keys())
        self.merek_option.pack(pady=5)
        
        label_warna = tk.Label(self.mobil_tambah_frame, text="Pilih Warna", font=("Helvetica", 10))
        label_warna.pack(pady=5)
        
        self.warna_option = tk.OptionMenu(self.mobil_tambah_frame, self.warna_var, *self.data_manager.list_data('warna').keys())
        self.warna_option.pack(pady=5)
        
        tambah_button = tk.Button(self.mobil_tambah_frame, text="Tambah Mobil", command=self.tambah_mobil)
        tambah_button.pack(pady=10)
        
        back_button = tk.Button(self.mobil_tambah_frame, text="Kembali", command=lambda: self.show_data('mobil'))
        back_button.pack(pady=10)

        # Detail frame
        self.detail_label = tk.Label(self.detail_frame, text="", font=("Helvetica", 12))
        self.detail_label.pack(pady=10)

        back_button = tk.Button(self.detail_frame, text="Kembali", command=self.show_data)
        back_button.pack(pady=10)

        #EDIT FRAME
        self.edit_frame = tk.Frame(self)
        label_edit = tk.Label(self.edit_frame, text="Edit Data", font=("Helvetica", 12))
        label_edit.pack(pady=5)
        
        self.edit_entry = tk.Entry(self.edit_frame, width=30)
        self.edit_entry.pack(pady=5)
        
        save_button = tk.Button(self.edit_frame, text="Simpan", command=self.save_edit)
        save_button.pack(pady=10)
        
        back_button = tk.Button(self.edit_frame, text="Kembali", command=self.show_data)
        back_button.pack(pady=10)

        # EDIT BUATMOBIL
        self.edit_mobil_frame = tk.Frame(self)
        label_edit = tk.Label(self.edit_mobil_frame, text="Edit Mobil", font=("Helvetica", 12))
        label_edit.pack(pady=5)
        
        self.edit_nama_mobil_entry = tk.Entry(self.edit_mobil_frame, width=30)
        self.edit_nama_mobil_entry.pack(pady=5)

        self.edit_merek_var = tk.StringVar()
        self.edit_warna_var = tk.StringVar()
        
        label_merek = tk.Label(self.edit_mobil_frame, text="Pilih Merek", font=("Helvetica", 10))
        label_merek.pack(pady=5)
        
        self.edit_merek_option = tk.OptionMenu(self.edit_mobil_frame, self.edit_merek_var, "")
        self.edit_merek_option.pack(pady=5)
        
        label_warna = tk.Label(self.edit_mobil_frame, text="Pilih Warna", font=("Helvetica", 10))
        label_warna.pack(pady=5)
        
        self.edit_warna_option = tk.OptionMenu(self.edit_mobil_frame, self.edit_warna_var, "")
        self.edit_warna_option.pack(pady=5)
        
        save_button = tk.Button(self.edit_mobil_frame, text="Simpan", command=self.save_edit_mobil)
        save_button.pack(pady=10)
        
        back_button = tk.Button(self.edit_mobil_frame, text="Kembali", command=self.show_data)
        back_button.pack(pady=10)

        # Modifikasi bagian transaksi frame
        label_transaksi = tk.Label(self.transaksi_frame, text="Tambah Transaksi", font=("Helvetica", 12))
        label_transaksi.pack(pady=5)

        label_mobil = tk.Label(self.transaksi_frame, text="Pilih Mobil", font=("Helvetica", 10))
        label_mobil.pack(pady=5)

        self.mobil_var = tk.StringVar()
        self.mobil_option = ttk.Combobox(self.transaksi_frame, textvariable=self.mobil_var, state="readonly")
        self.mobil_option.pack(pady=5)

        label_jarak = tk.Label(self.transaksi_frame, text="Jarak (km)", font=("Helvetica", 10))
        label_jarak.pack(pady=5)

        self.jarak_entry = tk.Entry(self.transaksi_frame, width=30)
        self.jarak_entry.pack(pady=5)

        label_tanggal = tk.Label(self.transaksi_frame, text="Tanggal Transaksi", font=("Helvetica", 10))
        label_tanggal.pack(pady=5)

        self.tanggal_entry = DateEntry(self.transaksi_frame, width=12, background='white',
                                       foreground='grey', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.tanggal_entry.pack(pady=5)

        tambah_button = tk.Button(self.transaksi_frame, text="Tambah Transaksi", command=self.tambah_transaksi)
        tambah_button.pack(pady=10)

        lihat_history_button = tk.Button(self.transaksi_frame, text="HISTORY", command=self.show_transaksi_history)
        lihat_history_button.pack(pady=5)

        back_button = tk.Button(self.transaksi_frame, text="Kembali", command=self.show_home)
        back_button.pack(pady=10)

        # Create a frame to contain the Treeview and scrollbar
        tree_frame = tk.Frame(self.transaksi_history_frame)
        tree_frame.pack(pady=10, fill="both", expand=True)

        # Create Treeview with adjusted column widths
        self.history_tree = ttk.Treeview(tree_frame, columns=('Tanggal', 'Mobil', 'Jarak'), show='headings')
        self.history_tree.heading('Tanggal', text='Tanggal')
        self.history_tree.heading('Mobil', text='Mobil')
        self.history_tree.heading('Jarak', text='Jarak (km)')
        
        # Set column widths
        self.history_tree.column('Tanggal', width=100)
        self.history_tree.column('Mobil', width=150)
        self.history_tree.column('Jarak', width=100)
        
        # Add scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.history_tree.pack(side="left", fill="both", expand=True)

        # Add the back button at the bottom
        back_button = tk.Button(self.transaksi_history_frame, text="Kembali", command=self.show_transaksi)
        back_button.pack(side="bottom", pady=10)

        # Create Tambah Transaksi frame
        self.tambah_transaksi_frame = tk.Frame(self)
        label_tambah_transaksi = tk.Label(self.tambah_transaksi_frame, text="Tambah Transaksi", font=("Helvetica", 12))
        label_tambah_transaksi.pack(pady=5)

        tambah_button = tk.Button(self.tambah_transaksi_frame, text="Tambah Transaksi", command=self.tambah_transaksi)
        tambah_button.pack(pady=10)

        back_button = tk.Button(self.tambah_transaksi_frame, text="Kembali", command=self.show_transaksi)
        back_button.pack(pady=10)



        # Tambahkan label untuk history
        history_label = tk.Label(self.home_frame, text="History Transaksi Terakhir:", 
                                font=("Helvetica", 12, 'bold'))
        history_label.pack(pady=10, side=tk.TOP)

        # Buat Treeview untuk history di home frame
        self.home_history_tree = ttk.Treeview(self.home_frame, 
                                            columns=('Tanggal', 'Mobil', 'Jarak'), 
                                            show='headings',
                                            height=5)  # Batasi jumlah baris yang ditampilkan
        
        # Set heading untuk setiap kolom
        self.home_history_tree.heading('Tanggal', text='Tanggal')
        self.home_history_tree.heading('Mobil', text='Mobil')
        self.home_history_tree.heading('Jarak', text='Jarak (km)')

        # Set lebar kolom
        self.home_history_tree.column('Tanggal', width=100)
        self.home_history_tree.column('Mobil', width=150)
        self.home_history_tree.column('Jarak', width=100)

        self.home_history_tree.pack(pady=10)

    #fiter frame
        filter_frame = tk.Frame(self.transaksi_history_frame)
        filter_frame.pack(pady=5)

        # Start date filter
        start_date_label = tk.Label(filter_frame, text="Tanggal Mulai:")
        start_date_label.pack(side=tk.LEFT, padx=5)
        
        self.start_date_filter = DateEntry(filter_frame, width=12, background='white',
                                         foreground='grey', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.start_date_filter.pack(side=tk.LEFT, padx=5)

        # End date filter
        end_date_label = tk.Label(filter_frame, text="Tanggal Selesai:")
        end_date_label.pack(side=tk.LEFT, padx=5)
        
        self.end_date_filter = DateEntry(filter_frame, width=12, background='white',
                                       foreground='grey', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.end_date_filter.pack(side=tk.LEFT, padx=5)

        # Filter button
        filter_button = tk.Button(filter_frame, text="Filter", command=self.apply_date_filter)
        filter_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        reset_button = tk.Button(filter_frame, text="Reset", command=self.reset_date_filter)
        reset_button.pack(side=tk.LEFT, padx=5)


    def show_home(self):
        self.hide_all_frames()
        self.home_frame.pack()
        self.update_home_history()

    def show_data(self, data_type=None):
        self.hide_all_frames()
        if data_type:
            self.current_data_type = data_type
        if self.current_data_type == 'mobil':
            frame = self.mobil_frame
        elif self.current_data_type == 'warna':
            frame = self.warna_frame
        elif self.current_data_type == 'merek':
            frame = self.merk_frame
        frame.pack()
        self.update_listbox(self.current_data_type)

    def show_tambah_warna(self):
        self.hide_all_frames()
        self.warna_tambah_frame.pack()
        
    def show_tambah_merek(self):
        self.hide_all_frames()
        self.merk_tambah_frame.pack()
        
    def show_tambah_mobil(self):
        self.hide_all_frames()
        self.mobil_tambah_frame.pack()
        self.update_options()
        self.merek_var.set('')  # Reset pilihan merek
        self.warna_var.set('')  # Reset pilihan warna

    def hide_all_frames(self):
        for frame in (self.home_frame, self.mobil_frame, self.warna_frame, self.merk_frame, self.warna_tambah_frame, self.merk_tambah_frame, self.mobil_tambah_frame, self.detail_frame):
            frame.pack_forget()

    def update_listbox(self, data_type):
        listbox = self.warna_frame.winfo_children()[1] if data_type == 'warna' else \
                  self.merk_frame.winfo_children()[1] if data_type == 'merek' else \
                  self.mobil_frame.winfo_children()[1]
        
        listbox.delete(0, tk.END)
        data_dict = self.data_manager.list_data(data_type)
        for key, value in data_dict.items():
            if data_type == 'mobil':
                nama_mobil = value.split(":")[0]
                listbox.insert(tk.END, f"{key}: {nama_mobil}")
            else:
                listbox.insert(tk.END, f"{key}: {value}")

    def update_options(self):
        self.merek_option['menu'].delete(0, 'end')
        for id_merek, merek in self.data_manager.list_data('merek').items():
            self.merek_option['menu'].add_command(label=merek, command=tk._setit(self.merek_var, merek))
        
        self.warna_option['menu'].delete(0, 'end')
        for id_warna, warna in self.data_manager.list_data('warna').items():
            self.warna_option['menu'].add_command(label=warna, command=tk._setit(self.warna_var, warna))
        
        self.merek_var.trace('w', self.on_merek_select)
        self.warna_var.trace('w', self.on_warna_select)

    def tambah_warna(self):
        warna_baru = self.warna_entry.get()
        if warna_baru.strip() == "":
            messagebox.showerror("Error", "Warna tidak boleh kosong!")
        else:
            self.data_manager.tambah_warna(warna_baru)
            self.update_listbox('warna')
            self.warna_entry.delete(0, tk.END)
            messagebox.showinfo("Sukses", f"Warna {warna_baru} berhasil ditambahkan!",command=self.show_data('warna'))
    
    def tambah_merek(self):
        merek_baru = self.merek_entry.get()
        if merek_baru.strip() == "":
            messagebox.showerror("Error", "Merek tidak boleh kosong!")
        else:
            self.data_manager.tambah_merek(merek_baru)
            self.update_listbox('merek')
            self.merek_entry.delete(0, tk.END)
            messagebox.showinfo("Sukses", f"Merek {merek_baru} berhasil ditambahkan!", command=self.show_data('merek'))
    
    def tambah_mobil(self):
        nama_mobil = self.nama_mobil_entry.get()
        if nama_mobil.strip() == "" or not hasattr(self, 'selected_merek_id') or not hasattr(self, 'selected_warna_id'):
            messagebox.showerror("Error", "Nama mobil, merek, dan warna tidak boleh kosong!")
        else:
            try:
                result = self.data_manager.tambah_mobil(nama_mobil, self.selected_merek_id, self.selected_warna_id)
                # Get the details for success message
                merek = self.merek_var.get()  # Get selected merek name
                warna = self.warna_var.get()   # Get selected warna name
                
                success_message = f"Mobil {nama_mobil} {merek} {warna} Berhasil ditambahkan !!!"
                
                self.update_listbox('mobil')
                self.nama_mobil_entry.delete(0, tk.END)
                self.merek_var.set('')
                self.warna_var.set('')
                messagebox.showinfo("Sukses", success_message)
                self.show_data('mobil')
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def delete_action(self, data_type):
        listbox = self.warna_frame.winfo_children()[1] if data_type == 'warna' else \
                  self.merk_frame.winfo_children()[1] if data_type == 'merek' else \
                  self.mobil_frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            parts = selected_item.split(":", 1)
            if len(parts) == 2:
                item_id, item_name = parts
                item_id = item_id.strip()
                item_name = item_name.strip()
                self.show_confirm_dialog(data_type, item_id, item_name)
            else:
                messagebox.showwarning("Peringatan", f"Format data {data_type} tidak sesuai.")
        else:
            messagebox.showwarning("Peringatan", f"Silakan pilih {data_type} yang ingin dihapus.")

    def show_confirm_dialog(self, data_type, item_id, item_name):
        confirm_window = tk.Toplevel(self)
        confirm_window.title("Konfirmasi Hapus")
        confirm_window.geometry("300x150")
        
        label = tk.Label(confirm_window, text=f"Apakah Anda yakin ingin menghapus {data_type} {item_name}?", wraplength=250)
        label.pack(pady=20)
        
        yes_button = tk.Button(confirm_window, text="Yes", command=lambda: self.delete_item(confirm_window, data_type, item_id, item_name))
        yes_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        no_button = tk.Button(confirm_window, text="No", command=confirm_window.destroy)
        no_button.pack(side=tk.RIGHT, padx=20, pady=20),

    def delete_item(self, confirm_window, data_type, item_id, item_name):
        if self.data_manager.delete_data(data_type, item_id):
            confirm_window.destroy()
            self.update_listbox(data_type)
            messagebox.showinfo("Sukses", f"{data_type.capitalize()} {item_name} berhasil dihapus!")
        else:
            messagebox.showerror("Error", f"Gagal menghapus {data_type} {item_name}.")

    def show_edit_dialog(self, frame):
        listbox = frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            item_id, item_value = selected_item.split(":", 1)
            item_id = item_id.strip()
            item_value = item_value.strip()
            
            self.current_edit_id = item_id
            
            if self.current_data_type == 'mobil':
                self.show_edit_mobil_dialog(item_id, item_value)
            else:
                self.edit_entry.delete(0, tk.END)
                self.edit_entry.insert(0, item_value)
                self.hide_all_frames()
                self.edit_frame.pack()
        else:
            messagebox.showwarning("Peringatan", f"Silakan pilih item yang ingin diedit.")

    def show_edit_mobil_dialog(self, item_id, item_value):
        mobil_details = self.data_manager.mobil.get_detail_mobil(item_id)
        if mobil_details:
            self. edit_nama_mobil_entry.delete(0, tk.END)
            self.edit_nama_mobil_entry.insert(0, mobil_details['nama_mobil'])
            
            self.update_edit_options()
            
            self.edit_merek_var.set(mobil_details['merek'])
            self.edit_warna_var.set(mobil_details['warna'])
            
            self.edit_merek_var.trace('w', self.on_edit_merek_select)
            self.edit_warna_var.trace('w', self.on_edit_warna_select)
            
            self.hide_all_frames()
            self.edit_mobil_frame.pack()
        else:
            messagebox.showerror("Error", "Detail mobil tidak ditemukan.")


    def update_edit_options(self):
        merek_dict = self.data_manager.list_data('merek')
        warna_dict = self.data_manager.list_data('warna')
        
        self.edit_merek_option['menu'].delete(0, 'end')
        for id_merek, merek in merek_dict.items():
            self.edit_merek_option['menu'].add_command(label=merek, command=tk._setit(self.edit_merek_var, merek))
        
        self.edit_warna_option['menu'].delete(0, 'end')
        for id_warna, warna in warna_dict.items():
            self.edit_warna_option['menu'].add_command(label=warna, command=tk._setit(self.edit_warna_var, warna))


    def save_edit(self):
        new_value = self.edit_entry.get()
        if new_value.strip() == "":
            messagebox.showerror("Error", "Nilai baru tidak boleh kosong!")
        else:
            try:
                self.data_manager.edit_data(self.current_data_type, self.current_edit_id, new_value)
                self.update_listbox(self.current_data_type)
                messagebox.showinfo("Sukses", f"Data berhasil diubah menjadi: {new_value}")
                self.show_data()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def save_edit_mobil(self):
        nama_mobil = self.edit_nama_mobil_entry.get()
        if nama_mobil.strip() == "" or not hasattr(self, 'selected_edit_merek_id') or not hasattr(self, 'selected_edit_warna_id'):
            messagebox.showerror("Error", "Semua field harus diisi!")
        else:
            try:
                new_value = f"{nama_mobil}:{self.selected_edit_merek_id}:{self.selected_edit_warna_id}"
                self.data_manager.edit_data('mobil', self.current_edit_id, new_value)
                self.update_listbox('mobil')
                messagebox.showinfo("Sukses", f"Data mobil berhasil diubah!")
                self.show_data()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def on_merek_select(self, *args):
        selected_name = self.merek_var.get()
        self.selected_merek_id = next((id for id, name in self.data_manager.list_data('merek').items() if name == selected_name), None)

    def on_warna_select(self, *args):
        selected_name = self.warna_var.get()
        self.selected_warna_id = next((id for id, name in self.data_manager.list_data('warna').items() if name == selected_name), None)

    def on_edit_merek_select(self, *args):
        selected_name = self.edit_merek_var.get()
        self.selected_edit_merek_id = next((id for id, name in self.data_manager.list_data('merek').items() if name == selected_name), None)

    def on_edit_warna_select(self, *args):
        selected_name = self.edit_warna_var.get()
        self.selected_edit_warna_id = next((id for id, name in self.data_manager.list_data('warna').items() if name == selected_name), None)

    def show_transaksi(self):
        self.hide_all_frames()
        self.transaksi_frame.pack()
        self.update_mobil_options()

    def show_tambah_transaksi(self):
        self.hide_all_frames()
        self.tambah_transaksi_frame.pack()
        self.update_mobil_options()

    def show_transaksi_history(self):
        self.hide_all_frames()
        self.transaksi_history_frame.pack()
        self.update_transaksi_history()

    def update_transaksi_history(self):
        # Clear existing items
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        # Fetch and display transaction history
        transaksi_list = self.data_manager.list_data('transaksi')
        for transaksi_id, transaksi_data in transaksi_list.items():
            id_mobil, jarak, tanggal = transaksi_data.split('_')
            nama_mobil = self.data_manager.mobil.get_detail_mobil(id_mobil)['nama_mobil']
            self.history_tree.insert('', 'end', values=(tanggal, nama_mobil, jarak))
        self.update_total_jarak()

    def update_total_jarak(self):
        total_jarak = 0
        for item in self.history_tree.get_children():
            # Ambil nilai jarak dari kolom ketiga (indeks 2)
            jarak = float(self.history_tree.item(item)['values'][2])
            total_jarak += jarak
        
        # Update label total jarak
        self.total_jarak_label.config(text=f"Total Jarak: {total_jarak:.1f} km")

    def update_home_history(self):
        # Bersihkan data lama
        for item in self.home_history_tree.get_children():
            self.home_history_tree.delete(item)

        # Ambil data transaksi
        transaksi_list = self.data_manager.list_data('transaksi')
        
        # Urutkan transaksi berdasarkan tanggal (terbaru dulu)
        sorted_transaksi = []
        for transaksi_id, transaksi_data in transaksi_list.items():
            id_mobil, jarak, tanggal = transaksi_data.split('_')
            nama_mobil = self.data_manager.mobil.get_detail_mobil(id_mobil)['nama_mobil']
            sorted_transaksi.append((tanggal, nama_mobil, jarak))
        
        sorted_transaksi.sort(reverse=True)  # Urutkan berdasarkan tanggal terbaru
        
        # Tampilkan 5 transaksi terakhir
        for i, (tanggal, nama_mobil, jarak) in enumerate(sorted_transaksi):
            if i < 5:  # Hanya tampilkan 5 data terakhir
                self.home_history_tree.insert('', 'end', values=(tanggal, nama_mobil, jarak))

    def update_mobil_options(self):
        mobil_dict = self.data_manager.list_data('mobil')
        mobil_list = []
        self.mobil_id_map = {}  # untuk menyimpan pemetaan nama mobil ke ID

        for id_mobil, mobil_info in mobil_dict.items():
            nama_mobil = mobil_info.split(':')[0]  # Asumsikan format "nama_mobil:id_merek:id_warna"
            mobil_list.append(nama_mobil)
            self.mobil_id_map[nama_mobil] = id_mobil

        self.mobil_option['values'] = mobil_list

    def tambah_transaksi(self):
        nama_mobil = self.mobil_var.get()
        id_mobil = self.mobil_id_map.get(nama_mobil)  # Dapatkan ID mobil dari nama
        jarak = self.jarak_entry.get()
        tanggal = self.tanggal_entry.get_date()  # Mendapatkan tanggal dari DateEntry

        if not nama_mobil or not id_mobil or jarak.strip() == "":
            messagebox.showerror("Error", "Semua field harus diisi!")
        else:
            try:
                jarak = int(jarak)  # Memastikan jarak adalah integer
                tanggal_str = tanggal.strftime('%Y-%m-%d')
                transaksi_data = f"{id_mobil}_{jarak}_{tanggal_str}"
                self.data_manager.tambah_transaksi(transaksi_data)
                self.jarak_entry.delete(0, tk.END)
                self.tanggal_entry.set_date(datetime.now())  # Reset tanggal ke hari ini
                self.mobil_var.set('')
                messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan!")
                self.update_home_history()
            # Update detail mobil jika sedang ditampilkan
                if self.detail_frame.winfo_viewable():
                    self.show_mobil_detail()
            except ValueError:
                messagebox.showerror("Error", "Format jarak tidak valid! Pastikan jarak adalah angka.")

    def hide_all_frames(self):
        for frame in (self.home_frame, self.mobil_frame, self.warna_frame, 
                    self.merk_frame, self.warna_tambah_frame, 
                    self.merk_tambah_frame, self.mobil_tambah_frame, 
                    self.detail_frame, self.edit_frame, self.edit_mobil_frame, 
                    self.transaksi_frame, getattr(self, 'result_frame', None), self.transaksi_history_frame):
            if frame:
                frame.pack_forget()

    def hitung_total_jarak(self, id_mobil):
        total_jarak = 0
        transaksi_list = self.data_manager.list_data('transaksi')
        
        for transaksi_id, transaksi_data in transaksi_list.items():
            mobil_id, jarak, tanggal = transaksi_data.split('_')
            if mobil_id == id_mobil:
                total_jarak += int(jarak)
        
        return total_jarak

    def show_mobil_detail(self):
        listbox = self.mobil_frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            item_id = selected_item.split(":")[0].strip()
            details = self.data_manager.mobil.get_detail_mobil(item_id)
            if details:
                # Clear previous widgets in detail frame
                for widget in self.detail_frame.winfo_children():
                    widget.destroy()
                
                # Informasi dasar
                total_jarak = self.hitung_total_jarak(item_id)
                detail_text = (f"\nNama Mobil\t: {details['nama_mobil']}"
                            f"\nMerek\t\t: {details['merek']}"
                            f"\nWarna\t\t: {details['warna']}"
                            f"\nTotal Jarak\t: {total_jarak} km")
                
                detail_label = tk.Label(self.detail_frame, text=detail_text, justify="left")
                detail_label.pack(pady=10)
                
                # Tabel riwayat transaksi
                history_label = tk.Label(self.detail_frame, text="Riwayat Penggunaan:", font=("Helvetica", 10, "bold"))
                history_label.pack(pady=5)
                
                # Create Treeview
                detail_tree = ttk.Treeview(self.detail_frame, columns=('Tanggal', 'Jarak'), show='headings', height=5)
                detail_tree.heading('Tanggal', text='Tanggal')
                detail_tree.heading('Jarak', text='Jarak (km)')
                detail_tree.column('Tanggal', width=100)
                detail_tree.column('Jarak', width=100)
                detail_tree.pack(pady=5)
                
                # Populate treeview
                riwayat = self.get_riwayat_transaksi_mobil(item_id)
                for transaksi in riwayat:
                    detail_tree.insert('', 'end', values=(transaksi['tanggal'], transaksi['jarak']))
                
                # Back button
                back_button = tk.Button(self.detail_frame, text="Kembali", command=self.show_data)
                back_button.pack(pady=10)
                
                self.hide_all_frames()
                self.detail_frame.pack()
            else:
                messagebox.showerror("Error", "Detail mobil tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih mobil yang ingin dilihat detailnya.")

    def get_riwayat_transaksi_mobil(self, id_mobil):
        transaksi_list = self.data_manager.list_data('transaksi')
        riwayat = []
        
        for transaksi_id, transaksi_data in transaksi_list.items():
            mobil_id, jarak, tanggal = transaksi_data.split('_')
            if mobil_id == id_mobil:
                riwayat.append({
                    'tanggal': tanggal,
                    'jarak': int(jarak)
                })
        
        # Urutkan berdasarkan tanggal
        riwayat.sort(key=lambda x: x['tanggal'], reverse=True)
        return riwayat

    def apply_date_filter(self):
        start_date = self.start_date_filter.get_date()
        end_date = self.end_date_filter.get_date()
        
        # Validate dates
        if start_date > end_date:
            messagebox.showerror("Error", "Tanggal mulai tidak boleh lebih besar dari tanggal selesai!")
            return
        
        # Clear existing items
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        # Fetch and filter transaction history
        transaksi_list = self.data_manager.list_data('transaksi')
        filtered_transactions = []
        
        for transaksi_id, transaksi_data in transaksi_list.items():
            id_mobil, jarak, tanggal_str = transaksi_data.split('_')
            tanggal = datetime.strptime(tanggal_str, '%Y-%m-%d').date()
            
            if start_date <= tanggal <= end_date:
                nama_mobil = self.data_manager.mobil.get_detail_mobil(id_mobil)['nama_mobil']
                filtered_transactions.append((tanggal_str, nama_mobil, jarak))
        
        # Sort by date
        filtered_transactions.sort(reverse=True)
        
        # Display filtered results
        for tanggal, nama_mobil, jarak in filtered_transactions:
            self.history_tree.insert('', 'end', values=(tanggal, nama_mobil, jarak))

    def reset_date_filter(self):
        # Reset date entries to current date
        current_date = datetime.now()
        self.start_date_filter.set_date(current_date)
        self.end_date_filter.set_date(current_date)
        
        # Update the display with all transactions
        self.update_transaksi_history()

    def show_mobil_list(self, title, mobil_list):
        # Buat frame baru untuk menampilkan hasil
        self.result_frame = tk.Frame(self)
        
        # Label untuk judul
        result_title = tk.Label(self.result_frame, text=title, font=("Helvetica", 12, "bold"))
        result_title.pack(pady=10)

        # Listbox untuk menampilkan data mobil
        result_listbox = tk.Listbox(self.result_frame, width=40, height=10)
        result_listbox.pack(pady=5, padx=10)

        # Populate listbox dengan data mobil
        for id_mobil, nama_mobil in mobil_list:
            result_listbox.insert(tk.END, f"{id_mobil}: {nama_mobil}")

        # Tombol kembali
        back_button = tk.Button(self.result_frame, text="Kembali", command=self.show_data)
        back_button.pack(pady=10)

        # Sembunyikan frame lain dan tampilkan result_frame
        self.hide_all_frames()
        self.result_frame.pack()


    def show_mobil_by_warna(self):
        listbox = self.warna_frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            id_warna = selected_item.split(":")[0].strip()
            warna_name = selected_item.split(":")[1].strip()
            mobil_list = self.data_manager.get_mobil_by_warna(id_warna)
            self.show_mobil_list(f"Daftar Mobil dengan Warna {warna_name}", mobil_list)
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih warna terlebih dahulu.")

    def show_mobil_by_merek(self):
        listbox = self.merk_frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            id_merek = selected_item.split(":")[0].strip()
            merek_name = selected_item.split(":")[1].strip()
            mobil_list = self.data_manager.get_mobil_by_merek(id_merek)
            self.show_mobil_list(f"Daftar Mobil dengan Merek {merek_name}", mobil_list)
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih merek terlebih dahulu.")
if __name__ == "__main__":
    app = Application()
    app.mainloop()