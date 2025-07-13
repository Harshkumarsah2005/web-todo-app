#read the file and make it in list
def get_todo(filepath= "task.txt"):
    with open(filepath, 'r') as file_local:
        task_local= file_local.readlines( )
    return task_local

#write the to-do items in the text file
def write_todo(task_arg, filepath= "task.txt"):
    with open(filepath, 'w') as file:
        for task in task_arg:
            file.writelines(task.strip()+ '\n')

if __name__== "__main__":
    print("hello")
    print(get_todo( ))