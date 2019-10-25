#! /usr/bin/python

import webbrowser
from evdev import UInput, InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/by-id/usb-NOVATEK_Kensington_U+P_Keyboard-event-kbd')
dev.grab()
ui = UInput()


class UndefinedKey:
    def __init__(self, key):
        self.key = key

    def action(self):
        print('No acton assigned to ' + self.key)
        ubprocess.call(['notify-send', '-u', 'low', 'MacroBoard', 'No Action Assigned to ' + self.key])


class WebBinding:
    def __init__(self, website, new, autoraise):
        self.website = website
        self.new = new  ## new=0: open in same browser window, new=1: open in new window, new=2: open in new tab
        self.autoraise = autoraise
    
    def action(self):
        webbrowser.open(self.website,new=self.new,autoraise=self.autoraise)


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


KEY_ESC = quit()
KEY_F1 = UndefinedKey(KEY_F1)
KEY_F2 = UndefinedKey(KEY_F1)
KEY_F3 = UndefinedKey(KEY_F1)
KEY_F4 = UndefinedKey(KEY_F1)
KEY_F5 = UndefinedKey(KEY_F1)
KEY_F6 = UndefinedKey(KEY_F1)
KEY_F7 = UndefinedKey(KEY_F1)
KEY_F8 = UndefinedKey(KEY_F1)
KEY_F9 = UndefinedKey(KEY_F1)
KEY_F10 = UndefinedKey(KEY_F1)
KEY_F11 = UndefinedKey(KEY_F1)
KEY_F12 = UndefinedKey(KEY_F1)
KEY_SYSRQ = UndefinedKey(KEY_F1)
KEY_SCROLLLOCK = UndefinedKey(KEY_F1)
KEY_PAUSE = UndefinedKey(KEY_F1)
KEY_GRAVE = UndefinedKey(KEY_F1)
KEY_1 = UndefinedKey(KEY_F1)
KEY_2 = UndefinedKey(KEY_F1)
KEY_3 = UndefinedKey(KEY_F1)
KEY_4 = UndefinedKey(KEY_F1)
KEY_5 = UndefinedKey(KEY_F1)
KEY_6 = UndefinedKey(KEY_F1)
KEY_7 = UndefinedKey(KEY_F1)
KEY_8 = UndefinedKey(KEY_F1)
KEY_9 = UndefinedKey(KEY_F1)
KEY_0 = UndefinedKey(KEY_F1)
KEY_MINUX = UndefinedKey(KEY_F1)
KEY_EQUAL = UndefinedKey(KEY_F1)
KEY_BACKSPACE = UndefinedKey(KEY_F1)
KEY_INSERT = UndefinedKey(KEY_F1)
KEY_HOME = UndefinedKey(KEY_F1)
KEY_PAGEUP = UndefinedKey(KEY_F1)
KEY_NUMLOCK = UndefinedKey(KEY_F1)
KEY_KPSPLASH = UndefinedKey(KEY_F1)
KEY_KPASTERISK = UndefinedKey(KEY_F1)
KEY_KPMINUS = UndefinedKey(KEY_F1)
KEY_TAB = UndefinedKey(KEY_F1)
KEY_Q = WebBinding('https://www.youtube.com', '2', 'True')
KEY_W = UndefinedKey(KEY_F1)
KEY_E = UndefinedKey(KEY_F1)
KEY_R = UndefinedKey(KEY_F1)
KEY_T = UndefinedKey(KEY_F1)
KEY_Y = UndefinedKey(KEY_F1)
KEY_U = UndefinedKey(KEY_F1)
KEY_I = UndefinedKey(KEY_F1)
KEY_O = UndefinedKey(KEY_F1)
KEY_P = UndefinedKey(KEY_F1)
KEY_LEFTBRACE = UndefinedKey(KEY_F1)
KEY_RIGHTBRACE = UndefinedKey(KEY_F1)
KEY_BACKSLASH = UndefinedKey(KEY_F1)
KEY_DELETE = UndefinedKey(KEY_F1)
KEY_END = UndefinedKey(KEY_F1)
KEY_PAGEDOWN = UndefinedKey(KEY_F1)
KEY_KP7 = UndefinedKey(KEY_F1)
KEY_KP8 = UndefinedKey(KEY_F1)
KEY_KP9 = UndefinedKey(KEY_F1)
KEY_KPPLUS = UndefinedKey(KEY_F1)
KEY_CAPSLOCK = UndefinedKey(KEY_F1)
KEY_A = UndefinedKey(KEY_F1)
KEY_S = UndefinedKey(KEY_F1)
KEY_D = UndefinedKey(KEY_F1)
KEY_F = UndefinedKey(KEY_F1)
KEY_G = UndefinedKey(KEY_F1)
KEY_H = UndefinedKey(KEY_F1)
KEY_J = UndefinedKey(KEY_F1)
KEY_K = UndefinedKey(KEY_F1)
KEY_L = UndefinedKey(KEY_F1)
KEY_SEMICOLON = UndefinedKey(KEY_F1)
KEY_APOSTROPHE = UndefinedKey(KEY_F1)
KEY_ENTER = UndefinedKey(KEY_F1)
KEY_KP4 = UndefinedKey(KEY_F1)
KEY_KP5 = UndefinedKey(KEY_F1)
KEY_KP6 = UndefinedKey(KEY_F1)
KEY_LEFTSHIFT = UndefinedKey(KEY_F1)
KEY_Z = UndefinedKey(KEY_F1)
KEY_X = MacroBinding('KEY_X', ['KEY_LEFTALT', 'KEY_F4'])
KEY_C = UndefinedKey(KEY_F1)
KEY_V = UndefinedKey(KEY_F1)
KEY_B = UndefinedKey(KEY_F1)
KEY_N = UndefinedKey(KEY_F1)
KEY_M = UndefinedKey(KEY_F1)
KEY_COMMA = UndefinedKey(KEY_F1)
KEY_DOT = UndefinedKey(KEY_F1)
KEY_SLASH = UndefinedKey(KEY_F1)
KEY_RIGHTSHIFT = UndefinedKey(KEY_F1)
KEY_UP = UndefinedKey(KEY_F1)
KEY_KP1 = UndefinedKey(KEY_F1)
KEY_KP2 = UndefinedKey(KEY_F1)
KEY_KP3 = UndefinedKey(KEY_F1)
KEY_KPENTER = UndefinedKey(KEY_F1)
KEY_LEFTCTRL = UndefinedKey(KEY_F1)
KEY_LEFTMETA = UndefinedKey(KEY_F1)
KEY_LEFTALT = UndefinedKey(KEY_F1)
KEY_SPACE = UndefinedKey(KEY_F1)
KEY_RIGHTALT = UndefinedKey(KEY_F1)
KEY_RIGHTMETA = UndefinedKey(KEY_F1)
KEY_COMPOSE = UndefinedKey(KEY_F1)
KEY_RIGHTCTRL = UndefinedKey(KEY_F1)
KEY_LEFT = UndefinedKey(KEY_F1)
KEY_DOWN = UndefinedKey(KEY_F1)
KEY_RIGHT = UndefinedKey(KEY_F1)
KEY_KP0 = UndefinedKey(KEY_F1)
KEY_KPDOT = UndefinedKey(KEY_F1)


bindings = {'KEY_ESC': KEY_ESC, 'KEY_F1': KEY_F1, 'KEY_F2': KEY_F2, 'KEY_F3': KEY_F3, 'KEY_F4': KEY_F4, 'KEY_F5': KEY_F5, 'KEY_F6': KEY_F6, 'KEY_F7': KEY_F7, 'KEY_F8': KEY_F8, 'KEY_F9': KEY_F9,
        'KEY_F10': KEY_F10, 'KEY_F11': KEY_F11, 'KEY_F12': KEY_F12, 'KEY_SYSRQ': KEY_SYSRQ, 'KEY_SCROLLLOCK': KEY_SCROLLLOCK, 'KEY_PAUSE': KEY_PAUSE, 'KEY_GRAVE': KEY_GRAVE, 'KEY_1': KEY_1,
        'KEY_2': KEY_2, 'KEY_3': KEY_3, 'KEY_4': KEY_4, 'KEY_5': KEY_5, 'KEY_6': KEY_6, 'KEY_7': KEY_7, 'KEY_8': KEY_8, 'KEY_9': KEY_9, 'KEY_0': KEY_0, 'KEY_MINUS': KEY_MINUS, 'KEY_EQUAL': KEY_EQUAL,
        'KEY_BACKSPACE': KEY_BACKSPACE, 'KEY_INSERT': KEY_INSERT, 'KEY_HOME': KEY_HOME, 'KEY_PAGEUP': KEY_PAGEUP, 'KEY_NUMLOCK': KEY_NUMLOCK, 'KEY_KPSLASH': KEY_KPSLASH,
        'KEY_KPASTERISK': KEY_KPASTERISK, 'KEY_KPMINUS': KEY_KPMINUS, 'KEY_TAB': KEY_TAB, 'KEY_Q': KEY_Q, 'KEY_W': KEY_W, 'KEY_E': KEY_E, 'KEY_R': KEY_R, 'KEY_T': KEY_T, 'KEY_Y': KEY_Y,
        'KEY_U': KEY_U, 'KEY_I': KEY_I, 'KEY_O': KEY_O, 'KEY_P': KEY_P, 'KEY_LEFTBRACE': KEY_LEFTBRACE, 'KEY_RIGHTBRACE': KEY_RIGHTBRACE, 'KEY_BACKSLASH': KEY_BACKSLASH,
        'KEY_DELETE': KEY_DELETE, 'KEY_END': KEY_END, 'KEY_PAGEDOWN': KEY_PAGEDOWN, 'KEY_KP7': KEY_KP7, 'KEY_KP8': KEY_KP8, 'KEY_KP9': KEY_KP9, 'KEY_KPPLUS': KEY_KPPLUS,
        'KEY_CAPSLOCK': KEY_CAPSLOCK, 'KEY_A': KEY_A, 'KEY_S': KEY_S, 'KEY_D': KEY_D, 'KEY_F': KEY_F, 'KEY_G': KEY_G, 'KEY_H': KEY_H, 'KEY_J': KEY_J, 'KEY_K': KEY_K, 'KEY_L': KEY_L,
        'KEY_SEMICOLON': KEY_SEMICOLON, 'KEY_APOSTROPHE': KEY_APOSTROPHE, 'KEY_ENTER': KEY_ENTER, 'KEY_KP4': KEY_KP4, 'KEY_KP5': KEY_KP5, 'KEY_KP6': KEY_KP6,
        'KEY_LEFTSHIFT': KEY_LEFTSHIFT, 'KEY_Z': KEY_Z, 'KEY_X': KEY_X, 'KEY_C': KEY_C, 'KEY_V': KEY_V, 'KEY_B': KEY_B, 'KEY_N': KEY_N, 'KEY_M': KEY_M, 'KEY_COMMA': KEY_COMMA, 'KEY_DOT': KEY_DOT,
        'KEY_SLASH': KEY_SLASH, 'KEY_RIGHTSHIFT': KEY_RIGHTSHIFT, 'KEY_UP': KEY_UP, 'KEY_KP1': KEY_KP1, 'KEY_KP2': KEY_KP2, 'KEY_KP3': KEY_KP3, 'KEY_KPENTER': KEY_KPENTER,
        'KEY_LEFTCTRL': KEY_LEFTCTRL, 'KEY_LEFTMETA': KEY_LEFTMETA, 'KEY_LEFTALT': KEY_LEFTALT, 'KEY_SPACE': KEY_SPACE, 'KEY_RIGHTALT': KEY_RIGHTALT, 'KEY_RIGHTMETA': KEY_RIGHTMETA,
        'KEY_COMPOSE': KEY_COMPOSE, 'KEY_RIGHTCTRL': KEY_RIGHTCTRL, 'KEY_LEFT': KEY_LEFT, 'KEY_DOWN': KEY_DOWN, 'KEY_RIGHT': KEY_RIGHT, 'KEY_KP0': KEY_KP0, 'KEY_KPDOT': KEY_KPDOT}


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
