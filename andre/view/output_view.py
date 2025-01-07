class OutputView:
    @staticmethod
    def tampilkan_tiket(tiket_list):
        if not tiket_list:
            print("Belum ada data tiket.")
            return
        print(f"{'No':<5}{'Nama Film':<20}{'Jumlah Tiket':<15}{'Harga Tiket':<15}{'Total Harga':<15}")
        print("-" * 70)
        for i, tiket in enumerate(tiket_list, start=1):
            print(f"{i:<5}{tiket.nama_film:<20}{tiket.jumlah_tiket:<15}{tiket.harga_tiket:<15}{tiket.total_harga():<15}")

