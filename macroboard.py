#! /usr/bin/python -u

from evdev import UInput, InputDevice, categorize, ecodes
import webbrowser
import subprocess
from keybinds import bindings

dev = InputDevice('/dev/input/by-id/usb-NOVATEK_Kensington_U+P_Keyboard-event-kbd')
dev.grab()
ui = UInput()


## write the key specified in the bind_dict
def write_input(bind): 
    for i in bind:
        key_number = ecodes.ecodes[i]
        ui.write(ecodes.EV_KEY, key_number, 1)
        ui.syn()
    for i in bind:
        key_number = ecodes.ecodes[i]
        ui.write(ecodes.EV_KEY, key_number, 0)
        ui.syn()


## check bind type and execute associated bind
def execute_bind():
    if key.keycode in bindings:
        bind = bindings[key.keycode][1]
        if bindings[key.keycode][0] == 'input':
            write_input(bind)
        elif bindings[key.keycode][0] == 'web':
            webbrowser.open(bind,new=2,autoraise=True)
        elif bindings[key.keycode][0] == 'unassigned':
            print('No acton assigned to ' + key.keycode)
            subprocess.call(['notify-send', '-u', 'low', 'MacroBoard', 'No Action Assigned to ' + key.keycode])
        else:
            print('Key must be a web or input type. Key is currently set to the type: ' + bindings[key.keycode][0])
    else:
        print(key.keycode + ' is undefined')


## Loop to read input from device 
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_ESC':
                quit()
            else:
                execute_bind()
