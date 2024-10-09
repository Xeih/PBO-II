import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from data_manager import DataManager


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

    def create_widgets(self):
        # Home frame widgets
        canvas = Canvas(self.home_frame, width=500, height=150, bg="#FFA559", highlightthickness=0)
        canvas.create_text(250, 75, text="DATA MOBIL", font=("impact", 24), fill="white")
        canvas.pack()

        frame = tk.Frame(self.home_frame)
        frame.pack(pady=20)

        button_mobil = tk.Button(frame, text="Mobil", font=("arial", 16, 'bold'), compound=tk.TOP, bg="green", fg="white", padx=20, pady=10, command=lambda: self.show_data('mobil'))
        button_mobil.grid(row=0, column=0, padx=20)

        button_merk = tk.Button(frame, text="Merk", font=("arial", 16, 'bold'), compound=tk.TOP, bg="purple", fg="white", padx=20, pady=10, command=lambda: self.show_data('merek'))
        button_merk.grid(row=0, column=1, padx=20)

        button_warna = tk.Button(frame, text="Warna", font=("arial", 16, 'bold'), compound=tk.TOP, bg="red", fg="white", padx=20, pady=10, command=lambda: self.show_data('warna'))
        button_warna.grid(row=0, column=2, padx=20)

        # Data frames (mobil, warna, merk)
        for frame, title in [(self.mobil_frame, "List Mobil"), (self.warna_frame, "List Warna"), (self.merk_frame, "List Merk")]:
            label = tk.Label(frame, text=title,font=("impact", 16))
            label.pack(pady=10)
            
            listbox = tk.Listbox(frame, width=40, height=10)
            listbox.pack(pady=10)
            
            back_button = tk.Button(frame, text="Kembali", command=self.show_home)
            back_button.pack(pady=15)
            
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

    def show_home(self):
        self.hide_all_frames()
        self.home_frame.pack()

    def show_data(self, data_type):
        self.hide_all_frames()
        self.current_data_type = data_type
        if data_type == 'mobil':
            frame = self.mobil_frame
        elif data_type == 'warna':
            frame = self.warna_frame
        elif data_type == 'merek':
            frame = self.merk_frame
        frame.pack()
        self.update_listbox(data_type)

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
        for frame in (self.home_frame, self.mobil_frame, self.warna_frame, self.merk_frame, self.warna_tambah_frame, self.merk_tambah_frame, self.mobil_tambah_frame):
            frame.pack_forget()

    def update_listbox(self, data_type):
        listbox = self.warna_frame.winfo_children()[1] if data_type == 'warna' else \
                  self.merk_frame.winfo_children()[1] if data_type == 'merek' else \
                  self.mobil_frame.winfo_children()[1]
        
        listbox.delete(0, tk.END)
        data_dict = self.data_manager.list_data(data_type)
        for key, value in data_dict.items():
            listbox.insert(tk.END, f"{key}: {value}")

    def update_options(self):
        # Update options for merek and warna in tambah mobil frame
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
        id_merek = self.merek_var.get()
        id_warna = self.warna_var.get()
        if id_merek.strip() == "" or id_warna.strip() == "":
            messagebox.showerror("Error", "Merek dan Warna tidak boleh kosong!")
        else:
            try:
                result = self.data_manager.mobil.tambah_mobil(id_merek, id_warna)
                self.update_listbox('mobil')
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
        
        yes_button = tk.Button(confirm_window, text="Yes", bg="green", fg="white", command=lambda: self.delete_item(confirm_window, data_type, item_id, item_name))
        yes_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        no_button = tk.Button(confirm_window, text="No", bg="red", fg="white", command=confirm_window.destroy)
        no_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def delete_item(self, confirm_window, data_type, item_id, item_name):
        if self.data_manager.delete_data(data_type, item_id):
            confirm_window.destroy()
            self.update_listbox(data_type)
            messagebox.showinfo("Sukses", f"{data_type.capitalize()} {item_name} berhasil dihapus!")
        else:
            messagebox.showerror("Error", f"Gagal menghapus {data_type} {item_name}.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
