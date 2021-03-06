import tkinter as tk
from multiprocessing import Process, Queue

# the message queue used for sending the lists
list_queue = Queue()

# function witch selects the respective process
# and calls the printing function
def select_option(select):

    # declaring the processes
    process0 = Process(target=filter_odd, args=(list_queue,))
    process1 = Process(target=filter_primes, args=(list_queue,))
    process2 = Process(target=sum_numbers, args=(list_queue,))

    if select == 0:
        process0.start()  # starts the process (calls the function)
        process0.join()  # join the process( blocks the calling function until the process exit ! NOT finished) (still researching about behavior)
    elif select == 1:
        process1.start()
        process1.join()
    elif select == 2:
        process2.start()
        process2.join()

    print_result()


# filter odd process
def filter_odd(list_queue):
    if not list_queue.empty():
        # the entered list
        my_list = list_queue.get()

        filtered_list = filter(lambda it: it % 2 , my_list)

        # the final list
        odd_numbers_list = list(filtered_list)
        print(odd_numbers_list) # prints to console

        list_queue.put(odd_numbers_list) # puts the new list in the queue; right after this printing is called
                                        # outside of the function

    else:
        print("INSERT NUMBERS")

# filter primes process
def filter_primes(list_queue):
    if not list_queue.empty():
        my_list = list_queue.get()
        prime_numbers_list = []

        for elem in my_list:
            if elem <= 1:
                continue
            if elem <= 3:
                prime_numbers_list.append(elem)
                continue

            if elem % 2 == 0 or elem % 3 == 0:
                continue

            i = 5
            while i * i <= elem:
                if elem % i == 0 or elem % (i + 2) == 0:
                    continue
                i = i + 6

            prime_numbers_list.append(elem)

        print(prime_numbers_list)

        list_queue.put(prime_numbers_list)
    else:
        print("INSERT NUMBERS")

# sum numbers process
def sum_numbers(list_queue):
    if not list_queue.empty():
        my_list = list_queue.get()
        sum = 0
        for elem in my_list:
            sum += elem

        print(sum)
        list_queue.put(sum)

    else:
        print("INSERT NUMBERS")

# function which prints in result field
def print_result():
    if not list_queue.empty():
        result = list_queue.get()
        result_field.set(result)
    else:
        result_field.set('Press Add List Button')

# function to save input and transforms the input into a list
def save_input():
    # input value a string with the entry
    input_value = array_list_entry.get("1.0", "end-1c")
    if input_value == '':
        result_field.set('Enter numbers')

    # list with numbers after split
    list = input_value.split(',')

    # the list with integer values
    int_list = []

    # converting to int
    try:
        for number in list:
            int_list.append(int(number))
    except ValueError:
        result_field.set('Enter again more carefully! and than choose option')
    # print(int_list)

    list_queue.put(int_list)

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
