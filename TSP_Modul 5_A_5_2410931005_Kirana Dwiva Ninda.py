class Produk:
    def __init__(self, jenis, harga, warna, stok):
        self.jenis = jenis
        self.harga = harga
        self.warna = warna
        self.stok = stok

    def __str__(self):
        return (f"Jenis buku: {self.jenis}, Harga: {self.harga}, Warna: {self.warna}, Stok: {self.stok}")

class TokoBuku:
    def __init__(self):
        self.produk_list = []

    def tampilkan_produk(self):
        if not self.produk_list:
            print("Belum ada produk tersedia.")
        else:
            print("\nDaftar Produk:")
            for produk in self.produk_list:
                print(produk)

    def tambah_produk(self, buku):
        print("\nProduk berhasil ditambahkan!")
        print("\nSebelum penambahan:")
        self.tampilkan_produk()
        self.produk_list.append(buku)
        print("\nSetelah penambahan:")
        self.tampilkan_produk()

    def hapus_produk(self, jenis):
        print("\nSebelum penghapusan:")
        self.tampilkan_produk()
        for produk in self.produk_list:
            if produk.jenis.lower() == jenis.lower():
                self.produk_list.remove(produk)
                print(f"\nProduk berhasil dihapus.")
                print("Setelah penghapusan:")
                self.tampilkan_produk()
                return
        print(f"\nProduk '{jenis}' tidak ditemukan.")

    def cari(self, ketentuan):
        ditemukan = [produk for produk in self.produk_list if produk.jenis.lower() == ketentuan.lower()]
        if ditemukan:
            print("\nBuku yang ditemukan:")
            for produk in ditemukan:
                print(produk)
        else:
            print(f"\nTidak ditemukan buku dengan kriteria '{ketentuan}'.")

def menu(toko):
    while True:
        print("\nMENU TOKO BUKU")
        print("1. Tampilkan daftar produk")
        print("2. Tambahkan produk")
        print("3. Hapus produk")
        print("4. Cari Produk")
        print("5. Keluar")
        pilihan = input("Masukkan menu 1-5: ")

        if pilihan == "1":
            toko.tampilkan_produk()
        elif pilihan == "2":
            buku_baru = input("Masukkan jenis buku: ")
            harga = input("Masukkan harga buku: ")
            warna = input("Masukkan warna sampul: ")
            stok = input("Masukkan jumlah stok: ")
            produk_baru = Produk(buku_baru, int(harga), warna, int(stok))
            toko.tambah_produk(produk_baru)
        elif pilihan == "3":
            hapus_buku = input("Masukkan jenis buku yang akan dihapus: ")
            toko.hapus_produk(hapus_buku)
        elif pilihan == "4":
            cari_buku = input("Masukkan jenis buku yang dicari: ")
            toko.cari(cari_buku)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    toko = TokoBuku()
    buku_awal = [
        Produk("novel", 75000, "putih", 10),
        Produk("pendidikan", 50000, "putih", 15),
        Produk("biografi", 35000, "kuning", 20)
    ]

    for buku in buku_awal:
        toko.produk_list.append(buku)

    print("Daftar produk sebelum perubahan :")
    toko.tampilkan_produk()

    menu(toko)