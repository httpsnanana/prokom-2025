pin = 9310
saldo_awal = 2410

for i in range(3) :
    pin_masuk = int(input("Input pin anda = ")) 
    if pin_masuk == pin : 
        print("Anda berhasil masuk")
        break
    else :
        if i < 2 :
            print(f"PIN salah, kesempatan tersisa ",{2 - i })
        else : 
            exit("Percobaan habis, anda gagal login")

print("\nPilih jenis transaksi :\n1. Tarik\n2. Transfer\n3. Setor Tunai") 
transaksi = {1 : 'tarik', 2 : 'transfer', 3 : 'setor tunai'}
while True :
    jenis_transaksi = int(input("Silahkan pilih jenis transaksi anda = "))
    if jenis_transaksi == 1 :
        try :
            jumlah_transaksi = int(input("Silahkan masukkan jumlah transaksi = "))
            tarik = saldo_awal - jumlah_transaksi
            print(f'''\nAnda telah melakukan transaksi tarik sebesar Rp.{jumlah_transaksi}
                    Saldo akhir anda tersisa Rp.{tarik}''')
            saldo_awal -= jumlah_transaksi
        except ValueError :
            print('Input tidak valid, jumlah transaksi harus berupa angka. Coba lagi')
    elif jenis_transaksi == 2 :
        try :
            jumlah_transaksi = int(input("Silahkan masukkan jumlah transaksi = "))
            transfer = saldo_awal - jumlah_transaksi
            print(f'''\nAnda telah melakukan transaksi transfer sebesar Rp.{jumlah_transaksi}
                    Saldo akhir anda tersisa Rp.{transfer}''')
            saldo_awal -= jumlah_transaksi
        except ValueError :
            print('Input tidak valid, jumlah transaksi harus berupa angka. Coba lagi')
    elif jenis_transaksi == 3 :
        try :
            jumlah_transaksi = int(input("Silahkan masukkan jumlah transaksi = "))
            setor_tunai = saldo_awal + jumlah_transaksi
            print(f'''\nAnda telah melakukan transaksi setor tunai sebesar Rp.{jumlah_transaksi}
                    Saldo akhir anda tersisa Rp.{setor_tunai}''')
            saldo_awal += jumlah_transaksi
        except ValueError :
            print('Input tidak valid, jumlah transaksi harus berupa angka. Coba lagi')
    else :
        print("Pilihan anda tidak tersedia")
        continue
    ulangi = input("Apakah ada ingin melakukan transaksi lagi? (Ya/Tidak) = ")
    if ulangi.lower() != 'ya':
        print("Terimakasih sudah menggunakan layanan ini")
        break
    
