from pynput.keyboard import Listener, Key, Controller

keyboard = Controller()

def press_ctrl_v():
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    

def on_release(key):
    if key == Key.down:
        press_ctrl_v()
    elif key == Key.esc:
        return False

with Listener(on_release=on_release) as listener:
    listener.join()
