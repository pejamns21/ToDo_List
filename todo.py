from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1


def input_check():
    if input_task.get() == '':
        messagebox.showerror("NO input")
        return 0
    return 1


def submit():
    global counter

    value = input_check()
    if value == 0:
        return

    content = input_task.get() + "\n"
    input_task.delete(0, END)
    tasks_list.append(content)

    to_do_list.insert('end -1 chars', str(counter) + ' -  ' + content)
    counter += 1


def delete():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return

    number = delete_task.get(1.0, END)

    if number == "\n" or int(number) == 0 or int(number) >= counter:
        messagebox.showerror("invalid")
        delete_task.delete(0.0, END)
        return
    else:
        delete_task.delete(0.0, END)

        task_num = int(number)
        tasks_list.pop(task_num - 1)
        counter -= 1

        to_do_list.delete(1.0, END)

        for i in range(len(tasks_list)):
            to_do_list.insert('end -1 chars', str(i + 1) + " -  " + tasks_list[i])


def exit_pr():
    master.quit()


if __name__ == '__main__':

    master = Tk()
    master.title('To Do List')
    master.iconbitmap('logo.ico')
    master.config(background="SteelBlue1")
    master.geometry('252x320')

    to_do_list = Text(master, height=2, width=14, font="helvetica  13")
    to_do_list.grid(row=0, column=0, ipadx=57, ipady=50, padx=(4, 2), pady=(5, 0), columnspan=3)

    input_task_label = Label(master, text="Enter your tasks", bg="MediumPurple1")
    input_task_label.grid(row=1, column=0, columnspan=3, pady=(5, 0), ipadx=75)

    input_task = Entry(master, borderwidth=2)
    input_task.grid(row=2, column=0, ipadx=57, columnspan=3, pady=(5, 0))

    submit_btn = Button(master, text="Submit", command=submit, bg="green2")
    submit_btn.grid(row=3, pady=(3, 0), columnspan=3, ipadx=95)

    delete_task_label = Label(master, text="Delete Task", bg="MediumPurple1")
    delete_task_label.grid(row=4, column=0, pady=(5, 0))

    delete_task = Text(master, height=1, width=2, font="helvetica  15")
    delete_task.grid(row=4, column=1, padx=(0, 5), pady=(5, 0))

    delete_btn = Button(master, text="Delete", command=delete, bg="red")
    delete_btn.grid(row=4, column=2, pady=(3, 0), ipadx=15)

    exit_btn = Button(master, text="EXIT", command=exit_pr, bg="red")
    exit_btn.grid(row=5, ipadx=100, columnspan=3, pady=(15, 0))

    master.mainloop()
