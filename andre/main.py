import sys
sys.path.append('C:/Andre/andre/andre')  # Sesuaikan dengan jalur direktori proyek Anda
from data.tiket import Tiket, DataTiket
from view.input_form import InputForm
from view.output_view import OutputView

def main():
    data_tiket = DataTiket()
    while True:
        print("\n=== Sistem Tiket Bioskop ===")
        print("1. Tambah Tiket")
        print("2. Tampilkan Tiket")
        print("3. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            input_data = InputForm.input_tiket()
            if input_data:
                nama_film, jumlah_tiket, harga_tiket = input_data
                tiket = Tiket(nama_film, jumlah_tiket, harga_tiket)
                data_tiket.tambah_tiket(tiket)
                print("Data tiket berhasil ditambahkan!")
        elif pilihan == "2":
            OutputView.tampilkan_tiket(data_tiket.get_all_tiket())
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
