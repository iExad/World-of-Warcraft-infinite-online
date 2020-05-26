import win32api
import win32con
import time
import random
i = 0
while True:
    pong = random.random()
    ping = random.randint(100, 490)
    tennis = ping * pong
    print("END PRESSED...", tennis, 'sec'), time.asctime()
    win32api.keybd_event(win32con.VK_END, 0, 0, 0)
    win32api.keybd_event(win32con.VK_END, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(tennis)
