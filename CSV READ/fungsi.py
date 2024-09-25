def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

def parse_array(data):
    # Coba pisahkan berdasarkan koma
    if ',' in data:
        array = [item.strip() for item in data.split(',')]
    else:
        # Pisahkan berdasarkan baris baru
        array = [item.strip() for item in data.splitlines() if item.strip()]
    return array

def parse_dictionary(data):
    dict_result = {}
    
    if '=>' in data:
        pairs = data.split(',')
    elif ':' in data:
        pairs = data.split(';')
    else:
        pairs = []
    
    for pair in pairs:
        if '=>' in pair:
            key, value = pair.split('=>')
        elif ':' in pair:
            key, value = pair.split(':')
        else:
            continue
        dict_result[key.strip()] = value.strip()
    return dict_result

def main():
    while True:
        nama_file = input("Masukkan nama file txt/csv: ")
        isi_file = baca_file(nama_file)
        if isi_file is not None:
            # Menangani data sebagai array
            data_array = parse_array(isi_file)
            print("\nData yang dibaca adalah Array:")
            print(data_array)
        else:
            print(f"File '{nama_file}' tidak ditemukan. Coba lagi.\n")
        
        # Tanyakan apakah ingin memasukkan file lain
        pilihan = input("\nApakah Anda ingin memasukkan file lain? (y/n): ").lower()
        if pilihan != 'y':
            print("Terima kasih telah menggunakan aplikasi!")
            break

if __name__ == "__main__":
    main()
