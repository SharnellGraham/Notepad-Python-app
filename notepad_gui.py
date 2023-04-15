import PySimpleGUI as sg


layout = [
    [sg.Text('Enter a note:'), sg.InputText()],
    [sg.Button('Create Note'), sg.Button('Exit')]
]


window = sg.Window('Notepad App', layout)