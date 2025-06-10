print("===Program login===")

username_benar = "kiranadwivaninda"
password_benar = "2410931005"
kesempatan = 3

for _ in range(3) :
    while True :
        username = input("Silahkan masukkan username = ")
        password = input("Silahkan masukkan password = ")

        if username == username_benar and password_benar == password_benar :
             print("Anda berhasil login, selamat datang")
             break 
        else :
            kesempatan -= 1
            print(f"username atau password salah, kesempatan tersisa : {kesempatan}")

            if kesempatan == 0 :
                print("silahkan coba beberapa saat lagi")
                exit()

    while True :
        try :
            daftar_harga = {"Padang Bukittinggi" : 20000, "Padang Batusangkar" : 30000, "Padang Solok" : 50000, "Padang Payakumbuh" : 65000}
    
            Nama = (str(input("Nama Pemesan : ")))
            Rute = (str(input("Pilih rute yang ingin dipesan : ")))
            Jumlah = (int(input("Jumlah tiket yang ingin dipesan : ")))

            if Rute in daftar_harga :
                Total = Jumlah*daftar_harga[Rute]
                print("Total harga tiket : ", Total )
            else :
                print("Pilihan tidak tersedia")
            break 
        except ValueError : 
            print("Masukkan data yang benar")

    Menambah_data = input("Apakah anda masih ingin menambah data? ")
    if Menambah_data == "tidak" :
        break
    else : 
        print("Silahkan login kembali")   