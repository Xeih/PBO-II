def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

def main():
    nama_file = input("Masukkan nama file (termasuk ekstensi, misal data.txt): ")
    isi_file = baca_file(nama_file)
    
    if isi_file is not None:
        print("\nIsi file:")
        print(isi_file)
    else:
        print(f"File '{nama_file}' tidak ditemukan.")

if __name__ == "__main__":
    main()
