import functions
import PySimpleGUI as sg

#Define layout
layout = [
    [sg.Text('Enter todo: '), sg.InputText(tooltip="Enter todo")],
    [sg.Button("Add")]
]

window = sg.Window('My To-Do App', layout)
window.read()
window.close()
