from datetime import datetime

print("===================================")
print(" Selamat Datang di Aplikasi Aktivitas ")
print("===================================")

print("\nPilihan Aktivitas:")
print("1. Sarapan")
print("2. Berangkat Kerja")
print("3. Olahraga")

pilihan = input("\nMasukkan pilihan aktivitas (1/2/3): ")

# List menu makanan yang tersedia
menu_tersedia = ["telur", "ikan", "nugget"]

# Aktivitas Sarapan
if pilihan == "1":
    print("\n=== Aktivitas Sarapan ===")

    print("Menu yang tersedia:", ", ".join(menu_tersedia))

    menu = input("Masukkan menu sarapan: ").lower()

    if menu in menu_tersedia:
        print(f"{menu.capitalize()} tersedia.")
        print("Silakan dimasak terlebih dahulu.")

        minuman = input("Apakah ingin minuman juga? (ya/tidak): ").lower()

        if minuman == "ya":
            jenis_minuman = input("Masukkan minuman yang diinginkan: ")
            print(f"Menyiapkan {jenis_minuman}.")
        else:
            print("Tidak menambahkan minuman.")

    else:
        print("Bahan tidak tersedia.")
        print("Silakan membeli bahan terlebih dahulu.")

# Aktivitas Berangkat Kerja
elif pilihan == "2":
    print("\n=== Aktivitas Berangkat Kerja ===")

    sekarang = datetime.now()

    jam_sekarang = sekarang.hour
    menit_sekarang = sekarang.minute

    print("Waktu sekarang:", sekarang.strftime("%H:%M"))

    jam_masuk = 8

    # Menghitung sisa waktu sebelum masuk kerja
    sisa_waktu = ((jam_masuk - jam_sekarang) * 60) - menit_sekarang

    if jam_sekarang >= jam_masuk:
        terlambat_menit = ((jam_sekarang - jam_masuk) * 60) + menit_sekarang

        print("Anda terlambat masuk kerja!")
        print(f"Keterlambatan: {terlambat_menit} menit")

    else:
        print("Anda belum terlambat masuk kerja.")
        print(f"Sisa waktu sebelum masuk kerja: {sisa_waktu} menit")

        if sisa_waktu >= 120:
            print("Anda masih punya banyak waktu.")
            print("Anda bisa santai, sarapan, atau olahraga terlebih dahulu.")

        elif sisa_waktu >= 60:
            print("Masih ada waktu untuk bersiap-siap.")

        else:
            print("Segera bersiap untuk berangkat kerja!")

# Aktivitas Olahraga
elif pilihan == "3":
    print("\n=== Aktivitas Olahraga ===")

    jenis_olahraga = input("Masukkan jenis olahraga: ")
    durasi = input("Masukkan durasi olahraga (menit): ")

    print(f"Anda akan melakukan olahraga {jenis_olahraga}")
    print(f"Durasi olahraga: {durasi} menit")
    print("Semangat! Jangan lupa minum air putih!")

# Jika pilihan tidak sesuai
else:
    print("Pilihan tidak ada, ayo pilih yang ada aja.")