from datetime import datetime

# Header
sekarang = datetime.now()
jam_sekarang = sekarang.hour

if jam_sekarang < 11:
    salam = "Selamat Pagi"
elif jam_sekarang < 15:
    salam = "Selamat Siang"
elif jam_sekarang < 18:
    salam = "Selamat Sore"
else:
    salam = "Selamat Malam"

print("=" * 42)
print("         ACTIVITY DASHBOARD")
print("=" * 42)
print(salam)
print("Waktu saat ini :", sekarang.strftime("%H:%M:%S"))

# Layout catur
print("\n=== Layout Catur ===")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()

# Manajemen aktivitas
print("\n=== Manajemen Aktivitas ===")

daftar_aktivitas = []

jumlah = int(input("Berapa aktivitas yang ingin ditambahkan? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Masukkan aktivitas           : ")
    detail = input("Masukkan detail aktivitas    : ")
    jam_mulai = input("Masukkan jam mulai (HH:MM)   : ")
    jam_selesai = input("Masukkan jam selesai (HH:MM) : ")
    prioritas = input("Masukkan prioritas (tinggi/sedang/rendah): ")

    status = input("Status aktivitas (selesai/belum): ").lower()

    if status not in ["selesai", "belum"]:
        status = "belum"

    data = {
        "aktivitas": aktivitas,
        "detail": detail,
        "jam_mulai": jam_mulai,
        "jam_selesai": jam_selesai,
        "prioritas": prioritas,
        "status": status
    }

    daftar_aktivitas.append(data)

print("\n" + "=" * 42)
print("           DAFTAR AKTIVITAS")
print("=" * 42)

jumlah_selesai = 0
jumlah_belum = 0

for i, data in enumerate(daftar_aktivitas, start=1):

    print(f"\n{i}. Aktivitas : {data['aktivitas']}")
    print(f"   Detail     : {data['detail']}")
    print(f"   Waktu      : {data['jam_mulai']} - {data['jam_selesai']}")
    print(f"   Prioritas  : {data['prioritas']}")
    print(f"   Status     : {data['status']}")

    if data["status"] == "selesai":
        jumlah_selesai += 1
    else:
        jumlah_belum += 1

print("\n=== Ringkasan Aktivitas ===")
print(f"Total aktivitas : {len(daftar_aktivitas)}")
print(f"Selesai         : {jumlah_selesai}")
print(f"Belum selesai   : {jumlah_belum}")

print("\nSemua aktivitas berhasil disimpan!")