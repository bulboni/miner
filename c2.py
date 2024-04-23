import pyautogui
import time
import random

# Daftar koordinat dan jumlah klik
click_coordinates = [
    (183, 51, 1),  # Klik 1x di koordinat (183, 51)
    (82, 493, 1),  # Klik 2x di koordinat (82, 493)
    (82, 494, 1),  # Klik 2x di koordinat (82, 493)
    # Tambahkan koordinat dan jumlah klik lainnya di sini
]

# Masa aktif (86400 detik = 24 jam)
total_duration = 86400
start_time = time.time()
current_time = time.time()
click_counter = 0

while current_time - start_time < total_duration:
    if click_counter < 100:
        interval = 60  # Jeda waktu setiap 60 detik untuk 100 klik pertama
    else:
        interval = 300  # Jeda waktu setiap 5 menit setelah 100 klik pertama

    random_delay = random.uniform(2, 6)  # Jeda waktu acak antara 2 hingga 6 detik
    time.sleep(random_delay)
    
    # Memainkan kembali rekaman gerakan mouse
    for coordinate in click_coordinates:
        x, y, clicks = coordinate
        if (x, y) == (82, 493):
            pyautogui.click(x, y)  # Melakukan klik di koordinat (82, 493)
            time.sleep(10)  # Menunggu 10 detik setelah klik di koordinat (82, 493)
        else:
            for _ in range(clicks):
                pyautogui.click(x, y)  # Melakukan klik sesuai jumlah yang ditentukan
                time.sleep(0.1)  # Jeda singkat antara klik
    
    # Menunggu sebentar sebelum mengulang langkah berikutnya
    time.sleep(interval)
    
    current_time = time.time()
    click_counter += 1
