#! /usr/bin/python

from evdev import UInput, InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/by-id/usb-NOVATEK_Kensington_U+P_Keyboard-event-kbd')
dev.grab()

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_ESC':
                quit()
            else: 
                print(key)
