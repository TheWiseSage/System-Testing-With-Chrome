# CPU / RAM / Temperature testing software.

# This program opens sequential google chrome tabs at a rate of 10 a second.

# it will then print the number of tabs currently open each second to the command line.

# The monitoring of  your system's status shall be handled by the end user with their
# operating system's tools.

# NOTE uncommenting line(s) ____ and ____ will cause Windows 10 to open the status
# monitors for you. if this feature is enabled you must allow the program to run unimpeded
# with exception of the control keys.

# Pressing  the "S" key will pause the program.
# Pressing the "S" key a second time will resume the program.
# Pressing the "E" key will terminate the program and close the browser
# NOTE: closing the browser may take some time depending on th number of tabs open. 


import keyboard
import webbrowser as wb
import PySimpleGUI as sg
from time import sleep
import threading
from pynput.keyboard import Listener, KeyCode

# VARIABLES

tabsOpen = 0 # Number of open tabs to be printed

itNumber = 2 # Number of iterations for the tabs code

start_stop_key = KeyCode(char='s') # Defines the start and stop key as s
exit_key = KeyCode(char='e') # Defines the exit key as e
delay = 0.1 

Chrome1 = ('https://www.youtube.com/watch?v=i8xOx3xl_-k') # The 5 chrome sites to open
Chrome2 = ('https://www.newgrounds.com/')
Chrome3 = ('https://www.reddit.com/')
Chrome4=('https://www.lttstore.com/')
Chrome5=('https://linustechtips.com/main/')

# Layout of interface window

layout=[[sg.Text('System Testing With Chrome')], # Defines layout of the window and titles it
        [sg.Button('BEGIN TEST'), sg.Button('ABORT')]]


# Create the interface window

window = sg.Window('System Testing With Chrome').Layout(layout) # Creates the window

# Read the interface window

button,values=window.Read()

# Control --------------------------------------------------------------

# ABORT Button

if button=='ABORT':  # Defines actions on initial GUI window Abort button
    window.close(); del window

# BEGIN TEST Button

if button=='BEGIN TEST': # Defines actions on initial GUI window Begin Test button
    window.close(); del window # Closes the first GUI window with the choices
    class opening(threading.Thread): 
        def _init_(self, delay, button):
            super(opening, self)._init_()
            self.delay = delay
            self.button = button
            self.running = False
            self.program_running = True

        def start_opening(self):
            self.running = True

        def stop_opening(self):
            self.running = False

        def exit(self):
            self.stop_opening()
            self.program_running = False

        def run(self):
            while self.program_running:
                while self.running:
                    for x in range(itNumber): # Repeats the following code a number of times
                        sleep(1)
                        # Defines the popup window to display the number of tabs open.
                        sg.popup('Tabs Open ' +str(tabsOpen), title='Tabs Currently Open',
                                 auto_close=True, auto_close_duration=0.9)
                        for x in range(1): # iterates through the urls provided
                           testTab = [Chrome1, Chrome2, Chrome3, Chrome4, Chrome5]
                           for x in testTab:
                               openTab = x
                               wb.open(x, new=2)
                               tabsOpen=tabsOpen+2

        sleep(delay)
        sleep(0.1)
click_thread = opening()
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_opening()
        else:
            click_thread.start_opening()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
