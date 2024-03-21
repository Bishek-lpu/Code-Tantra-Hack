import os
import time
try:
    import subprocess
except:
    os.system('pip install subprocess.run')

try:
    import keyboard
except:
    os.system('pip install keyboard')

try:
    import pyperclip
except:
    os.system('pip install pyperclip')



def main():
    print("Press the 'Esc' key to exit the loop.")
    while True:
        if keyboard.is_pressed('Esc'):
            print("Exiting the loop.")
            break

        elif keyboard.is_pressed('`'):
            # run Explorer
            subprocess.Popen(['explorer.exe'])
            time.sleep(1)

        elif keyboard.is_pressed('alt') and keyboard.is_pressed('v'):
            text = pyperclip.paste()
            keyboard.write(text)
            keyboard.press("alt")
            time.sleep(0.2)
            keyboard.release("alt")
            time.sleep(0.8)
            

            
if __name__ == "__main__":
    main()

