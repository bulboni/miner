import pyautogui
import time
import random

# Rekaman gerakan mouse sebelumnya (ganti dengan rekaman Anda)
recorded_mouse_actions = [
    (631, 378, 0.5),  # Contoh: Gerakan ke koordinat (100, 200) dalam 0.5 detik
    (677, 586, 0.5),
    (744, 611, 0.5),
    (805, 580, 0.5),
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
        interval = 300  # Jeda waktu setiap 5 menit setelah 100 klik pertama

    random_delay = random.uniform(2, 6)  # Jeda waktu acak antara 2 hingga 6 detik
    time.sleep(random_delay)
    
    # Menambahkan langkah untuk mengetik "top" dan tekan tombol Enter di koordinat pertama
    recorded_mouse_actions.insert(0, ('top', 0))  # Mengetik "top"
    recorded_mouse_actions.insert(1, ('enter', 0))  # Tekan tombol Enter
    
    # Memainkan kembali rekaman gerakan mouse
    for action in recorded_mouse_actions:
        if action[0] == 'top':
            pyautogui.typewrite('top', interval=0.25)
        elif action[0] == 'enter':
            pyautogui.press('enter')
        else:
            pyautogui.moveTo(action[0], action[1], duration=action[2])
            pyautogui.doubleClick()  # Melakukan double klik pada setiap langkah
    
    pyautogui.hotkey('ctrl', 'c')  # Menekan tombol Ctrl + C
    
    pyautogui.clearCache()  # Membersihkan cache memori pyautogui
    
    # Menunggu sebentar sebelum mengulang langkah berikutnya
    time.sleep(interval)
    
    current_time = time.time()
    click_counter += 1
