import pyautogui
import time
import random
import gc  # Import modul gc untuk garbage collection

# Setel fail-safe menjadi False
pyautogui.FAILSAFE = False

# Koordinat untuk double klik
coordinates = [
    (287, 615),
    (966, 611)
]

# Masa aktif (86400 detik = 24 jam)
total_duration = 86400
start_time = time.time()
current_time = time.time()

# Jeda 1 menit sebelum memulai proses apapun
time.sleep(60)

while current_time - start_time < total_duration:
    for coord in coordinates:
        pyautogui.moveTo(coord[0], coord[1], duration=0.5)
        pyautogui.doubleClick()
    
    # Membersihkan sampah (garbage collection)
    gc.collect()
    
    # Menunggu 3 menit sebelum melakukan double klik lagi
    time.sleep(180)
    
    current_time = time.time()
