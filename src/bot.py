import pyautogui
from time import sleep

from src.utils import *
from enums.pixels import Colors,PixelPositions,PixelRegions

def connect_cepsum():
    newTab()
    sleep(1)
    write("www.cepsum.umontreal.ca")
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    sleep(1.5)
    click(PixelPositions.COMPTE_BUTTON.value)
    sleep(1)
    writeSpecial("LOGIN")
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    sleep(1)
    writeSpecial("MDP")
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    sleep(2)

def go_day_before():
    change_day(PixelRegions.SCREEN_ARROW_LEFT.value)

def go_day_after():
    change_day(PixelRegions.SCREEN_ARROW_RIGHT.value)

def validate_resa():
    screen = PixelRegions.SCREEN_SEARCH_VALIDATE.value
    x,y = find_color(screen[0], screen[1], Colors.VALIDATE_RESA.value)
    click((screen[0][0] + x + 15, screen[0][1] + y + 15))
    # pyautogui.moveTo(screen[0][0] + x + 15, screen[0][1] + y + 15)
    sleep(0.3)

def change_day(screen):
    x,y = find_color(screen[0], screen[1], Colors.ARROW_DAYS.value)
    if(x == -1):
        pyautogui.click()
    else:
        click((screen[0][0] + x, screen[0][1] + y))
    sleep(0.5)

def go_to_resa():
    click(PixelPositions.RESERVATION_BUTTON.value)
    sleep(1)
    click(PixelPositions.ADD_RESA_BUTTON.value)
    sleep(1)
    click(PixelPositions.TENNIS.value)
    # click(PixelPositions.PING_PONG.value)
    sleep(1)

def go_last_day():
    go_day_after()
    go_day_after()

def refresh():
    go_day_before()
    go_day_after()

def is_red():
    x,y = find_color(PixelRegions.SCREEN_SEARCH_RED.value[0], PixelRegions.SCREEN_SEARCH_RED.value[1], Colors.RED_WAIT.value)
    return x != -1

def wait_19h():
    # while(not is_red()):
    #     refresh()
    ###########
    isred = is_red()
    # while
    for i in range(150):
        if(isred):
            refresh()
            isred = is_red()
            print(isred) 
        else:
            break

def find_pos(image_hour,region):
    img = takeScreen(region)
    # showScreen(img)
    img.save("images/screen.png")
    pos_me = findPosition('images/screen.png', image_hour)
    return pos_me

def click_arrow_partner():
    pos_me = find_pos('templates/arrow_partner.png',PixelRegions.SCREEN_SEARCH_ARROW.value)
    pos_click = (PixelRegions.SCREEN_SEARCH_ARROW.value[0][0] + pos_me[0], PixelRegions.SCREEN_SEARCH_ARROW.value[0][1] + pos_me[1]-10)
    click(pos_click)
    sleep(0.1)
    return pos_click

def add_partner():
    pos_click = click_arrow_partner()
    click((pos_click[0],pos_click[1]+60))
    sleep(0.1)

def click_right_hour(image_hour):
    pos_me = find_pos(image_hour,PixelRegions.SCREEN_SEARCH_RESA.value)
    click((PixelRegions.SCREEN_SEARCH_RESA.value[0][0] + pos_me[0]+40, PixelRegions.SCREEN_SEARCH_RESA.value[0][1] + pos_me[1]-20))
    # x,y = (PixelRegions.SCREEN_SEARCH_RESA.value[0][0] + pos_me[0]+40, PixelRegions.SCREEN_SEARCH_RESA.value[0][1] + pos_me[1]-20)
    # pyautogui.moveTo(x,y)
    sleep(0.5)

def reserve():
    add_partner()
    validate_resa()