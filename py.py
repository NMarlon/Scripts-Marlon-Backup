#"""import re

#string = '  Hello  World   From Pankaj \t\n\r\tHi There  '

#print('Remove all spaces using RegEx:\n', re.sub(r"\s+", "", string), sep='')  # \s matches all white spaces
#print()

#print('Remove leading spaces using RegEx:\n', re.sub(r"^\s+", "", string), sep='')  # ^ matches start
#print()

#print('Remove trailing spaces using RegEx:\n', re.sub(r"\s+$", "", string), sep='')  # $ matches end
#print()

#print('Remove leading and trailing spaces using RegEx:\n', re.sub(r"^\s+|\s+$", "", string), sep='')  # | for OR condition
#"""

#import tkinter as tk
#import time
#"""import keyboard  # using module keyboard

#while True:  # making a loop
#    try:  # used try so that if user pressed other than the given key error will not be shown
#        if keyboard.is_pressed('q'):  # if key 'q' its pressed 
#            print('You Pressed A Key!')
#            break  # finishing the loop
#    except:
#        break  # if user pressed a key other than the given key the loop will break



#"""




#from pynput.keyboard import Key, Listener

#def on_press(key):
#    #print('{0} pressed'.format(key))

#def on_release(key):
#    print('{0} release'.format(key))
#    if key == Key.esc:
#        # Stop listener
#        return False

## Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()




#i=0
#while(i<4):


#	root = tk.Tk()
#	root.attributes("-fullscreen", True, "-topmost", True, "-disabled", True)
#	time_interrupt = 1500 # Time screen is active in ms

#	root.after(time_interrupt, root.destroy)

	
#	root.mainloop()

#	time.sleep(1.3)


#	i+=1



import keyboard
import time



stop = False
def onkeypress(event):
    global stop
    if event.name == 'q':
        stop = True

# ---------> hook event handler
keyboard.on_press(onkeypress)
# --------->

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        print("sleeping 5")
        time.sleep(1)
        print("sleeping 4")
        time.sleep(1)
        print("sleeping 3")
        time.sleep(1)
        print("sleeping 2")
        time.sleep(1)
        print("sleeping 1")
        time.sleep(1)
        print("slept")
        if stop:  # if key 'q' is pressed 
            print('You Pressed "q" Key!')
            break  
    except:
        print("#######")
        break