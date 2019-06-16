# Credit goes to Karim Zaher

import tkinter as tk

# ///// Initialize Variables /////
WIDTH = 200
HEIGHT = 300
Operations = ['+', '-', '/', '*']
DataStore = []


def clear(clearType):  # Occurs when 'C' button pressed
    if clearType == "Button":
        label['text'] = ""
        label2['text'] = ""
        DataStore.clear()
    elif clearType == 'Prior':
        label['text'] = ""


def equal(equalType):
    if equalType == "Button":  # Occurs if '=' button pressed
        label3['text'] = ''
        DataStore.append(label['text'])
        num_sentence = "".join(DataStore)
        label2['text'] = eval(num_sentence)
        label['text'] = ""
        DataStore.clear()
    elif equalType == "Prior":  # Occurs if an operator button is clicked after two values are entered into calculator
        num_sentence = "".join(DataStore)  # Turns DataStore array into a string
        label2['text'] = eval(num_sentence)
        DataStore.clear()
        DataStore.append(str(label2['text']))


def button(value):
    try:  # Checks what button is clicked
        if value == '.':  # Checks for decimal point
            if value in label['text']:  # If decimal exists, don't add another one
                pass
            else:
                if label['text'] == "":
                    label['text'] += "0"
                label["text"] += value
        else:  # Checks if number button is clicked
            int(value)
            label['text'] += value
    except ValueError:  # If attempt to convert the button clicked into an integer fails, assume that sign is pressed
        if value == "SIGN":
            try:
                label['text'] = str(int(label['text']) * -1)
            except:
                label['text'] = str(float(label['text']) * -1)
        if value == "ADD":
            label3['text'] = '+'
            if DataStore == []:
                label2['text'] = label['text']
            try:
                if (DataStore[-1] in Operations) and (DataStore[-1] != '+') and (label['text'] == ""):
                    DataStore[-1] = '+'
            except:
                for i in DataStore:
                    if i in Operations:
                        equal('Prior')
            if ((DataStore != []) and ((DataStore[-1] not in Operations) or (label['text'] != ''))) or (
                    (DataStore == []) and (label['text'] != '')):
                DataStore.append(label['text'])
                equal('Prior')
                DataStore.append('+')
                clear("Prior")
        if value == "SUBTRACT":
            label3['text'] = '-'
            if DataStore == []:
                label2['text'] = label['text']
            try:
                if (DataStore[-1] in Operations) and (DataStore[-1] != '-') and (label['text'] == ""):
                    DataStore[-1] = '-'
            except IndexError:
                for i in DataStore:
                    if i in Operations:
                        equal('Prior')
            if ((DataStore != []) and ((DataStore[-1] not in Operations) or (label['text'] != ''))) or (
                    (DataStore == []) and (label['text'] != '')):
                DataStore.append(label['text'])
                equal('Prior')
                DataStore.append('-')
                clear("Prior")
        if value == "MULTIPLY":
            label3['text'] = '*'
            if DataStore == []:
                label2['text'] = label['text']
            try:
                if (DataStore[-1] in Operations) and (DataStore[-1] != '*') and (label['text'] == ""):
                    DataStore[-1] = '*'
            except IndexError:
                for i in DataStore:
                    if i in Operations:
                        equal('Prior')
            if ((DataStore != []) and ((DataStore[-1] not in Operations) or (label['text'] != ''))) or (
                    (DataStore == []) and (label['text'] != '')):
                DataStore.append(label['text'])
                equal('Prior')
                DataStore.append('*')
                clear("Prior")
        if value == "DIVIDE":
            label3['text'] = '/'
            if DataStore == []:
                label2['text'] = label['text']
            try:
                if (DataStore[-1] in Operations) and (DataStore[-1] != '/') and (label['text'] == ""):
                    DataStore[-1] = '/'
            except IndexError:
                for i in DataStore:
                    if i in Operations:
                        equal('Prior')
            if ((DataStore != []) and ((DataStore[-1] not in Operations) or (label['text'] != ''))) or (
                    (DataStore == []) and (label['text'] != '')):
                DataStore.append(label['text'])
                equal('Prior')
                DataStore.append('/')
                clear("Prior")


# ///// Create GUI /////
root = tk.Tk()

# Set initial width and height of window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Initial gray background
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='gray')
canvas.place(relwidth=1, relheight=1)

# Frame that stores the Label
frame = tk.Frame(root, bg='orange', bd=2)
frame.place(relx=0.5, rely=0.05, anchor='n', relwidth=0.75, relheight=0.2)

# Orange background -- Shows inputted numbers
label = tk.Label(frame, bg='orange', text="", anchor='se', font=('Courier', 20))
label.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

label2 = tk.Label(frame, bg='orange', text="", anchor='ne', font=('Courier', 20))
label2.place(relx=0, rely=0, relwidth=1, relheight=0.5)

label3 = tk.Label(frame, bg='red', fg='white', text="", anchor='nw', font=('Courier', 20))
label3.place(relx=0, rely=0, relwidth=0.1, relheight=0.3)

# Frame that stores the Buttons
frame_number = tk.Frame(root, bg='#80c1ff', bd=1)
frame_number.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.35, anchor='n')

# Frame that stores the Operators
frame_operator = tk.Frame(root, bg='#db4242', bd=1)
frame_operator.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.18, anchor='n')

# Number Pad GUI
button_DECIMAL = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='.',
                           command=lambda: button('.'))
button_DECIMAL.grid(row=3, column=0, ipadx=19, ipady=2)

button_0 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='0', command=lambda: button('0'))
button_0.grid(row=3, column=1, ipadx=17, ipady=2)

button_CLEAR = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='C',
                         command=lambda: clear('Button'))
button_CLEAR.grid(row=3, column=2, ipadx=16.27, ipady=2)

button_1 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='1', command=lambda: button('1'))
button_1.grid(row=2, column=0, ipadx=17, ipady=2)

button_2 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='2', command=lambda: button('2'))
button_2.grid(row=2, column=1, ipadx=17, ipady=2)

button_3 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='3', command=lambda: button('3'))
button_3.grid(row=2, column=2, ipadx=17, ipady=2)

button_4 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='4', command=lambda: button('4'))
button_4.grid(row=1, column=0, ipadx=17, ipady=2)

button_5 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='5', command=lambda: button('5'))
button_5.grid(row=1, column=1, ipadx=17, ipady=2)

button_6 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='6', command=lambda: button('6'))
button_6.grid(row=1, column=2, ipadx=17, ipady=2)

button_7 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='7', command=lambda: button('7'))
button_7.grid(row=0, column=0, ipadx=17, ipady=2)

button_8 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='8', command=lambda: button('8'))
button_8.grid(row=0, column=1, ipadx=17, ipady=2)

button_9 = tk.Button(frame_number, highlightbackground='#80c1ff', relief='flat', text='9', command=lambda: button('9'))
button_9.grid(row=0, column=2, ipadx=17, ipady=2)

# Operations Pad GUI
button_SUBTRACT = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text='-',
                            command=lambda: button('SUBTRACT'))
button_SUBTRACT.grid(row=0, column=0, ipadx=17, ipady=2)

button_EQUAL = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text='=',
                         command=lambda: equal('Button'))
button_EQUAL.grid(row=0, column=2, ipadx=17, ipady=2)

button_ADD = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text='+',
                       command=lambda: button('ADD'))
button_ADD.grid(row=0, column=1, ipadx=17, ipady=2)

button_MULTIPLY = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text='*',
                            command=lambda: button('MULTIPLY'))
button_MULTIPLY.grid(row=1, column=0, ipadx=17, ipady=2)

button_DIVIDE = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text='/',
                          command=lambda: button('DIVIDE'))
button_DIVIDE.grid(row=1, column=1, ipadx=18, ipady=2)

button_SIGN = tk.Button(frame_operator, highlightbackground='#db4242', relief='flat', text="+/-",
                        command=lambda: button('SIGN'))
button_SIGN.grid(row=1, column=2, ipadx=10, ipady=2)

tk.mainloop()
