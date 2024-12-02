# Lu'lu'a Lim'a Laila
# Programming dan GCS
# Tugas Magang Bengawan UV 2024

import cv2
import time

class Ayah:
    def __init__(self, nama, usia, peran):
        self.nama = nama
        self.usia = usia
        self.peran = peran

    def berkenalan(self):
        print(f"{self.nama} adalah {self.peran}. {self.peran} berusia {self.usia} tahun.")

    def jadwal_harian(self):
        """
        Jadwal harian ayah.
        """
        jadwal = [
            "Membangunkan anak",
            "Membantu istri memasak",
            "Membantu istri menyapu",
            "Bekerja",
            "Menjemput anak dari sekolah",
            "Membantu istri mencuci piring",
            "Tidur"
        ]
        print(f"Jadwal harian {self.nama}:")
        for i, tugas in enumerate(jadwal, 1):
            print(f"{i}. {tugas}")
        return jadwal

    def melihat(self):
        print(f"{self.nama} sedang membuka mata untuk melihat...")
        time.sleep(1) # memberi jeda waktu
        cap = cv2.VideoCapture(0) 

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Gagal membuka mata.") # jika pembacaan frame gagal, kamera akan ditutup
                break

            mirror_frame = cv2.flip(frame, 1) # mencerminkan frame secara horizontal
            cv2.imshow(f'Penglihatan {self.nama}', mirror_frame)

            # Tahan frame selama 1ms, tekan 'a' untuk keluar
            if cv2.waitKey(1) & 0xFF == ord('a'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print(f"{self.nama} telah menutup mata.\n\n")

class Ibu(Ayah):
    def jadwal_harian(self):
        """
        Menyusun jadwal harian ibu berdasarkan prioritas.
        """
        jadwal = [
            "Membuat sarapan",
            "Mengantar anak ke sekolah",
            "Yoga dan Pilates",
            "Ngemall",
            "Nyalon",
            "Memasak makan malam",
            "Tidur"
        ]
        print(f"Jadwal harian {self.nama}:")
        for i, tugas in enumerate(jadwal, 1):
            print(f"{i}. {tugas}")
        return jadwal

class Anak(Ayah):
    pass

# Objek 1: Ayah
ayah1 = Ayah("Dimas", 45, "Ayah")
ayah1.berkenalan()
ayah1.jadwal_harian()
ayah1.melihat()

# Objek 2: Ibu
ibu1 = Ibu("Putri", 43, "Ibu")
ibu1.berkenalan()
ibu1.jadwal_harian()
ibu1.melihat()

# Objek 3: Anak
anak1 = Anak("Caca", 10, "Anak")
anak1.berkenalan()
anak1.melihat()
