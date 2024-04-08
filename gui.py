import functions
import PySimpleGUI as sg

#Define layout
layout = [
    #row1
    [sg.Text('Enter a todo: ')],
    [sg.InputText(tooltip="Enter todo", key='todo'),
     sg.Button("Add")],
    #row2
    [sg.Listbox(values=functions.get_todos(), key='todos',
                enable_events=True, size=[45, 10]),
     sg.Button("Edit")]
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print('Edit values:', values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todos_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todos_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
