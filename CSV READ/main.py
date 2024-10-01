from fungsi import baca_file, parse_array, parse_dictionary, hapus_data
#saya aslinya tiga

def main():
    # Muat data dari file saat aplikasi dimulai
    while True:
        print("\n==== Menu Utama ====")
        print("1. Lihat Data")
        print("2. Hapus Data")
        print("3. Tutup Aplikasi")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            print("1. Lihat Data Warna")
            print("2. Lihat Data Merek")
            print("3. Lihat Data Mobil")
            pilihan = input("Pilihan : ")
            if pilihan == '1':
                isi = baca_file(nama_file="data_warna.txt")
                data_dict = parse_dictionary(isi)
                print("\nData yang dibaca adalah Dictionary:")
                print(data_dict)
            elif pilihan == '2':
                isi = baca_file(nama_file="data_merek.txt")
                data_dict = parse_dictionary(isi)
                print("\nData yang dibaca adalah Dictionary:")
                print(data_dict)
            elif pilihan == '3':
                isi = baca_file(nama_file="data_mobil.txt")
                data_dict = parse_dictionary(isi)
                print("\nData yang dibaca adalah Dictionary:")
                print(data_dict)   
            
        elif pilihan == '2':
            print("Pilih File yang ingin di hapus : ")
            print("1. Data Warna")
            print("2. Data Merek")
            print("3. Data Mobil")
            pilihan = input("Pilihan : ")
            if pilihan == '1':
                hapus_data(nama_file="data_warna.txt")
                 
            elif pilihan == '2':
                hapus_data(nama_file="data_merek.txt")

            elif pilihan == '3':
                hapus_data(nama_file="data_mobil.txt")  


        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()