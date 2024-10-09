import tkinter as tk
from tkinter import Canvas
from fungsi import Warna, Merek, Mobil
from tkinter import messagebox

warna = Warna()
merek = Merek()
mobil = Mobil()
    
#Fungsi untuk menampilkan halaman utama
def show_home():
    hide_all_frames()  # Sembunyikan semua frame
    home_frame.pack()  # Tampilkan frame halaman utama

#Fungsi untuk menampilkan list mobil
def show_mobil():
    hide_all_frames()  # Sembunyikan semua frame
    mobil_frame.pack()  # Tampilkan frame mobil

#Fungsi untuk menampilkan list warna
def show_warna():
    hide_all_frames()  # Sembunyikan semua frame
    warna_frame.pack()  # Tampilkan frame warna



#Fungsi untuk menampilkan list merk
def show_merk():
    hide_all_frames()  # Hide all frames first
    merk_frame.pack()

def show_tambah_warna():
    hide_all_frames()
    warna_tambah_frame.pack()



#Fungsi untuk memperbarui Listbox
def update_listbox():
    list_data.delete(0, tk.END)  # Hapus semua item sebelumnya
    warna_dict = warna.list_warna()  # Mengambil dictionary warna
    for key, value in warna_dict.items():
        list_data.insert(tk.END, f"{key}: {value}")  # Masukkan data dalam format 'key: value'

def tambah_warna():
    warna_baru = warna_entry.get()  # Ambil input dari entry
    if warna_baru.strip() == "":  # Jika input kosong
        messagebox.showerror("Error", "Warna tidak boleh kosong!")
    else:
        warna.tambah_warna(warna_baru)  # Tambah warna menggunakan metode di class
        update_listbox()  # Perbarui Listbox setelah menambah data
        warna_entry.delete(0, tk.END)  # Hapus teks dari entry setelah menambah

#def load_data_to_list(filename):
    #try:
        #with open(filename, 'r') as file:
            #lines = file.readlines()
            #for line in lines[1:]:
                # Mengabaikan baris header (jika ada)
                #if line.strip() and "ID_WARNA"and"ID_MEREK"and'ID_MOBIL' not in line:
                    #list_data.insert(tk.END, line.strip())
    #except FileNotFoundError:
        #list_data.insert(tk.END, "File tidak ditemukan.")        

#Fungsi untuk menyembunyikan semua frame
def hide_all_frames():
    home_frame.pack_forget()
    mobil_frame.pack_forget()
    warna_frame.pack_forget()
    merk_frame.pack_forget()
    warna_tambah_frame.pack_forget()




    
    


#Inisialisasi jendela utama
root = tk.Tk()
root.title("Data Mobil")
root.geometry("400x400")

#Membuat frame untuk halaman utama
home_frame = tk.Frame(root)

#Membuat canvas untuk header atas di halaman utama
canvas = Canvas(home_frame, width=400, height=150, bg="#FFA559", highlightthickness=0)
canvas.create_text(200, 75, text="DATA MOBIL", font=("Helvetica", 24, "bold"), fill="white")
canvas.pack()

#Membuat frame untuk menampung tombol-tombol di halaman utama
frame = tk.Frame(home_frame)
frame.pack(pady=20)

#Membuat tombol-tombol di halaman utama
button_mobil = tk.Button(frame, text="Mobil", font=("Helvetica", 12), compound=tk.TOP, bg="green", fg="white", padx=20, pady=10, command=show_mobil)
button_mobil.grid(row=0, column=0, padx=20)

button_merk = tk.Button(frame, text="Merk", font=("Helvetica", 12), compound=tk.TOP, bg="purple", fg="white", padx=20, pady=10, command=show_merk)
button_merk.grid(row=0, column=1, padx=20)

button_warna = tk.Button(frame, text="WARNA", font=("Helvetica", 12), compound=tk.TOP, bg="red", fg="white", padx=20, pady=10, command=show_warna)
button_warna.grid(row=0, column=2, padx=20)


#Frame untuk list mobil
mobil_frame = tk.Frame(root)
label_mobil = tk.Label(mobil_frame, text="List Mobil", font=("Helvetica", 16))
label_mobil.pack(pady=10)
list_data = tk.Listbox(mobil_frame)

mobil_dict = mobil.list_mobil()  # Mengambil dictionary
#Masukkan data ke dalam Listbox dalam format 'key: value'
for key, value in mobil_dict.items():
    list_data.insert(tk.END, f"{key}: {value}")

#filename = 'data_mobil.txt'  # Ganti dengan path file txt kamu jika berbeda
#load_data_to_list(filename)
list_data.pack(pady=10)
button_back_mobil = tk.Button(mobil_frame, text="Kembali", command=show_home)
button_back_mobil.pack(pady=10)
button_tambah_mobil = tk.Button(mobil_frame, text ="+", command = show_home)
button_tambah_mobil.pack(pady=10)


#Frame untuk list warna
warna_frame = tk.Frame(root)
label_warna = tk.Label(warna_frame, text="List Warna", font=("Helvetica", 16))
label_warna.pack(pady=10)
list_data = tk.Listbox(warna_frame)

warna_dict = warna.list_warna()  # Mengambil dictionary
#Masukkan data ke dalam Listbox dalam format 'key: value'
for key, value in warna_dict.items():
    list_data.insert(tk.END, f"{key}: {value}")
#filename = 'data_warna.txt'  # Ganti dengan path file txt kamu jika berbeda
#load_data_to_list(filename)
list_data.pack(pady=10)
button_back_warna = tk.Button(warna_frame, text="Kembali", command=show_home)
button_back_warna.pack(pady=10)
button_tambah_warna = tk.Button(warna_frame, text ="+", command = show_tambah_warna)
button_tambah_warna.pack(pady=10)

#Frame Tambah Warna

warna_tambah_frame = tk.Frame(root)
label_warna = tk.Label(warna_tambah_frame, text="List Warna", font=("Helvetica", 16))
label_warna.pack(pady=10)
list_data = tk.Listbox(warna_tambah_frame, width=40, height=10)
# Pertama kali panggil untuk menampilkan data yang ada
update_listbox()

list_data.pack(pady=10)

#Entry field untuk memasukkan warna baru
label_tambah = tk.Label(warna_tambah_frame, text="Tambah Warna Baru", font=("Helvetica", 12))
label_tambah.pack(pady=5)
warna_entry = tk.Entry(warna_tambah_frame, width=30)
warna_entry.pack(pady=5)

#Tombol untuk menambah warna baru
button_tambah_warna = tk.Button(warna_tambah_frame, text="Tambah Warna", command=tambah_warna)
button_tambah_warna.pack(pady=10)

#Tombol kembali untuk kembali ke halaman utama
button_back_warna = tk.Button(warna_tambah_frame, text="Kembali", command=show_home)
button_back_warna.pack(pady=10)

#Frame untuk list merk
merk_frame = tk.Frame(root)
label_merk = tk.Label(merk_frame, text="List Merk", font=("Helvetica", 16))
label_merk.pack(pady=10)
list_data = tk.Listbox(merk_frame)

merek_dict = merek.list_merek()  # Mengambil dictionary
#Masukkan data ke dalam Listbox dalam format 'key: value'
for key, value in merek_dict.items():
    list_data.insert(tk.END, f"{key}: {value}")

#filename = 'data_merek.txt'  # Ganti dengan path file txt kamu jika berbeda
#load_data_to_list(filename)
list_data.pack(pady=10)
button_back_merk = tk.Button(merk_frame, text="Kembali", command=show_home)
button_back_merk.pack(pady=10)

#Tampilkan halaman utama saat program dimulai
show_home()

#Jalankan aplikasi
root.mainloop()