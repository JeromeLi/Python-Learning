import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'),sg.Spin(['item1','item2','item3'])],
    [sg.Button('Button', key = 'Button1')],
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button')]
]
window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Button1':
        print('button1 pressed')

    if event == 'Test Button':
        print('Test button pressed')

    if event == '-TEXT-':
        print('Text changed to:')

window.close()