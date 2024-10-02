from fungsi import baca_file, parse_array, tambah_data, data_mobil,  parse_dictionary, hapus_data


def main():
    # Muat data dari file saat aplikasi dimulai
    while True:
        print("\n==== Menu Utama ====")
        print("1. Lihat Data")
        print("2. Tambah warna dan Merk")
        print("3. Hapus Data")
        print("4. Buat Data Mobil")
        print("5. Keluar Aplikasi")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

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
            print("Pilih File yang ingin di tambah : ")
            print("1. Data Warna")
            print("2. Data Merek")
            pilihan = input("Pilihan : ")
            if pilihan == '1':
                tambah_data(nama_file="data_warna.txt")
                 
            elif pilihan == '2':
                tambah_data(nama_file="data_merek.txt")   


        elif pilihan == '3':
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

        elif pilihan == '4':
            print("Buat Mobil: ")  
            data_mobil()

        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi!") 
            break


        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()