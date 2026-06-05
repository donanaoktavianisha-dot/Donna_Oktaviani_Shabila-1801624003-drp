from datetime import datetime

print("==========================================")
print("      MANAJEMEN AKTIVITAS HARIAN")
print("  Teman Digital untuk Mengatur Harimu")
print("==========================================")

print("\nApa yang ingin kamu lakukan hari ini?")
print("1. Sarapan")
print("2. Berangkat Kerja")
print("3. Olahraga")
print("4. Hiburan dan Relaksasi")

pilihan = input("\nMasukkan pilihan aktivitas (1/2/3/4): ")

# Daftar menu yang tersedia
menu_tersedia = ["telur", "ikan", "nugget"]

# Aktivitas Sarapan
if pilihan == "1":
    print("\n=== Aktivitas Sarapan ===")
    print("Menu yang tersedia:", ", ".join(menu_tersedia))

    menu = input("Masukkan menu sarapan yang diinginkan: ").lower()

    if menu in menu_tersedia:
        print(f"\nBahan untuk {menu.capitalize()} tersedia.")
        print("Menu perlu dimasak terlebih dahulu.")

        minuman = input("Apakah ingin menambahkan minuman? (ya/tidak): ").lower()

        if minuman == "ya":
            jenis_minuman = input("Masukkan minuman yang diinginkan: ")
            print(f"Menyiapkan {jenis_minuman} untuk menemani sarapan.")
        else:
            print("Tidak menambahkan minuman.")

        print("Selamat menikmati sarapan dan semoga harimu menyenangkan.")

    else:
        print("\nMaaf, bahan yang kamu inginkan belum tersedia.")
        print("Silakan membeli bahan terlebih dahulu.")

# Aktivitas Berangkat Kerja
elif pilihan == "2":
    print("\n=== Aktivitas Berangkat Kerja ===")

    sekarang = datetime.now()
    jam_sekarang = sekarang.hour
    menit_sekarang = sekarang.minute

    print("Waktu saat ini:", sekarang.strftime("%H:%M"))

    jam_masuk = 8
    sisa_waktu = ((jam_masuk - jam_sekarang) * 60) - menit_sekarang

    if jam_sekarang > jam_masuk or (jam_sekarang == jam_masuk and menit_sekarang > 0):

        terlambat_menit = ((jam_sekarang - jam_masuk) * 60) + menit_sekarang

        print("\nAnda terlambat masuk kerja.")
        print(f"Keterlambatan: {terlambat_menit} menit.")
        print("Segera berangkat agar tidak semakin terlambat.")

    else:
        print("\nAnda belum terlambat masuk kerja.")
        print(f"Sisa waktu sebelum masuk kerja: {sisa_waktu} menit.")

        print("\nPilih kendaraan yang akan digunakan:")
        print("1. Jalan Kaki")
        print("2. Sepeda")
        print("3. Motor")
        print("4. Mobil")

        kendaraan = input("Masukkan pilihan kendaraan (1/2/3/4): ")

        if kendaraan == "1":
            waktu_tempuh = 30
            nama_kendaraan = "Jalan Kaki"

        elif kendaraan == "2":
            waktu_tempuh = 20
            nama_kendaraan = "Sepeda"

        elif kendaraan == "3":
            waktu_tempuh = 10
            nama_kendaraan = "Motor"

        elif kendaraan == "4":
            waktu_tempuh = 15
            nama_kendaraan = "Mobil"

        else:
            waktu_tempuh = None
            nama_kendaraan = None

        if waktu_tempuh is not None:
            print(f"\nKendaraan yang dipilih: {nama_kendaraan}")
            print(f"Estimasi waktu tempuh: {waktu_tempuh} menit")

            if sisa_waktu > waktu_tempuh:
                print("Anda diperkirakan tiba tepat waktu.")
            elif sisa_waktu == waktu_tempuh:
                print("Waktunya pas. Sebaiknya segera berangkat sekarang.")
            else:
                print("Jika berangkat sekarang, Anda berpotensi terlambat.")
        else:
            print("Pilihan kendaraan tidak valid.")

        if sisa_waktu >= 120:
            print("\nAnda masih memiliki banyak waktu.")
            print("Anda dapat bersantai, sarapan, atau berolahraga terlebih dahulu.")
        elif sisa_waktu >= 60:
            print("\nMasih ada waktu untuk bersiap-siap dengan tenang.")
        else:
            print("\nSegera bersiap dan berangkat ke tempat kerja.")

# Aktivitas Olahraga
elif pilihan == "3":
    print("\n=== Aktivitas Olahraga ===")

    jenis_olahraga = input("Masukkan jenis olahraga: ")
    durasi = input("Masukkan durasi olahraga (menit): ")

    print(f"\nAnda akan melakukan olahraga {jenis_olahraga}.")
    print(f"Durasi yang direncanakan: {durasi} menit.")
    print("Jangan lupa melakukan pemanasan dan minum air putih yang cukup.")

# Aktivitas Hiburan dan Relaksasi
elif pilihan == "4":
    print("\n=== Hiburan dan Relaksasi ===")
    print("Saatnya melepas penat dan menikmati waktu luang.")

    print("\nPilih kegiatan:")
    print("1. Menonton Film")
    print("2. Bermain Game")
    print("3. Membaca Buku")
    print("4. Mendengarkan Musik")

    kegiatan = input("Masukkan pilihan kegiatan (1/2/3/4): ")

    if kegiatan == "1":
        genre = input("Masukkan genre film yang ingin ditonton: ")
        print(f"\nSelamat menikmati film bergenre {genre}.")
        print("Semoga menjadi hiburan yang menyenangkan.")

    elif kegiatan == "2":
        game = input("Masukkan nama game yang ingin dimainkan: ")
        print(f"\nSelamat bermain {game}.")
        print("Semoga mendapatkan pengalaman bermain yang seru.")

    elif kegiatan == "3":
        buku = input("Masukkan judul buku yang ingin dibaca: ")
        print(f"\nSelamat membaca '{buku}'.")
        print("Semoga mendapatkan wawasan dan inspirasi baru.")

    elif kegiatan == "4":
        musik = input("Masukkan genre musik yang ingin didengarkan: ")
        print(f"\nSelamat menikmati musik {musik}.")
        print("Semoga suasana hati menjadi lebih baik.")

    else:
        print("\nPilihan kegiatan tidak tersedia.")

# Input tidak valid
else:
    print("\nPilihan tidak tersedia.")
    print("Silakan pilih menu yang telah disediakan.")
