class Tiket:
    def __init__(self, nama_film, jumlah_tiket, harga_tiket):
        self.nama_film = nama_film
        self.jumlah_tiket = jumlah_tiket
        self.harga_tiket = harga_tiket

    def total_harga(self):
        return self.jumlah_tiket * self.harga_tiket

class DataTiket:
    def __init__(self):
        self.tiket_list = []

    def tambah_tiket(self, tiket):
        self.tiket_list.append(tiket)

    def get_all_tiket(self):
        return self.tiket_list
