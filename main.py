import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='k')
QUIT_PROGRAM = KeyCode(char='y')

clicking = False
stop_program = False 
mouse = Controller()

def clicker():
    while not stop_program:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)
        
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
    if key == QUIT_PROGRAM:
        global stop_program
        stop_program = True
        clicking = False
        listener.__exit__(listener, BaseException, TypeError)
        time.sleep(1)
        print("Terminated")
        exit()
        
click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
        