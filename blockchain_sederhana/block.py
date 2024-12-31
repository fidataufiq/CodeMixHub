import hashlib
import time

class Blok:
    def __init__(self, indeks, waktu, transaksi, hash_sebelumnya):
        self.indeks = indeks
        self.waktu = waktu
        self.transaksi = transaksi
        self.hash_sebelumnya = hash_sebelumnya
        self.nonce = 0  #menemukan hash yang valid
        self.hash = self.hitung_hash()

    def hitung_hash(self):
        """Menghasilkan hash SHA-256 untuk blok."""
        string_blok = f"{self.indeks}{self.waktu}{self.transaksi}{self.hash_sebelumnya}{self.nonce}"
        return hashlib.sha256(string_blok.encode()).hexdigest()

class RantaiBlok:
    def __init__(self):
        self.rantai = []
        self.kesulitan = 2  # Jumlah angka nol di depan hash
        self.buat_blok_genesis()

    def buat_blok_genesis(self):
        """Membuat blok pertama (genesis) dalam rantai."""
        blok_genesis = Blok(0, time.time(), [], "0")
        self.rantai.append(blok_genesis)

    def ambil_blok_terakhir(self):
        return self.rantai[-1]

    def tambah_blok(self, transaksi):
        """Menambahkan blok baru ke rantai setelah mining."""
        blok_terakhir = self.ambil_blok_terakhir()
        blok_baru = Blok(len(self.rantai), time.time(), transaksi, blok_terakhir.hash)
        blok_baru = self.mining_blok(blok_baru)
        self.rantai.append(blok_baru)

    def mining_blok(self, blok):
        """Mensimulasikan mining dengan mencari hash yang valid."""
        print(f"Sedang mining blok {blok.indeks}...")
        while not blok.hash.startswith('0' * self.kesulitan):
            blok.nonce += 1
            blok.hash = blok.hitung_hash()
        print(f"Blok {blok.indeks} berhasil dimining dengan hash: {blok.hash}")
        return blok

    def validasi_rantai(self):
        """Memeriksa validitas rantai blok."""
        for i in range(1, len(self.rantai)):
            blok_sekarang = self.rantai[i]
            blok_sebelumnya = self.rantai[i - 1]

            if blok_sekarang.hash != blok_sekarang.hitung_hash():
                return False

            if blok_sekarang.hash_sebelumnya != blok_sebelumnya.hash:
                return False

        return True

    def ubah_blok(self, indeks, transaksi_palsu):
        """Mensimulasikan manipulasi data dalam blok."""
        if 0 < indeks < len(self.rantai):
            self.rantai[indeks].transaksi = [transaksi_palsu]
            print(f"Blok {indeks} telah dimanipulasi!")
        else:
            print("Indeks blok tidak valid. Blok genesis tidak dapat dimanipulasi.")

# Program utama
if __name__ == "__main__":
    rantai_blok = RantaiBlok()

    while True:
        print("\n1. Tambah transaksi baru")
        print("2. Tampilkan rantai blok")
        print("3. Validasi rantai blok")
        print("4. Manipulasi blok")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            pengirim = input("Masukkan nama pengirim: ")
            penerima = input("Masukkan nama penerima: ")
            jumlah = input("Masukkan jumlah: ")
            transaksi = {"pengirim": pengirim, "penerima": penerima, "jumlah": jumlah}
            rantai_blok.tambah_blok([transaksi])

        elif pilihan == "2":
            print("\nRantai Blok:")
            for blok in rantai_blok.rantai:
                print(f"Indeks: {blok.indeks}")
                print(f"Waktu: {time.ctime(blok.waktu)}")
                print(f"Transaksi: {blok.transaksi}")
                print(f"Hash: {blok.hash}")
                print(f"Hash Sebelumnya: {blok.hash_sebelumnya}\n")

        elif pilihan == "3":
            valid = rantai_blok.validasi_rantai()
            print(f"Rantai blok valid: {valid}")

        elif pilihan == "4":
            indeks = int(input("Masukkan indeks blok yang akan dimanipulasi: "))
            transaksi_palsu = {"pengirim": "Palsu", "penerima": "Hacker", "jumlah": "999999"}
            rantai_blok.ubah_blok(indeks, transaksi_palsu)

        elif pilihan == "5":
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
