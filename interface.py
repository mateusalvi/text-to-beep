import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text (" ",size=(10, 1))],
            [sg.Text (" ",size=(14, 1)), sg.Text("TEXT-TO-BEEP",justification='center',size=(20, 1),font=['halvetica',30]), ],     # Part 2 - The Layout
            [sg.Multiline(default_text='',size=(75, 25),font='halvetica'), ],
            [sg.Text (" ",size=(10, 1))],
            [sg.Text (" ",size=(20, 2)), sg.Button('Tocar música',font='halvetica'), sg.Text(" ",size=(10, 2)), sg.Button('Parar música',font='halvetica'), ],
            [sg.Text (" ",size=(10, 1))],
         ]

# Create the window
window = sg.Window('Text-to-Beep', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()    