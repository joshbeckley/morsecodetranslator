from pynput import keyboard 
import time

code_morse = ""
continue_reading = True
is_terminated = True

# Converts the seconds pressed into a dash or dot
def convert_seconds_symbol(seconds):
    if seconds <= 0.20: # Dot 
        return '.'
    else: # Dash
        return '-'

# Converts the morse code into character
def convert_morse(morse):
    codes = {
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z',
    '.----':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
    '-----':'0',
    '.-.-.-':'.',
    '--..--':',',
    '..--..':'?',
}
    character = codes[morse] # Returns the character of the corresponding morse code
    return character

    
def on_key_release(key): 
    global continue_reading
    global is_terminated
    if key == keyboard.Key.tab: # Stop the current reading
        continue_reading = False
    elif key == keyboard.Key.shift_l: # Terminate program
        is_terminated = False
    else: # Take keypress time
        time_taken = round(time.time() - t, 2) # Total time taken from onpress to onrelease

        # Adding to the message
        global code_morse
        code_morse += convert_seconds_symbol(time_taken)
    return False # Stop the listener

def on_key_press(key):
    return False # Stop the listener

# Entire program loop
while is_terminated:

    # Reading single character loop
    while continue_reading:
        with keyboard.Listener(on_press = on_key_press) as press_listener: #setting code for listening key-press
            press_listener.join()

        t = time.time() # Reading current time

        with keyboard.Listener(on_release = on_key_release) as release_listener: #setting code for listening key-release
            release_listener.join()

    print(convert_morse(code_morse))

    # Reset the values
    code_morse = ""
    continue_reading = True
    
    

