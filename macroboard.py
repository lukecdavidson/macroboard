#! /usr/bin/python -u

from evdev import UInput, InputDevice, categorize, ecodes
import webbrowser
import subprocess
import configparser

## Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

## Grab input device specified in config file
keyboard = config['General']['Keyboard']
dev = InputDevice(keyboard)
dev.grab()


ui = UInput()


## Inject keys as a macro. All keys are pressed and released at the same time 
def write_macro(macro):
    for i in macro:
        key_number = ecodes.ecodes[i]
        ui.write(ecodes.EV_KEY, key_number, 1)
        ui.syn()
    for i in macro:
        key_number = ecodes.ecodes[i]
        ui.write(ecodes.EV_KEY, key_number, 0)
        ui.syn()


## check bind type and execute associated bind
def execute_bind():
    if key.keycode in config:
        if config[key.keycode]['Type'] == 'macro':
            macro_string = config[key.keycode]['Value']
            macro_list = macro_string.split(" ")
            macro = ['KEY_' + s for s in macro_list]
            write_macro(macro)
        elif config[key.keycode]['Type'] == 'string':
            string_string = config[key.keycode]['Value']
            string = string_string.split(" ")
            write_string(string)
        elif config[key.keycode]['Type'] == 'web':
            web = config[key.keycode]
            website = web['Value']
            window = int(web.get('Window', '2'))
            autoraise = web.getboolean('Autoraise', 'True')
            webbrowser.open(website,new=window,autoraise=autoraise)
        else:
            error_msg = 'Key must be a web or input type. Key is currently set to the type: '
            print(error_msg + config[key.keycode]['Type'])
            subprocess.call(['notify-send', '-u', 'low', 'MacroBoard', error_msg + config[key.keycode]['Type']])
    else:
        error_msg = 'No acton assigned to '
        print(error_msg + key.keycode)
        subprocess.call(['notify-send', '-u', 'low', 'MacroBoard', error_msg + key.keycode])


## Loop to read input from device 
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_ESC':
                quit()
            else:
                execute_bind()
