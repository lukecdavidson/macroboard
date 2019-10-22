#! /usr/bin/python

import webbrowser
from evdev import UInput, InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/by-id/usb-NOVATEK_Kensington_U+P_Keyboard-event-kbd')
dev.grab()
ui = UInput()


class WebBinding:
    def __init__(self, key, website):
        self.key = key
        self.website = website
    
    def action(self):
        webbrowser.open(self.website,new=2,autoraise=True)


class MacroBinding:
    def __init__(self, key, macro):
        self.key = key
        self.macro = macro

    def action(self):
        for i in x.macro:
            key_number = ecodes.ecodes[i]
            ui.write(ecodes.EV_KEY, key_number, 1)
            ui.syn()
        for i in x.macro:
            key_number - ecodes.ecodes[i]
            ui.write(ecodes.EV_KEY, key_number, 0)
            ui.syn()


q = WebBinding('KEY_Q', 'https://www.youtube.com')
x = MacroBinding('KEY_X', ['KEY_LEFTALT', 'KEY_F4'])


bindings = {'KEY_ESC': esc, 'KEY_F1': f1, 'KEY_F2': f2, 'KEY_F3': f3, 'KEY_F4': f4, 'KEY_F5': f5, 'KEY_F6': f6, 'KEY_F7': f7, 'KEY_F8': f8, 'KEY_F9': f9,
        'KEY_F10': f10, 'KEY_F11': f11, 'KEY_F12': f12, 'KEY_SYSRQ': sysrq, 'KEY_SCROLLLOCK': scrolllock, 'KEY_PAUSE': pause, 'KEY_GRAVE': grave, 'KEY_1': 1,
        'KEY_2': 2, 'KEY_3': 3, 'KEY_4': 4, 'KEY_5': 5, 'KEY_6': 6, 'KEY_7': 7, 'KEY_8': 8, 'KEY_9': 9, 'KEY_0': 0, 'KEY_MINUS': minus, 'KEY_EQUAL': equal,
        'KEY_BACKSPACE': backspace, 'KEY_INSERT': insert, 'KEY_HOME': home, 'KEY_PAGEUP': pageup, 'KEY_NUMLOCK': numlock, 'KEY_KPSLASH': kpslash,
        'KEY_KPASTERISK': kpasterisk, 'KEY_KPMINUS': kpminus, 'KEY_TAB': tab, 'KEY_Q': q, 'KEY_W': w, 'KEY_E': e, 'KEY_R': r, 'KEY_T': t, 'KEY_Y': y,
        'KEY_U': u, 'KEY_I': i, 'KEY_O': o, 'KEY_P': p, 'KEY_LEFTBRACE': leftbrace, 'KEY_RIGHTBRACE': rightbrace, 'KEY_BACKSLASH': backslash,
        'KEY_DELETE': delete, 'KEY_END': end, 'KEY_PAGEDOWN': pagedown, 'KEY_KP7': kp7, 'KEY_KP8': kp8, 'KEY_KP9': kp9, 'KEY_KPPLUS': kpplus,
        'KEY_CAPSLOCK': capslock, 'KEY_A': a, 'KEY_S': s, 'KEY_D': d, 'KEY_F': f, 'KEY_G': G, 'KEY_H': h, 'KEY_J': j, 'KEY_K': k, 'KEY_L': l,
        'KEY_SEMICOLON': semicolon, 'KEY_APOSTROPHE': apostrophe, 'KEY_ENTER': enter, 'KEY_KP4': kp4, 'KEY_KP5': kp5, 'KEY_KP6': kp6,
        'KEY_LEFTSHIFT': leftshift, 'KEY_Z': z, 'KEY_X': x, 'KEY_C': c, 'KEY_V': v, 'KEY_B': b, 'KEY_N': n, 'KEY_M': m, 'KEY_COMMA': comma, 'KEY_DOT': dot,
        'KEY_SLASH': slash, 'KEY_RIGHTSHIFT': rightshift, 'KEY_UP': up, 'KEY_KP1': kp1, 'KEY_KP2': kp2, 'KEY_KP3': kp3, 'KEY_KPENTER': kpenter,
        'KEY_LEFTCTRL': leftctrl, 'KEY_LEFTMETA': leftmeta, 'KEY_LEFTALT': leftalt, 'KEY_SPACE': space, 'KEY_RIGHTALT': rightalt, 'KEY_RIGHTMETA': rightmeta,
        'KEY_COMPOSE': compose, 'KEY_RIGHTCTRL': rightctrl, 'KEY_LEFT': left, 'KEY_DOWN': down, 'KEY_RIGHT': right, 'KEY_KP0': kp0, 'KEY_KPDOT': kpdot}


## Loop to read input from device 
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_ESC':
                quit()
            elif key.keycode == 'KEY_F12':
                print('Implement rebind function here')
            else:
                if key.keycode in bindings:
                    keyobject = bindings[key.keycode]
                    keyobject.action()
                else:
                    print(key.keycode + ' is undefined')
