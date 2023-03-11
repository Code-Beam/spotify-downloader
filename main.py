import subprocess as sp
import PySimpleGUI as sg
import os
from termcolor import colored

# List of Required modules
required_modules = ["spotdl", "termcolor", "pysimplegui"]

# Check if each required module is installed
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        # If the module is not installed, install it with pip
        sp.call(['pip', 'install', module])

# Text for Intro
intro = """
███████╗██████╗  ██████╗ ████████╗██╗ ██████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
███████╗██████╔╝██║   ██║   ██║   ██║██║     ██████╔╝██║   ██║██║ █╗ ██║██╔██╗ ██║
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██║     ██╔══██╗██║   ██║██║███╗██║██║╚██╗██║
███████║██║     ╚██████╔╝   ██║   ██║╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚████║
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

By WvijayW
"""

# Use Termcolor to change the color of intro
text = colored(intro,"green")

# Define the GUI layout
layout = [[sg.Text('Enter URL:'), sg.InputText(key='url')],
          [sg.Button('Download'), sg.Button('Cancel')],
          [sg.Text('The proccess takes time , somtimes it may say not responding, it means that its working, to view the downloaded files check the directory this file is in, to see if the proccess has started check the terminal! -WvijayW')]]

# Create the PySimpleGUI window
window = sg.Window('Spotify Downloader', layout, background_color='#1DB954',
                   element_padding=(5, 5), finalize=True)

# Loop to process window events
while True:
    if os.name == 'posix':  # for UNIX-like systems (e.g. Linux, macOS)
        os.system('clear')
    else:  # for Windows
        os.system('cls')
    
    print(text)

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Download':
        url = values['url']
        if url.startswith('https://open.spotify.com/'):
            # Call spotdl using subprocess
            sp.run(['python','-m','spotdl', url])
        else:
            sg.popup('Invalid URL', title='Error', background_color='#1DB954')

# Close the window
window.close()
