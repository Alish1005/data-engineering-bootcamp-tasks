import datetime
import time

import pyautogui as pg
t=datetime.datetime.now()
time.sleep(2)
for i in range(10000):
    t2=datetime.datetime.now().minute-t.minute
    print(i)
    print(t2," minutes")
    pg.click(button='left')