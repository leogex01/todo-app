import functions
import PySimpleGUI as sg
import time
#Define layout

sg.theme('Black')
layout = [
    #row1
    [sg.Text('', key='clock')],
    [sg.Text('Enter a todo: ')],
    [sg.InputText(tooltip="Enter todo", key='todo'),
     sg.Button("Add")],
    #row2 edit-button
    [sg.Listbox(values=functions.get_todos(), key='todos',
                enable_events=True, size=[45, 10]),
     sg.Button("Edit"), sg.Button("Complete")],

    #row3
    [sg.Button('Exit')]


]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%B %d, %Y %H:%M:%S %p"))
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
            try:
                todos_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todos_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please choose an item to edit", font='Helvetica, 10')

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please choose an item to edit", font='Helvetica, 10')


        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
print('Bye')
window.close()
