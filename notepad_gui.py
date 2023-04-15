import PySimpleGUI as sg


layout = [
    [sg.Text('Enter a note:'), sg.InputText()],
    [sg.Button('Create Note'), sg.Button('Exit')]
]


window = sg.Window('Notepad App', layout)


while True:
    event, values = window.Read()


    if event == 'Create Note':
        note = values[0]
        
        print(f'Note created: {note}')
    elif event == 'Exit':
        break
