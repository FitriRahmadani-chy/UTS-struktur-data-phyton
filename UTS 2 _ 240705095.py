# Program Queue Pengunjung Kafe dengan laporan akhir

class Queue:
    def __init__(self):   # gunakan __init__ (dua garis bawah) yaitu konstuktor (fungsi otomatis yg dipanggil saat objek dibuat karena dia menyimpaqn data)
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def tampilkan(self):
        for item in self.items:
            print(item, end=" ")
        print()


# Program utama
antrian = Queue()
pesanan_selesai = []  # menyimpan hasil pesanan semua konsumen

jumlah = int(input("Masukkan jumlah konsumen cafe = "))

# Input nama konsumen cafe
for i in range(1, jumlah + 1):
    nama = input(f"Konsumen Cafe {i} = ")
    antrian.enqueue(nama)

# Cetak semua antrian awal konsumen
print("\nCetak Konsumen Cafe =", end=" ")
antrian.tampilkan()
print()

# Simulasi: satu per satu konsumen dilayani
while not antrian.is_empty():
    keluar = antrian.dequeue()
    print(f"Simulasi = {keluar}")
    pesanan = input("Ingin pesan apa? : ")
    print(f"{keluar}, {pesanan}")
    pesanan_selesai.append((keluar, pesanan))  # simpan hasil pesanan konsumen
    print()

# Cetak daftar pesanan akhir konsumen
print("----- Daftar Pesanan Selesai -----")
for nama, pesanan in pesanan_selesai:
    print(f"{nama} - {pesanan}")
