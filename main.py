import pyautogui
from time import sleep

from src.utils import *
from src.bot import *

pyautogui.PAUSE = 0
FOCUS_CHROME_SCREEN()
sleep(0.2)
connect_cepsum()
go_to_resa()
go_last_day()
wait_19h()
# go_day_before() #DELETE AFTER TESTING
sleep(0.5)
click_right_hour('templates/11.png')
reserve()

#CHANGER TEST EN PROD :
# PING PONG => TENNIS  T
# NOMBRE BOUCLE FOR wait_19h() T
# MOVE EN CLICK SUR LA RESA T
# ENLEVER LE GO DAY BEFORE T
