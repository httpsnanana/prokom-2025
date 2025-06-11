data_pemain = [
    ["Vinicius Junior", 24, 3, 3476.33],
    ["Rodrygo", 24, 4, 1738.16],
    ["Arda Guler", 19, 5, 782.17],
    ["Brahim Diaz", 25, 3, 608.36],
    ["Kylian Mbappe", 26, 5, 2781.06]
]

while True :
    print("\n==Menu Utama==")
    print("1. Tampilkan Data Pemain")
    print("2. Hapus Data")
    print("3. Tambah Data")
    print("4. Ubah Data")
    pilihan = int(input("Input menu pilihan (1/2/3/4) = "))

    if pilihan == 1 :
        print("\nData Pemain = ")
        for data in data_pemain :
            print(f"nama : {data[0]}, umur : {data[1]}, kontrak : {data[2]}, nilai : {data[3]}")

    elif pilihan == 2 :
        hapus_data = input("Silahkan input data yang akan dihapus = ")
        for data in data_pemain :
            if data[0].lower() == hapus_data.lower() :
                data_pemain.remove(data)
                print(f"Data {hapus_data} berhasil dihapus")
                break

    elif pilihan == 3 :
        tambah_nama = input("Silahkan input nama data yang akan ditambah = ")
        tambah_usia = int(input("Silahkan input usia pemain = "))
        tambah_kontrak = int(input("Silahkan input lama kontrak = "))
        tambah_nilai = input("Silahkan input nilai pasar pemain = ")
        data_pemain.append([tambah_nama, tambah_usia, tambah_kontrak, tambah_nilai])
        print("Data pemain berhasil ditambahkan.")

    elif pilihan == 4 :
        ubah_data = input("Data nama pemain yang akan diubah: ")
        ditemukan = False
        for data in data_pemain:
            if data[0].lower() == ubah_data.lower():
                print("Pilih data yang ingin diubah:")
                print("1. Usia")
                print("2. Kontrak")
                print("3. Nilai Pasar")
                pilihan_ubah = input("Masukkan pilihan (1/2/3): ")
                if pilihan_ubah == "1":
                    try:
                        data[1] = int(input("Usia baru: "))
                        print("Usia berhasil diubah.")
                    except ValueError:
                        print("Usia harus berupa angka.")
                elif pilihan_ubah == "2":
                    try :
                        data[2] = int(input("Durasi kontrak baru: "))
                        print("Kontrak berhasil diubah.")
                    except ValueError:
                        print("Kontrak harus berupa angka.")
                elif pilihan_ubah == "3":
                    try :
                        data[3] = int(input("Nilai pasar baru: "))
                        print("Nilai berhasil diubah.")
                    except ValueError:
                        print("Nilai harus berupa angka.")
                else:
                    print("Pilihan tidak valid.")
                ditemukan = True
                break
        if not ditemukan:
            print("Data tidak ditemukan.")

    else :
        print("Pilihan tidak tersedia")

    lanjut = input("\nApakah anda ingin memilih menu lagi? (ya/tidak): ")
    if lanjut.lower() != "ya":
        print("Terima kasih telah menggunakan program ini.")
        break
