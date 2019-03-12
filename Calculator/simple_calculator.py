from tkinter import *
"""This is very simple calculator program."""
# Really old project. A lot to improve here still..

__author__ = 'Joanna Czernicka'
__copyright__ = 'Copyright 2016, simple_calculator'

root = Tk()
root.geometry("400x520+0+0")
root.configure(background='white')
root.title("My first calculator")

textInput = StringVar()
operator = ""


class MyButton(Button):
    """Class responsible for buttons appearance"""

    def __init__(self, parent, **options):
        Button.__init__(self, parent, **options)
        self['bg'] = 'white'
        self['font'] = ('arial', 40, 'bold')
        self['borderwidth'] = 0
        textInput.set("0")

        def enter(event):
            self.configure(bg='gray93')

        def leave(event):
            self.configure(bg='white')

        self.bind('<Enter>', enter)
        self.bind('<Leave>', leave)


def btn_click(numbers):
    global operator
    if len(operator) != 0 and '+-*/'.find(str(numbers)) >= 0 and '+-*/'.find(operator[-1]) >= 0:
        operator = operator[:-1]
    if not (len(operator) == 0 and numbers == 0):
        operator = operator + str(numbers)
        textInput.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    textInput.set("0")


def btn_equals_input():
    global operator
    sum_up = "%.5f" % eval(operator)
    sum_up = sum_up.rstrip("0")
    sum_up = sum_up.rstrip(".")
    textInput.set(sum_up)
    operator = sum_up


txtDisplay = Entry(root, font=('arial', 40, 'bold'), textvariable=textInput,
                   bg="gray93", justify='right',
                   fg="black").place(x=20, y=20, width=360, height=100)

# ==============NUMBERS======================
btn1 = MyButton(root, text='1',
                command=lambda: btn_click(1)).place(x=20, y=140,
                                                    width=90, height=90)
btn2 = MyButton(root, text='2',
                command=lambda: btn_click(2)).place(x=110, y=140,
                                                    width=90, height=90)
btn3 = MyButton(root, text='3',
                command=lambda: btn_click(3)).place(x=200, y=140,
                                                    width=90, height=90)
btn4 = MyButton(root, text='4',
                command=lambda: btn_click(4)).place(x=20, y=230,
                                                    width=90, height=90)
btn5 = MyButton(root, text='5',
                command=lambda: btn_click(5)).place(x=110, y=230,
                                                    width=90, height=90)
btn6 = MyButton(root, text='6',
                command=lambda: btn_click(6)).place(x=200, y=230,
                                                    width=90, height=90)
btn7 = MyButton(root, text='7',
                command=lambda: btn_click(7)).place(x=20, y=320,
                                                    width=90, height=90)
btn8 = MyButton(root, text='8',
                command=lambda: btn_click(8)).place(x=110, y=320,
                                                    width=90, height=90)
btn9 = MyButton(root, text='9',
                command=lambda: btn_click(9)).place(x=200, y=320,
                                                    width=90, height=90)
btn0 = MyButton(root, text='0',
                command=lambda: btn_click(0)).place(x=110, y=410,
                                                    width=90, height=90)

# ==============FUNCTIONS CLICK======================
addition = MyButton(root, text='+',
                    command=lambda: btn_click('+')).place(x=290, y=140,
                                                          width=90, height=90)
subtraction = MyButton(root, text='-',
                       command=lambda: btn_click('-')).place(x=290, y=230,
                                                             width=90, height=90)
division = MyButton(root, text='/',
                    command=lambda: btn_click('/')).place(x=290, y=320,
                                                          width=90, height=90)
multiplication = MyButton(root, text='*',
                          command=lambda: btn_click('*')).place(x=290, y=410,
                                                                width=90, height=90)

# ==============FUNCTIONS DO======================
summing = MyButton(root, text='=',
                   command=btn_equals_input).place(x=200, y=410,
                                                   width=90, height=90)
clear = MyButton(root, text='C',
                 command=btn_clear_display).place(x=20, y=410,
                                                  width=90, height=90)


if __name__ == "__main__":
    root.mainloop()
