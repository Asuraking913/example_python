import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)

    layout = [
        [sg.Push(), sg.Image('exit.png',enable_events=True, key = 'key-image')],
        [sg.VPush()], 
        [sg.Text('', key = 'key-text')],
        [sg.Button(
            'Start', 
            button_color=('red', 'white'), 
            key = 'key-start'
        )
        ],
        [sg.Button(
            'Lap', 
            button_color=('red', 'white'), 
            key = 'key-lap'
        )
        ],
        [sg.Column([[]], key='key-column')]
        [sg.VPush()]
    ]
    return sg.Window('Stopwatch', layout, no_titlebar=True, element_justification='center', size= (300, 300))


window = create_window('black')