from functions import get_todos, write_todos
import time

now = time.strftime("%B %d, %Y %I:%M%p")

print(now)
while True:
    #Get user input and strip space chars
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    #Check users action
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()


        for index,item in enumerate(todos):
             item = item.strip('\n')
             row = f"{index + 1}) {item}"
             print(row)


    elif user_action.startswith('complete'):
          number = int(user_action[9:])

          todos = get_todos("todos.txt")
          index = number -1
          todos_removed = todos[index].strip("\n")
          todos.pop(index)

          write_todos(todos)

          print(f"Todo {todos_removed} was removed from the list.")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number -= 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('exit'):
          break
    else:
        print("Command is not valid.")
print('Bye')




