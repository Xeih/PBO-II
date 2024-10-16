import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas, ttk
from data_manager import DataManager
from datetime import datetime


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Mobil")
        self.geometry("400x400")
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

    def create_widgets(self):
        # Home frame widgets
        canvas = Canvas(self.home_frame, width=400, height=150, bg="#FFA559", highlightthickness=0)
        canvas.create_text(200, 75, text="DATA MOBIL", font=("Helvetica", 24, "bold"), fill="white")
        canvas.pack()

        frame = tk.Frame(self.home_frame)
        frame.pack(pady=20)

        button_mobil = tk.Button(frame, text="MOBIL", font=("Helvetica", 12), compound=tk.TOP, bg="green", fg="white", padx=20, pady=10, command=lambda: self.show_data('mobil'))
        button_mobil.grid(row=0, column=0, padx=20)

        button_merk = tk.Button(frame, text="MERK", font=("Helvetica", 12), compound=tk.TOP, bg="purple", fg="white", padx=20, pady=10, command=lambda: self.show_data('merek'))
        button_merk.grid(row=0, column=1, padx=20)

        button_warna = tk.Button(frame, text="WARNA", font=("Helvetica", 12), compound=tk.TOP, bg="red", fg="white", padx=20, pady=10, command=lambda: self.show_data('warna'))
        button_warna.grid(row=0, column=2, padx=20)

        frame = self.home_frame.winfo_children()[1]
        button_transaksi = tk.Button(frame, text="Transaksi", font=("IMPACT", 12), compound=tk.TOP, bg="blue", fg="white", padx=20, pady=10, command=self.show_transaksi)
        button_transaksi.grid(row=1, column=1, padx=20, pady=10)



        # Data frames (mobil, warna, merk)
        for frame, title in [(self.mobil_frame, "List Mobil"), (self.warna_frame, "List Warna"), (self.merk_frame, "List Merk")]:
            label = tk.Label(frame, text=title, font=("Helvetica", 16))
            label.pack(pady=10)
            
            listbox = tk.Listbox(frame, width=40, height=10)
            listbox.pack(pady=10)

            edit_button = tk.Button(frame, text="Edit", command=lambda f=frame: self.show_edit_dialog(f))
            edit_button.pack(side=tk.LEFT, padx=5, pady=5)

            if frame == self.mobil_frame:
                detail_button = tk.Button(frame, text="Tampilkan Detail", command=self.show_mobil_detail)
                detail_button.pack(pady=5)
                
            back_button = tk.Button(frame, text="Kembali", command=self.show_home)
            back_button.pack(pady=10)
            
            if frame == self.warna_frame:
                add_button = tk.Button(frame, text="+", command=self.show_tambah_warna)
                add_button.pack(side=tk.LEFT, padx=5, pady=5)
                
                delete_button = tk.Button(frame, text="-", command=lambda: self.delete_action('warna'))
                delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
                
            if frame == self.merk_frame:
                add_button = tk.Button(frame, text="+", command=self.show_tambah_merek)
                add_button.pack(side=tk.LEFT, padx=5, pady=5)
                
                delete_button = tk.Button(frame, text="-", command=lambda: self.delete_action('merek'))
                delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
                
            if frame == self.mobil_frame:
                add_button = tk.Button(frame, text="+", command=self.show_tambah_mobil)
                add_button.pack(side=tk.LEFT, padx=5, pady=5)
                
                delete_button = tk.Button(frame, text="-", command=lambda: self.delete_action('mobil'))
                delete_button.pack(side=tk.RIGHT, padx=5, pady=5)

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

        self.edit_frame = tk.Frame(self)
        label_edit = tk.Label(self.edit_frame, text="Edit Data", font=("Helvetica", 12))
        label_edit.pack(pady=5)
        
        self.edit_entry = tk.Entry(self.edit_frame, width=30)
        self.edit_entry.pack(pady=5)
        
        save_button = tk.Button(self.edit_frame, text="Simpan", command=self.save_edit)
        save_button.pack(pady=10)
        
        back_button = tk.Button(self.edit_frame, text="Kembali", command=self.show_data)
        back_button.pack(pady=10)

    def show_home(self):
        self.hide_all_frames()
        self.home_frame.pack()

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
        # Update options for merek dan warna in tambah mobil frame
        self.merek_option['menu'].delete(0, 'end')
        for id_merek, merek in self.data_manager.list_data('merek').items():
            self.merek_option['menu'].add_command(label=merek, command=tk._setit(self.merek_var, id_merek))
        
        self.warna_option['menu'].delete(0, 'end')
        for id_warna, warna in self.data_manager.list_data('warna').items():
            self.warna_option['menu'].add_command(label=warna, command=tk._setit(self.warna_var, id_warna))

    def tambah_warna(self):
        warna_baru = self.warna_entry.get()
        if warna_baru.strip() == "":
            messagebox.showerror("Error", "Warna tidak boleh kosong!")
        else:
            self.data_manager.tambah_warna(warna_baru)
            self.update_listbox('warna')
            self.warna_entry.delete(0, tk.END)
            messagebox.showinfo("Sukses", f"Warna {warna_baru} berhasil ditambahkan!")
    
    def tambah_merek(self):
        merek_baru = self.merek_entry.get()
        if merek_baru.strip() == "":
            messagebox.showerror("Error", "Merek tidak boleh kosong!")
        else:
            self.data_manager.tambah_merek(merek_baru)
            self.update_listbox('merek')
            self.merek_entry.delete(0, tk.END)
            messagebox.showinfo("Sukses", f"Merek {merek_baru} berhasil ditambahkan!")
    
    def tambah_mobil(self):
        nama_mobil = self.nama_mobil_entry.get()
        id_merek = self.merek_var.get()
        id_warna = self.warna_var.get()
        if nama_mobil.strip() == "" or id_merek.strip() == "" or id_warna.strip() == "":
            messagebox.showerror("Error", "Nama mobil, merek, dan warna tidak boleh kosong!")
        else:
            try:
                result = self.data_manager.tambah_mobil(nama_mobil, id_merek, id_warna)
                self.update_listbox('mobil')
                self.nama_mobil_entry.delete(0, tk.END)
                self.merek_var.set('')
                self.warna_var.set('')
                messagebox.showinfo("Sukses", f"Mobil berhasil ditambahkan: {result}")
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
        no_button.pack(side=tk.RIGHT, padx=20, pady=20)

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

    def show_detail(self, event):
        listbox = event.widget
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            item_id = selected_item.split(":")[0].strip()
            details = self.data_manager.mobil.get_detail_mobil(item_id)
            if details:
                detail_text = f"Nama Mobil: {details['nama_mobil']}\nMerek: {details['merek']}\nWarna: {details['warna']}"
                self.detail_label.config(text=detail_text)
                self.hide_all_frames()
                self.detail_frame.pack()
            else:
                messagebox.showerror("Error", "Detail mobil tidak ditemukan.")

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
            self.edit_entry.delete(0, tk.END)
            self.edit_entry.insert(0, item_value)
            
            self.hide_all_frames()
            self.edit_frame.pack()
        else:
            messagebox.showwarning("Peringatan", f"Silakan pilih item yang ingin diedit.")

    def update_edit_options(self):
        merek_dict = self.data_manager.list_data('merek')
        warna_dict = self.data_manager.list_data('warna')
        
        self.edit_merek_option['menu'].delete(0, 'end')
        for id_merek, merek in merek_dict.items():
            self.edit_merek_option['menu'].add_command(label=merek, command=tk._setit(self.edit_merek_var, merek))
        
        self.edit_warna_option['menu'].delete(0, 'end')
        for id_warna, warna in warna_dict.items():
            self.edit_warna_option['menu'].add_command(label=warna, command=tk._setit(self.edit_warna_var, warna))

    def on_merk_select(self, *args):
        selected_name = self.warna_var.get()
        self.selected_merek_id = next((id for id, name in self.data_manager.list_data('merek').items() if name == selected_name), None)

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

    def hide_all_frames(self):
        for frame in (self.home_frame, self.mobil_frame, self.warna_frame, self.merk_frame, 
                      self.warna_tambah_frame, self.merk_tambah_frame, self.mobil_tambah_frame, 
                      self.detail_frame, self.edit_frame):
            frame.pack_forget()

    def show_mobil_detail(self):
        listbox = self.mobil_frame.winfo_children()[1]
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = listbox.get(index)
            item_id = selected_item.split(":")[0].strip()
            details = self.data_manager.mobil.get_detail_mobil(item_id)
            if details:
                detail_text = f"Nama Mobil: {details['nama_mobil']}\nMerek: {details['merek']}\nWarna: {details['warna']}"
                self.detail_label.config(text=detail_text)
                self.hide_all_frames()
                self.detail_frame.pack()
            else:
                messagebox.showerror("Error", "Detail mobil tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih mobil yang ingin dilihat detailnya.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
