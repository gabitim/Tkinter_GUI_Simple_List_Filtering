import tkinter as tk
from multiprocessing import Process, Queue
from collections import deque



# function witch selects the respective process
# and calls the printing function(the printing in the result box doesnt work right now)
def select_option(select):
    if select == 0:
        process0.start()
    elif select == 1:
        process1.start()
    elif select == 2:
        process2.start()

    print_result()

# filter odd process (test)
def filter_odd(list_queue,result):
    if not list_queue.empty():
        elem = list_queue.get()
        print(elem[0])
        result += elem[0]
        print(result)
    else:
        result = "INSERT NUMBERS"

# filter primes process (test)
def filter_primes(list_queue, result):
    if not list_queue.empty():
        elem = list_queue.get()
        print(elem[1])
        result = elem[1]
    else:
        result = "INSERT NUMBERS"

# sum numbers process (test)
def sum_numbers(list_queue, result):
    if not list_queue.empty():
        elem = list_queue.get()
        print(elem[2])
        result = elem[2]
    else:
        result = "INSERT NUMBERS"


# the message queue used for sending the lists
list_queue = Queue()

# output in result field (not good!!, doesnt work to print from process)
result = "asc"

# declaring the processes
process0 = Process(target=filter_odd, args=(list_queue,result))
process1 = Process(target=filter_primes, args=(list_queue,result))
process2 = Process(target=sum_numbers, args=(list_queue,result))

# function to save input and transforms the input into a list
def save_input():
    input_value = array_list_entry.get("1.0", "end-1c")
    array_list_entry.delete('1.0',tk.END)
    list = input_value.split(',')

    list_queue.put(list)
    # print_result()

# function which prints in result field
def print_result():
    result_field.set(result)

# noinspection PyInterpreter
if __name__ == "__main__":
    # create a GUI window
    window = tk.Tk()

    # set the title
    window.title("ListFilters")

    # set the background colour of G UI window
    window.configure(background='gray')

    # set the configuration of GUI window
    window.geometry("640x300")

    # "List of Integers" label
    canvas = tk.Canvas(window, borderwidth=0, highlightthickness=0, bg="gray", width=110, height=60)
    canvas.place(x=0, y=0)
    label = canvas.create_text(5, 5, anchor="nw")
    canvas.itemconfig(label, text="List of Integers \n add numbers with \n ',' between them")

    # the entry field
    empty_the_entry_field = tk.StringVar()
    array_list_entry = tk.Text(window, height = 1, width=50)
    array_list_entry.pack(pady=5)

    # the result field
    result_field = tk.StringVar()
    result_field.set('')

    result_field_entry = tk.Entry(window, textvariable=result_field)
    result_field_entry.pack(ipadx=140, ipady=50, pady=5)

    # the add list button
    Button_addList = tk.Button(window, text="Add list", bg='gray', height=1, width=7,
                               command=lambda: save_input())
    Button_addList.place(x=550, y=5)

    # the filter odd button
    Button_FilterOdd = tk.Button(window, text="Filter Odd", bg='gray', height=1, width=10,
                                 command=lambda: select_option(0))
    Button_FilterOdd.place(x=550, y=50)

    # the filter Primes button
    Button_FilterPrimes = tk.Button(window, text="Filter Primes", bg='gray', height=1, width=10,
                                 command=lambda: select_option(1))
    Button_FilterPrimes.place(x=550, y=80)

    # the filter odd button
    Button_Sum = tk.Button(window, text="Sum numbers", bg='gray', height=1, width=10,
                                 command=lambda: select_option(2))
    Button_Sum.place(x=550, y=110)



    # main loop
    window.mainloop()
