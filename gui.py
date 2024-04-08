import functions
import PySimpleGUI as sg

#Define layout
layout = [
    [sg.Text('Enter a todo: ')],
    [sg.InputText(tooltip="Enter todo", key='todo'),
     sg.Button("Add")]
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
