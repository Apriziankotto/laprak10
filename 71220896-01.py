parkiran = [
    {'plat_nomor' : 'AB 3465 UK', 'jenis_kendaraan' : 'MOTOR', 'waktu_masuk': 15.30},
    {'plat_nomor' : 'AB 6851 JG', 'jenis_kendaraan' : 'MOTOR', 'waktu_masuk': 14.00},
    {'plat_nomor' : 'AB 2231 HH', 'jenis_kendaraan' : 'MOBIL', 'waktu_masuk': 13.45},
    {'plat_nomor' : 'B 3978 UL', 'jenis_kendaraan' : 'MOBIL', 'waktu_masuk': 16.00},
    {'plat_nomor' : 'UG 6987 AR', 'jenis_kendaraan' : 'MOTOR', 'waktu_masuk': 11.00},
    {'plat_nomor' : 'A 1 UK', 'jenis_kendaraan' : 'MOBIL', 'waktu_masuk': 10.30},
    {'plat_nomor' : 'AR 5768 UD', 'jenis_kendaraan' : 'MOTOR', 'waktu_masuk': 09.00}
]
def menu_dua(no_kendaraan):
    jam_pertama = 3000
    setiap_jam = 2000
    durasi = None
    jam_keluar = float(input("Masukan waktu keluar: "))
    for panggil in parkiran:
        if panggil['plat_nomor'] == no_kendaraan:
            durasi =  jam_keluar - panggil['waktu_masuk']
            parkiran.remove(panggil)
            break
    if durasi > 1:
        total = jam_pertama + (setiap_jam * (durasi-1))
        print(40*'=')
        print(f'No kendaraan: {panggil["plat_nomor"]}\nJenis kendaraan: {panggil["jenis_kendaraan"]}\nDurasi parkir: {int(durasi)} jam\nTotal yang dibayarkan: {int(total)}')
        print(40*'=')
    else:
        total = jam_pertama
        print(total)
    
def menu_tiga(no_kendaraan):
    batas = 0
    for panggil in parkiran:
        if panggil['plat_nomor'] == no_kendaraan:
            return True
        else:
            batas += 1
    if len(parkiran) == batas:
        return False
def menu_empat(jenis_kendaraan):
    total_motor = 0
    total_mobil = 0
    for panggil in parkiran:
        if panggil['jenis_kendaraan'] == jenis_kendaraan:
            total_motor += 1
        else:
            total_mobil += 1
    if jenis_kendaraan == 'Motor':
        return total_motor
    else:
        return total_mobil
while True:
    print('1. Kendaraan masuk.')
    print('2. Kendaraan keluar.')
    print('3. Cek kendaraan menggunakan no ds.')
    print('4. Cek berapa kendaraan (motor/mobil).')
    print('5. Cek waktu masuk kendaraan menggunakan no kendaraan.')
    print('6. Lihat daftar kendaraan.')
    print('Ketik "done" untuk keluar.')
    pilihan = input("Masukan pilihan anda: ").lower()
    if pilihan == "1":
        no_kendaraan = input('Masukan no kendaraan: ').upper()
        jenis_kendaraan = input('Masukan jenis kendaraan: ').upper()
        waktu_masuk = float(input('Masukan jam masuk: '))
        tamplate = {'plat_nomor' : no_kendaraan, 'jenis_kendaraan' : jenis_kendaraan, 'waktu_masuk': waktu_masuk}
        parkiran.append(tamplate)
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    elif pilihan == "2":
        no_kendaraan = input("Masukan no kendaraan: ").upper()
        if menu_tiga(no_kendaraan) == True:
            menu_dua(no_kendaraan)
        else:
            print(f"Kendaraan dengan no {no_kendaraan} tidak ada!")
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    elif pilihan == "3":
        no_kendaraan = input("Masukan no kendaraan: ").upper()
        if menu_tiga(no_kendaraan) == True:
            for panggil in parkiran:
                if panggil['plat_nomor'] == no_kendaraan:
                    print(40*'=')
                    print(f'Jenis kendaraan: {panggil["jenis_kendaraan"]}\nNo kendaraan: {panggil["plat_nomor"]}\nJam masuk: {panggil["waktu_masuk"]:.2f}')
                    print(40*'=')
        else:
            print(f"Kendaraan dengan plat '{no_kendaraan}' tidak ada")
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    elif pilihan == '4':
        jenis_kendaraan = input('Masukan jenis kendaraan yang mau diketahui jumlahnya: ')
        print(40*'=')
        print(f'Total kendaraan {jenis_kendaraan} yaitu {menu_empat(jenis_kendaraan)}')
        print(40*'=')
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    elif pilihan == '5':
        no_kendaraan = input('Masukan no kendaraan: ').upper()
        indikator = 0
        for panggil in parkiran:
            if panggil['plat_nomor'] == no_kendaraan:
                print(f'{no_kendaraan} masuk pada jam {panggil["waktu_masuk"]:.2f}')
            else:
                indikator += 1
        if indikator == len(parkiran):
            print(f'Kendaraan dengan plat {no_kendaraan} tidak ada!')
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    elif pilihan == '6':
        for panggil in parkiran:
            print(40*'=')
            print(f'Jenis kendaraan\t: {panggil["jenis_kendaraan"]}\nNo kendaraan\t: {panggil["plat_nomor"]}\nWaktu masuk\t: {panggil["waktu_masuk"]:.2f}')
            print(40*'=')
        pilihan = input("apakah anda ingin melanjutkan pencarin lain (y/n?)").lower()
        if pilihan == 'n':
            break
    else:
            break
