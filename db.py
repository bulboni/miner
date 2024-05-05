import pyautogui
import time
import random
import gc  # Import modul gc untuk garbage collection

# Setel fail-safe menjadi False
pyautogui.FAILSAFE = False

# Rekaman gerakan mouse sebelumnya (ganti dengan rekaman Anda)
recorded_mouse_actions = [
    (374, 240, 0.9),  # Contoh: Gerakan ke koordinat (100, 200) dalam 0.5 detik
    (486, 245, 0.9),
    # ... tambahkan langkah lainnya
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
        interval = 120  # Jeda waktu setiap 5 menit setelah 100 klik pertama

    random_delay = random.uniform(2, 6)  # Jeda waktu acak antara 2 hingga 6 detik
    time.sleep(random_delay)
    
    # Memainkan kembali rekaman gerakan mouse
    for action in recorded_mouse_actions:
        if action[0] == 374 and action[1] == 240:  # Jika mouse berada di koordinat (631, 378)
            pyautogui.moveTo(action[0], action[1], duration=action[2])
            pyautogui.doubleClick()  # Melakukan double klik
            time.sleep(60)  # Tunggu 1 menit
            pyautogui.hotkey('ctrl', 'c')  # Tekan tombol Ctrl + C
            pyautogui.press('enter')  # Tekan tombol Enter
        elif action[0] == 486 and action[1] == 245:  # Jika mouse berada di koordinat (700, 751)
            pyautogui.moveTo(action[0], action[1], duration=action[2])
            pyautogui.doubleClick()  # Melakukan double klik
            pyautogui.moveTo(374, 240, duration=0.5)  # Pindahkan mouse ke koordinat (631, 378)
        else:
            pyautogui.moveTo(action[0], action[1], duration=action[2])
            pyautogui.doubleClick()  # Melakukan double klik pada setiap langkah
    
    # Membersihkan sampah (garbage collection)
    gc.collect()
    
    # Menunggu sebentar sebelum mengulang langkah berikutnya
    time.sleep(interval)
    
    current_time = time.time()
    click_counter += 1
