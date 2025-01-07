class InputForm:
    @staticmethod
    def input_tiket():
        try:
            nama_film = input("Masukkan nama film: ").strip()
            jumlah_tiket = int(input("Masukkan jumlah tiket: "))
            if jumlah_tiket <= 0:
                raise ValueError("Jumlah tiket harus lebih dari 0.")
            harga_tiket = int(input("Masukkan harga tiket: "))
            if harga_tiket <= 0:
                raise ValueError("Harga tiket harus lebih dari 0.")
            return nama_film, jumlah_tiket, harga_tiket
        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None
