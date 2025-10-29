# Program Queue Data Konsumen 

from collections import deque

def main():
    queue = deque()

    # Input jumlah konsumen
    jumlah = int(input("Masukkan jumlah konsumen cafe : "))

    # Input nama konsumen satu per satu
    for i in range(jumlah):
        nama = input(f"Konsumen {+1} : ")
        queue.append(nama)

    # Cetak daftar konsumen dalam antrian
    print("\nCetak Konsumen :", end=" ")
    for nama in queue:
        print(nama, end=" ")
    print()

    # Simulasi: konsumen cafe pertama keluar dari antrian
    if len(queue) > 0:
        keluar = queue.popleft()
        print(f"\nSimulasi : {keluar} keluar dari antrian")

    # Cetak daftar antrian setelah simulasi
    print("Cetak Konsumen :", end=" ")
    for nama in queue:
        print(nama, end=" ")
    print()

if __name__ == "__main__":
    main()
