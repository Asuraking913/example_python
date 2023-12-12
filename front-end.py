import PySimpleGUI as sg
from time import time

def create_window(theme):
    sg.theme(theme)

    layout = [
        [sg.Push(), sg.Image('exit.png',enable_events=True, key = 'key-image')],
        [sg.VPush()], 
        [sg.Text('', key = 'key-text', font='young 50')],
        [sg.Button(
            'Start', 
            button_color=('white', 'red'), 
            key = 'key-start'
        ),
        sg.Button(
            'Lap', 
            button_color=('white', 'red'), 
            key = 'key-lap', 
            visible=False
        )
        ],
        [sg.Column([[]], key='key-column')],
        [sg.VPush()]
    ]
    return sg.Window('Stopwatch', layout, no_titlebar=True, element_justification='center', size= (300, 300))


window = create_window('black')
active = False
start_time = 0
layout_amount = 1

while True:
    
    event, value = window.read(timeout=10)

    if event == 'key-image':
        break

    if event == 'key-start':
        if active:
            active = False
            window['key-start'].update('Reset')
            window['key-lap'].update(visible = False)
        
        else:
            if start_time > 0:
                window.close()
                window = create_window('black')
                start_time = 0
                layout_amount = 1
            
            else:
                active = True
                start_time = time()
                window['key-start'].update('Stop')
                window['key-lap'].update(visible = True)
    
    if active:
        elasped_time = round(time() - start_time, 1)
        window['key-text'].update(elasped_time)

    if event == 'key-lap':
        window.extend_layout(window['key-column'], [[sg.Text(f'{layout_amount}'), sg.VSeparator(), sg.Text(f'{elasped_time} secs')]])
        layout_amount += 1



window.close()