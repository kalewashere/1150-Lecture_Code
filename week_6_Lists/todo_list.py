todo_list = []  # this is an empty list

while True:
    task = input('Enter your task, or press enter to stop: ')
    if task:  # an empty string (user pressed enter) is noted as False
        if task in todo_list:
            print('You already added that task.')
        else:
            todo_list.append(task)
        todo_list.append(task)  # this adds task to todo_list - much like how .append() adds to end of already
        # established list
    else:
        break  # this tells loop to end if user pressed enter, an empty string "breaks out" of while loop

print('Thank you. Your tasks are: ')

# for task in todo_list:  # this will print every task in the todo_list
#     print(task)  # prints task --- converted to comment to try out enumerate

for index, task in enumerate(todo_list): # enumerate returns two values - index - counting along the list and list
    # item - element. Must tell loop to gather both for enumerate
    print(f'Task {index + 1} is {task}') # added + 1 to index to start counting from 1 instead of 0 - tried adding it to
    # task first but program did not like that, remembered i needed to add that to index bc that is what is counting


number_of_tasks = len(todo_list)
print(f'You have {number_of_tasks} tasks to do today.')  # f'string indicating how many tasks the user has entered
# we can also use len() in a shorter way, see below
# print(f'You have {len(todo_list)} tasks to complete today.') this way is more concise but both are correct

