# ARRAY 1D: nama barang dan nama gudang
barang = ["Beras", "Gula", "Mie", "Minyak", "Telur"]
gudang = ["Gudang A", "Gudang B"]

# ARRAY 2D: stok[i][j] = stok barang ke-j di gudang ke-i
#               Beras  Gula  Mie  Minyak  Telur
stok = [[100,    30,   80,    50,     40],     # Gudang A
        [ 60,    20,   40,    25,     15]]     # Gudang B

# ARRAY 2D: donasi = [[nama, jumlah, sisa_hari_kedaluwarsa], ...]

donasi = [ 
    ["Minyak", 40, 30],
    ["Beras", 100,  5],
    ["Mie",    60, 90],
    ["Telur",  30,  3],
]

def baca_angka(pesan):
    """Minta input bilangan bulat > 0 sampai valid."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai > 0:
                return nilai
            print("  Angka tidak boleh bernilai negatif atau kosong!")
        except ValueError:
            print("  Input harus berupa bilangan bulat!")


def tampil_daftar(judul, daftar):
    print(f"\n--- {judul} ---")
    for i in range(len(daftar)):
        print(f"{i + 1}. {daftar[i]}")


def tampil_donasi(judul, data):
    print(f"\n--- {judul} ---")
    for d in data:
        print(f"  {d[0]:<8} {d[1]:>4} unit   sisa {d[2]:>3} hari")


# SEARCHING 

def binary_search(arr, target, kiri, kanan, langkah=0):
    """BINARY SEARCH (REKURSIF): syarat array sudah URUT.
       Bandingkan dengan elemen tengah, lalu cari di separuhnya saja.
       Best O(1), Average/Worst O(log n)."""
    if kiri > kanan:                        # BASE CASE: tidak ketemu
        return -1, langkah
    tengah = (kiri + kanan) // 2
    langkah += 1
    if arr[tengah] == target:               # BASE CASE: ketemu
        return tengah, langkah
    elif target < arr[tengah]:              # buang separuh kanan
        return binary_search(arr, target, kiri, tengah - 1, langkah)
    else:                                   # buang separuh kiri
        return binary_search(arr, target, tengah + 1, kanan, langkah)


# SORTING 

def bubble_sort(data):
    """BUBBLE SORT: bandingkan 2 data bertetangga, tukar jika salah urut.
       Diurutkan FEFO: sisa hari paling sedikit didahulukan.
       Best O(n) (data sudah urut), Worst O(n^2)."""
    hasil = []
    for baris in data:
        hasil.append(baris[:])              # salin agar data asli aman
    n = len(hasil)
    perbandingan = 0
    for i in range(n - 1):
        ada_tukar = False
        for j in range(n - 1 - i):
            perbandingan += 1
            if hasil[j][2] > hasil[j + 1][2]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
                ada_tukar = True
        if not ada_tukar:                   # tidak ada tukar = sudah urut
            break
    return hasil, perbandingan


# REKURSI

def total_rekursif(arr, i=0, tampil=False):
    """Jumlah semua elemen secara REKURSIF. Time complexity O(n).
       Base case : i sudah di luar array -> 0
       Rekursi   : arr[i] + total dari sisa elemen."""
    jarak = "   " * i
    if i == len(arr):                       # BASE CASE
        if tampil:
            print(f"{jarak}panggilan i={i}: elemen habis -> kembali 0")
        return 0
    if tampil:
        print(f"{jarak}panggilan i={i}: {arr[i]} + (total sisanya)")
    hasil = arr[i] + total_rekursif(arr, i + 1, tampil)   # panggil diri sendiri
    if tampil:
        print(f"{jarak}selesai    i={i}: hasil = {hasil}")
    return hasil



# FITUR MENU

def lihat_stok():
    print("\n--- PETA STOK GUDANG ---")
    print(" " * 10, end="")
    for b in barang:                        # judul kolom dari array 1D
        print(f"{b:>8}", end="")
    print()
    for i in range(len(gudang)):            # perulangan BARIS
        print(f"{gudang[i]:<10}", end="")
        for j in range(len(barang)):        # perulangan KOLOM
            print(f"{stok[i][j]:>8}", end="")
        print()


def tambah_donasi():
    tampil_daftar("TAMBAH DONASI - Daftar Barang", barang)
    nama = input("Nama barang    : ").strip().title()
    posisi, langkah = binary_search(barang, nama, 0, len(barang) - 1)
    if posisi == -1:
        print(f"Barang '{nama}' tidak dikenali.")
        return
    jumlah = baca_angka("Jumlah (unit)        : ")
    hari = baca_angka("Sisa hari kedaluwarsa: ")
    tampil_daftar("Pilih gudang penerima", gudang)
    g = baca_angka("Nomor gudang         : ")
    if g < 1 or g > len(gudang):
        print("Gudang tidak valid, donasi dibatalkan.")
        return
    donasi.append([nama, jumlah, hari])     # tambah ke array donasi
    stok[g - 1][posisi] += jumlah           # perbarui array 2D stok
    print(f"Donasi tercatat! Stok {nama} di {gudang[g - 1]} bertambah {jumlah}.")
    print(f"(Validasi nama barang: {langkah} langkah binary search)")


def cari_barang():
    tampil_daftar("CARI BARANG (Binary Search)", barang)
    nama = input("Nama barang yang dicari: ").strip().title()
    posisi, langkah = binary_search(barang, nama, 0, len(barang) - 1)
    if posisi == -1:
        print(f"Barang '{nama}' tidak ditemukan ({langkah} langkah binary search).")
    else:
        print(f"Barang '{nama}' ditemukan pada posisi {posisi + 1} ({langkah} langkah binary search).")


def urutkan_donasi():
    tampil_donasi("DONASI SEBELUM DIURUT", donasi)
    hasil, banding = bubble_sort(donasi)
    tampil_donasi("SESUDAH DIURUT (FEFO: kedaluwarsa terdekat dulu)", hasil)
    print(f"\nJumlah perbandingan: {banding}")
    print("Baris paling atas harus segera dibagikan!")


def rekap_stok():
    print("\n--- REKAP TOTAL STOK: REKURSIF ---")
    for j in range(len(barang)):
        kolom = []                          # kumpulkan stok barang ke-j
        for i in range(len(gudang)):
            kolom.append(stok[i][j])
        print(f"{barang[j]:<8}: rekursif = {total_rekursif(kolom):>4}")

    print("\nJejak rekursi untuk stok Beras:")
    kolom = [stok[i][0] for i in range(len(gudang))]
    total_rekursif(kolom, tampil=True)


# MENU UTAMA 

def menu():
    while True:
        print("\n" + "=" * 45)
        print("   PANGANKITA - Gudang Bantuan Sembako")
        print("=" * 45)
        print("1. Lihat stok gudang ")
        print("2. Tambah donasi ")
        print("3. Cari barang ")
        print("4. Urutkan donasi ")
        print("5. Rekap total stok ")
        print("6. Keluar")
        pilih = baca_angka("Pilih menu: ")

        if pilih == 1:
            lihat_stok()
        elif pilih == 2:
            tambah_donasi()
        elif pilih == 3:
            cari_barang()
        elif pilih == 4:
            urutkan_donasi()
        elif pilih == 5:
            rekap_stok()
        elif pilih == 6:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak ada, coba lagi.")


if __name__ == "__main__":
    menu()