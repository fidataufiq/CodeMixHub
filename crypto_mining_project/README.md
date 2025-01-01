# Blockchain Sederhana 🚀

Blockchain adalah teknologi yang super keren, terkenal dengan sifatnya yang aman, transparan, dan nggak bisa dimanipulasi. Teknologi ini nggak cuma jadi pondasi buat kripto kayak Bitcoin, tapi juga membuka peluang baru di bidang keuangan, logistik, kontrak pintar, dan bahkan buat bikin kamu keliatan pintar (hehe). Tapi serius, banyak yang ngerasa memahami cara kerja blockchain itu ribet, apalagi buat pemula.

Proyek **Blockchain Sederhana** ini hadir buat kamu yang pengen ngerti blockchain tapi nggak pengen kepala pusing. Di sini, kamu bisa nyobain simulasi blockchain dasar. Kamu bisa tambahin transaksi, nambang blok (tenang, nggak pake cangkul kok), dan bahkan nyobain kontrak pintar! Proyek ini pakai Python sebagai otaknya, Flask buat servernya, dan HTML/CSS/JavaScript buat tampilannya.

## Apa itu Blockchain? 🤔

Blockchain itu ibarat buku catatan digital yang nggak bisa diedit sembarangan. Setiap "halaman" atau blok di buku ini berisi:

- **Data**: Misalnya, transaksi kayak "Si A kirim 10 koin ke Si B."
- **Hash**: Semacam "sidik jari" digital buat ngenalin blok.
- **Previous Hash**: Hash dari blok sebelumnya supaya semua tetap nyambung kayak gerbong kereta.

Kalau ada yang ngubah data di blok, hash-nya langsung beda. Jadi, blok yang rusak gampang ketahuan. Aman banget kan? 🔒

## Apa itu Mining? 🛠️

Mining itu proses nambahin blok baru ke blockchain. Tapi ini nggak semudah klik tombol "Tambah Blok". Ada tantangan yang disebut **Proof of Work (PoW)**:

- Komputer (atau program) bakal coba angka acak (_nonce_) sampai hash blok memenuhi syarat tertentu, misalnya harus dimulai dengan "0000" (ini disebut _difficulty_ atau tingkat kesulitan).
- Kalau hash-nya cocok, blok dianggap valid dan bisa dimasukin ke rantai.

Bayangin aja, mining itu kayak main puzzle, tapi hadiahnya bukan cuma rasa puas, tapi juga blok baru di blockchain. 😎

## Penjelasan Kode

### 1. File `blockchain.py`

- **Membuat Blok**:
  Setiap blok itu kayak kotak penyimpanan. Di dalamnya ada transaksi, hash, dan nomor urut (_index_). Blok pertama disebut _genesis block_ (blok awal alias "nenek moyang" blok 😂).

- **Mining Blok**:
  Program terus coba angka acak (_nonce_) sampai hash-nya cocok sama syarat (_difficulty_). Semakin tinggi kesulitannya, makin lama prosesnya. Jadi jangan heran kalau laptop mulai panas! 🔥

- **Menjaga Keamanan Rantai**:
  Blockchain ini bakal cek apakah:
  - Hash tiap blok sesuai sama datanya.
  - Hash blok sebelumnya cocok sama data di blok berikutnya.

### 2. File `node.py`

Ini kayak pelayan restoran yang nyambungin pengguna dengan blockchain:

- Kamu bisa:

  - Lihat rantai blok di browser (kayak ngintip buku besar digital).
  - Tambahin transaksi (misalnya, "Jovan kirim 10 coin ke Luna").
  - Nambang blok baru buat masukin transaksi ke blockchain.

- Semua ini dilakukan via antarmuka web yang gampang banget dipake. 😉

### 3. File HTML dan CSS

Halaman webnya lengkap dengan:

- Tampilan rantai blok dalam bentuk JSON.
- Formulir buat tambahin transaksi.
- Grafik transaksi per blok buat visualisasi yang mantap! 📊

### 4. Kontrak Pintar (Smart Contract) 🧠

Ini semacam aturan otomatis. Misalnya:

- **Aturan**: Kalau ada lebih dari 10 transaksi dalam satu blok, cetak "Blok ini penuh, bro!".
- Program bakal jalankan aturan ini tiap kali blok baru dibuat. Mantap, kan? 😄

## Contoh Cara Kerja 🚀

1. Kamu tambahin transaksi:
   - "Jovan kirim 10 coin ke Luna."
2. Transaksi masuk antrean (belum dimasukin ke blok).
3. Kamu mining blok:
   - Program coba angka acak sampai hash blok sesuai syarat.
   - Transaksi dalam antrean dimasukin ke blok yang berhasil dimining.
4. Blok baru ditambahin ke rantai. Sekarang, blockchain mencatat kalau Jovan udah kirim 10 coin ke Luna. Hore! 🎉

## Kenapa Mining Dibuat Sulit? 🤔

Supaya nggak sembarang orang bisa nambah blok dengan gampang. Proses mining ini bikin blockchain lebih aman dan nggak gampang dimanipulasi. Jadi, nggak ada tuh yang bisa asal nyontek "sidik jari" blok. 😉

## Kesimpulan

- Blockchain ini kayak buku besar digital yang aman dan keren banget.
- Mining itu kayak main game puzzle buat validasi blok baru.
- Dengan proyek ini, kamu bisa lihat langsung cara kerja blockchain, dari A sampai Z! 🎮

Cobain, deh! Siapa tau kamu jadi suka sama blockchain (dan dapet inspirasi bikin startup!). 😎✨
