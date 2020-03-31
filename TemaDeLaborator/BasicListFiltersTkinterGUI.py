import tkinter as tk

def save_input():
    input_value = array_list_entry.get("1.0", "end-1c")

    print(input_value)

def print_result(var):
    result_field.set(var)


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
    canvas = tk.Canvas(window, borderwidth=0, highlightthickness=0, bg="gray", width=100, height=20)
    canvas.place(x=0, y=0)
    label = canvas.create_text(5, 5, anchor="nw")
    canvas.itemconfig(label, text="List of Integers")

    # the entry field
    # array_list = tk.StringVar()
    # array_list.set('')
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
                                 command=lambda: print_result('bbb'))
    Button_FilterOdd.place(x=550, y=50)

    # the filter Primes button
    Button_FilterPrimes = tk.Button(window, text="Filter Primes", bg='gray', height=1, width=10,
                                 command=lambda: print_result('ccc'))
    Button_FilterPrimes.place(x=550, y=80)

    # the filter odd button
    Button_Sum = tk.Button(window, text="Sum numbers", bg='gray', height=1, width=10,
                                 command=lambda: print_result('ddd'))
    Button_Sum.place(x=550, y=110)

    # main loop
    window.mainloop()
