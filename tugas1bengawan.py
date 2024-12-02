# Lu'lu'a Lim'a Laila
# Informatika 23
# Tugas 1 Magang Bengawan UV

import random

tingkatLevel = ("Mudah", "Menengah", "Sulit") # Tuple untuk tingkat kesulitan

aturanLevel = {
    "Mudah" : {"batasBawah": 1, "batasAtas": 20, "kesempatan": 15},
    "Menengah" : {"batasBawah": 1, "batasAtas": 25, "kesempatan": 10},
    "Sulit" : {"batasBawah": 1, "batasAtas": 30, "kesempatan": 5}
} # Dictionary untuk pengaturan level

def aturanMain():
    print("\n======= SELAMAT DATANG DI GAME TEBAK ANGKA =======")
    print("Aturan Permainan:")
    print("1. Komputer akan memilih angka acak")
    print("2. Anda harus menebak angka tersebut")
    print("3. Setelah menebak, akan diberi petunjuk:")
    print("   - 'Terlalu Rendah' jika tebakan Anda kurang")
    print("   - 'Terlalu Tinggi' jika tebakan Anda lebih")
    print("   - 'Benar!' jika tebakan tepat")

def pilihLevel():
    print("\nPilih Tingkat Kesulitan :")
    for i, level in enumerate(tingkatLevel, 1) : # for untuk menampilkan pilihan level, memulai penomoran dari 1 bukan 0
        print(f"{i}. {level}")

    pilihan = int(input("Masukkan nomor level yang dipilih : "))
    if 1 <= pilihan <= len(tingkatLevel): # memastikan input dalam rentang yg valid
        return tingkatLevel[pilihan-1]  # -1 sebab indeks list dimulai dari 0
    else:
        print("Pilihan tidak valid.")

def main():
    aturanMain()

    level = pilihLevel()
    pengaturan = aturanLevel[level] 

    angkaRahasia = random.randint(
        pengaturan["batasBawah"],
        pengaturan["batasAtas"]
    )

    print(f"\nTebak angka antara {pengaturan['batasBawah']} hingga {pengaturan['batasAtas']}")

    kesempatan = pengaturan["kesempatan"] # mengambil jumlah kesempatan dari dictionary pengaturan
    menang = False #  melacak status permainan, false jadi true saat pemain berhasil menebak angka

    while kesempatan > 0 and not menang:
        print(f"\nKesempatan tersisa : {kesempatan}")

        # Input tebakan pemain
        tebakan = int(input("Masukkan tebakan Anda: "))
            
        # Operator perbandingan untuk mengecek tebakan
        if tebakan < pengaturan["batasBawah"] or tebakan > pengaturan["batasAtas"]:
            print(f"Tebakan di luar rentang {pengaturan['batasBawah']} - {pengaturan['batasAtas']}!")
            continue
            
        # Pengecekan tebakan
        if tebakan < angkaRahasia:
            print("Terlalu Rendah!")
        elif tebakan > angkaRahasia:
            print("Terlalu Tinggi!")
        else:
            print(f"BENAR! Anda berhasil menebak {angkaRahasia}")
            menang = True
            
        kesempatan -= 1
    
    if menang:
        print(f"\nSelamat! Anda menang.")
    else:
        print(f"\nMaaf, kesempatan habis. Angka rahasianya adalah {angkaRahasia}")

def menu():
    while True:
        print("\n===== GAME TEBAK ANGKA =====")
        print("1. Mulai Permainan")
        print("2. Keluar")
        
        pilihan = input("Pilih menu : ")
        
        if pilihan == "1":
            main()
        elif pilihan == "2":
            print("Terima kasih telah bermain. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()