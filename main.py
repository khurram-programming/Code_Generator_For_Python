from tkinter import *
root = Tk()
root.geometry("450x200")
root.title("Code Generator")
root.configure(background="#d6d6d6")
root.wm_iconbitmap("icon.ico")


# Functions

# Function for Hello World
def helloworld():
    file = open("helloworld.py", "w")
    file.write('print("Hello World")')
    file.close()
    file = open("helloworld.py", "r")
    z = file.read()

    root2 = Tk()
    root2.geometry("495x525")
    root2.title("Hello World")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    Label(root2, text="You can copy this code.", font="Helvetica 16 bold",
          bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
    t = Text(root2, width=50, font=16)
    t.grid(row=1, column=0, padx=20, pady=10)
    t.insert(1.0, z)
    root2.mainloop()

    file.close()



# Function for print name
def print_name():
    file = open("print_name.py", "w")
    a = 'a = input("Enter your name: ")'
    b = 'print("Your name is:",a)'
    n = '\n'
    data = a+n+b
    file.write(data)
    file.close()
    file = open("print_name.py", "r")
    z = file.read()

    root2 = Tk()
    root2.geometry("495x525")
    root2.title("Print Name")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    Label(root2, text="You can copy this code.", font="Helvetica 16 bold",
          bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
    t = Text(root2, width=50, font=16)
    t.grid(row=1, column=0, padx=20, pady=10)
    t.insert(1.0, z)
    root2.mainloop()

    file.close()


# Function for arithmetic operators
def arithmetic_operators():
    window = Tk()
    window.geometry("250x160")
    window.title("Select Operator")
    window.configure(background="#d6d6d6")
    window.wm_iconbitmap("icon.ico")
    Label(window, text="Select Operator:", font="Helvetica 16 bold",
          bg="#d6d6d6").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
    def add():
        file = open("arithmetic_operators.py", "w")
        a = 'a = float(input("Enter any number: "))'
        b = 'b = float(input("Enter any number: "))'
        c = 'c = a+b'
        d = 'print("The arithmetic operation is performed and the result is:",c)'
        n = '\n'
        data = a+n+b+n+c+n+d+n
        file.write(data)
        file.close()
        file = open("arithmetic_operators.py", "r")
        z = file.read()
        
        root2 = Tk()
        root2.geometry("495x525")
        root2.title("Arithematic Operators")
        root2.configure(background="#d6d6d6")
        root2.wm_iconbitmap("icon.ico")
        Label(root2, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
        t = Text(root2, width=50, font=16)
        t.grid(row=1, column=0, padx=20, pady=10)
        t.insert(1.0, z)
        root2.mainloop()
        
        file.close()
        
        
    def sub():
        file = open("arithmetic_operators.py", "w")
        a = 'a = float(input("Enter any number: "))'
        b = 'b = float(input("Enter any number: "))'
        c = 'c = a-b'
        d = 'print("The arithmetic operation is performed and the result is:",c)'
        n = '\n'
        data = a+n+b+n+c+n+d+n
        file.write(data)
        file.close()
        file = open("arithmetic_operators.py", "r")
        z = file.read()
        
        root2 = Tk()
        root2.geometry("495x525")
        root2.title("Arithematic Operators")
        root2.configure(background="#d6d6d6")
        root2.wm_iconbitmap("icon.ico")
        Label(root2, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
        t = Text(root2, width=50, font=16)
        t.grid(row=1, column=0, padx=20, pady=10)
        t.insert(1.0, z)
        root2.mainloop()
        
        file.close()
        
        
    def multiply():
        file = open("arithmetic_operators.py", "w")
        a = 'a = float(input("Enter any number: "))'
        b = 'b = float(input("Enter any number: "))'
        c = 'c = a*b'
        d = 'print("The arithmetic operation is performed and the result is:",c)'
        n = '\n'
        data = a+n+b+n+c+n+d+n
        file.write(data)
        file.close()
        file = open("arithmetic_operators.py", "r")
        z = file.read()
        
        root2 = Tk()
        root2.geometry("495x525")
        root2.title("Arithematic Operators")
        root2.configure(background="#d6d6d6")
        root2.wm_iconbitmap("icon.ico")
        Label(root2, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
        t = Text(root2, width=50, font=16)
        t.grid(row=1, column=0, padx=20, pady=10)
        t.insert(1.0, z)
        root2.mainloop()
        
        file.close()
        
        
    def divide():
        file = open("arithmetic_operators.py", "w")
        a = 'a = float(input("Enter any number: "))'
        b = 'b = float(input("Enter any number: "))'
        c = 'c = a/b'
        d = 'print("The arithmetic operation is performed and the result is:",c)'
        n = '\n'
        data = a+n+b+n+c+n+d+n
        file.write(data)
        file.close()
        file = open("arithmetic_operators.py", "r")
        z = file.read()
        
        root2 = Tk()
        root2.geometry("495x525")
        root2.title("Arithematic Operators")
        root2.configure(background="#d6d6d6")
        root2.wm_iconbitmap("icon.ico")
        Label(root2, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
        t = Text(root2, width=50, font=16)
        t.grid(row=1, column=0, padx=20, pady=10)
        t.insert(1.0, z)
        root2.mainloop()
        
        file.close()
        
    addButton = Button(window, text="  +  ", font="Helvetica 12 bold",
            command=add, bg="#36a4ff", fg="white", relief=SUNKEN)
    addButton.grid(row=1, column=0, padx=10, pady=10)
    
    subButton = Button(window, text="  -  ", font="Helvetica 12 bold",
            command=sub, bg="#36a4ff", fg="white", relief=SUNKEN)
    subButton.grid(row=1, column=1, padx=10, pady=10)
    
    multiplyButton = Button(window, text="  *  ", font="Helvetica 12 bold",
            command=multiply, bg="#36a4ff", fg="white", relief=SUNKEN)
    multiplyButton.grid(row=2, column=0, padx=10, pady=10)
    
    divideButton = Button(window, text="  /  ", font="Helvetica 12 bold",
            command=divide, bg="#36a4ff", fg="white", relief=SUNKEN)
    divideButton.grid(row=2, column=1, padx=10, pady=10)

    
    window.mainloop()



# Function for if elif else
def if_elif_else():
    file = open("if_elif_else.py", "w")
    a = 'a = input("Enter if or elif or else: ")'
    b = 'if a == "if":'
    c = '\tprint("This is if statement")'
    d = 'elif a == "elif":'
    e = '\tprint("This is elif statement")'
    f = 'else:'
    g = '\tprint("This is else statement")'
    new = '\n'
    data = a+new+b+new+c+new+d+new+e+new+f+new+g
    file.write(data)
    file.close()
    file = open("if_elif_else.py", "r")
    z = file.read()
    
    root2 = Tk()
    root2.geometry("495x525")
    root2.title("if elif else")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    Label(root2, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
    t = Text(root2, width=50, font=16)
    t.grid(row=1, column=0, padx=20, pady=10)
    t.insert(1.0, z)
    root2.mainloop()
    
    file.close()


# Function for for loop Button
def forloop():
    
    root2 = Tk()
    root2.geometry("260x120")
    root2.title("for Loop")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    
    
    startLabel = Label(root2, text="Start Value", font="Helvetica 12 bold", bg="#d6d6d6")
    startLabel.grid(row=0, column=0)
    
    startvalue = IntVar()
    startentry = Entry(root2, textvariable=startvalue)
    startentry.grid(row=0, column=1)
    
    
    endLabel = Label(root2, text="End Value", font="Helvetica 12 bold", bg="#d6d6d6")
    endLabel.grid(row=1, column=0)
    
    endvalue = IntVar()
    endentry= Entry(root2, textvariable=endvalue)
    endentry.grid(row=1, column=1)
    
    
    stepLabel = Label(root2, text="Step Size Value", font="Helvetica 12 bold", bg="#d6d6d6")
    stepLabel.grid(row=2, column=0)
    
    stepvalue = IntVar()
    stepentry= Entry(root2, textvariable=stepvalue)
    stepentry.grid(row=2, column=1)
    
    
    def submit():
        global data
        global start
        global end
        global step
        global file
        def takevalue(s, e, stp):
            global data
            global start
            global end
            global step
            global file
            file = open("forloop.py", "w")
            
            start = s
            end = e
            step = stp
            
            a = f'for i in range({start}, {end}, {step}):'
            b = '\tprint(i)'
            new = '\n'
            
            data = a+new+b
            file.write(data)
            file.close()
            file = open("forloop.py", "r")
            z = file.read()
    
            root3 = Tk()
            root3.geometry("495x525")
            root3.title("for Loop")
            root3.configure(background="#d6d6d6")
            root3.wm_iconbitmap("icon.ico")
            Label(root3, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
            t = Text(root3, width=50, font=16)
            t.grid(row=1, column=0, padx=20, pady=10)
            t.insert(1.0, z)
            root3.mainloop()
    
            file.close()
            
        takevalue(startentry.get(), endentry.get(), stepentry.get())
        
        
    buttonforloop = Button(root2, text="Submit To This Application", font="Helvetica 12 bold", command=submit, bg="#36a4ff", fg="white", relief=SUNKEN)
    buttonforloop.grid(row=3, column=0,columnspan=2)
    root2.mainloop()
    



# Function for "for loop to print name" Button
def forname():
    root2 = Tk()
    root2.geometry("223x85")
    root2.title("for Loop")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    
    
    startLabel = Label(root2, text="Start Value", font="Helvetica 12 bold", bg="#d6d6d6")
    startLabel.grid(row=0, column=0)
    
    startvalue = IntVar()
    startentry = Entry(root2, textvariable=startvalue)
    startentry.grid(row=0, column=1)
    
    
    endLabel = Label(root2, text="End Value", font="Helvetica 12 bold", bg="#d6d6d6")
    endLabel.grid(row=1, column=0)
    
    endvalue = IntVar()
    endentry= Entry(root2, textvariable=endvalue)
    endentry.grid(row=1, column=1)
    
    
    def submit():
        global data
        global start
        global end
        global file
        def takevalue(s, e):
            global data
            global start
            global end
            global name
            global file
            file = open("forname.py", "w")
            name = 'name = input("Enter your name ")'
            start = s
            end = e
            a = f'for i in range({start}, {end}):'
            b = f'\tprint(name)'
            new = '\n'
            data = name+new+a+new+b
            file.write(data)
            file.close()
            file = open("forname.py", "r")
            z = file.read()
            root3 = Tk()
            root3.geometry("495x525")
            root3.title("for loop to print name n times")
            root3.configure(background="#d6d6d6")
            root3.wm_iconbitmap("icon.ico")
            Label(root3, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
            t = Text(root3, width=50, font=16)
            t.grid(row=1, column=0, padx=20, pady=10)
            t.insert(1.0, z)
            root3.mainloop()
            file.close()
            
        takevalue(startentry.get(), endentry.get())
    
    
    buttonforloop = Button(root2, text="Submit To This Application", font="Helvetica 12 bold", command=submit, bg="#36a4ff", fg="white", relief=SUNKEN)
    buttonforloop.grid(row=2, column=0,columnspan=2)
    root2.mainloop()








# While Loop Function
def whileloop():
    root2 = Tk()
    root2.geometry("223x85")
    root2.title("while Loop")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    
    startLabel = Label(root2, text="Start Value", font="Helvetica 12 bold", bg="#d6d6d6")
    startLabel.grid(row=0, column=0)
    
    startvalue = IntVar()
    startentry = Entry(root2, textvariable=startvalue)
    startentry.grid(row=0, column=1)
    
    
    endLabel = Label(root2, text="End Value", font="Helvetica 12 bold", bg="#d6d6d6")
    endLabel.grid(row=1, column=0)
    
    endvalue = IntVar()
    endentry= Entry(root2, textvariable=endvalue)
    endentry.grid(row=1, column=1)
    
    def submit():
        global data
        global start
        global end
        global file
        def takevalue(s, e):
            global data
            global start
            global end
            global file
            file = open("whileloop.py", "w")
            start = s
            end = e
            if int(start) > int(end):
                start, end = end, start
            a = f'a = {start}'
            b = f'b = {end}'
            c = f'while a<=b:'
            d = '\tprint(a)'
            e = '\ta=a+1'
            new = '\n'
            data = a+new+b+new+c+new+d+new+e
            file.write(data)
            file.close()
            file = open("whileloop.py", "r")
            z = file.read()
            root3 = Tk()
            root3.geometry("495x525")
            root3.title("while loop")
            root3.configure(background="#d6d6d6")
            root3.wm_iconbitmap("icon.ico")
            Label(root3, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
            t = Text(root3, width=50, font=16)
            t.grid(row=1, column=0, padx=20, pady=10)
            t.insert(1.0, z)
            root3.mainloop()
            file.close()
            
        takevalue(startentry.get(), endentry.get())
        
        
    buttonforloop = Button(root2, text="Submit To This Application", font="Helvetica 12 bold", command=submit, bg="#36a4ff", fg="white", relief=SUNKEN)
    buttonforloop.grid(row=2, column=0,columnspan=2)
    root2.mainloop()









# This is the function for the program of for loop print even numbers
def foreven():
    root2 = Tk()
    root2.geometry("320x100")
    root2.title("Even Numbers for Loop")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    
    
    startLabel = Label(root2, text="Start Value", font="Helvetica 12 bold", bg="#d6d6d6")
    startLabel.grid(row=0, column=0)
    
    startvalue = IntVar()
    startentry = Entry(root2, textvariable=startvalue)
    startentry.grid(row=0, column=1)
    
    
    endLabel = Label(root2, text="End Value", font="Helvetica 12 bold", bg="#d6d6d6")
    endLabel.grid(row=1, column=0)
    
    endvalue = IntVar()
    endentry= Entry(root2, textvariable=endvalue)
    endentry.grid(row=1, column=1)
    
    
    def submit():
        def takevalue(s, e):
            file = open("foreven.py", "w")
            start = s
            end = e
            a = f'for i in range({start}, {end}):'
            b = '\tif(i%2==0):'
            c = '\t\tprint(i)'
            new = '\n'
            data = a+new+b+new+c
            file.write(data)
            file.close()
            file = open("foreven.py", "r")
            z = file.read()
            root3 = Tk()
            root3.geometry("495x525")
            root3.title("for loop to print even numbers")
            root3.configure(background="#d6d6d6")
            root3.wm_iconbitmap("icon.ico")
            Label(root3, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
            t = Text(root3, width=50, font=16)
            t.grid(row=1, column=0, padx=20, pady=10)
            t.insert(1.0, z)
            root3.mainloop()
            file.close()
            
        takevalue(startentry.get(), endentry.get())
    
    
    buttonforloop = Button(root2, text="Submit To This Application", font="Helvetica 12 bold", command=submit, bg="#36a4ff", fg="white", relief=SUNKEN)
    buttonforloop.grid(row=2, column=0,columnspan=2)
    root2.mainloop()










# This function is used to print a program of while loop printing name
def whileloopname():
    root2 = Tk()
    root2.geometry("223x85")
    root2.title("while loop to print names")
    root2.configure(background="#d6d6d6")
    root2.wm_iconbitmap("icon.ico")
    
    startLabel = Label(root2, text="Start Value", font="Helvetica 12 bold", bg="#d6d6d6")
    startLabel.grid(row=0, column=0)
    
    startvalue = IntVar()
    startentry = Entry(root2, textvariable=startvalue)
    startentry.grid(row=0, column=1)
    
    
    endLabel = Label(root2, text="End Value", font="Helvetica 12 bold", bg="#d6d6d6")
    endLabel.grid(row=1, column=0)
    
    endvalue = IntVar()
    endentry= Entry(root2, textvariable=endvalue)
    endentry.grid(row=1, column=1)
    
    def submit():
        def takevalue(s, e):
            file = open("whileloopname.py", "w")
            start = s
            end = e
            if int(start) > int(end):
                start, end = end, start
            a = 'name = input("Enter your name: ")'
            b = f'a = {start}'
            c = f'b = {end}'
            d = f'while a<=b:'
            e = '\tprint(name)'
            f = '\ta=a+1'
            new = '\n'
            data = a+new+b+new+c+new+d+new+e+new+f
            file.write(data)
            file.close()
            file = open("whileloopname.py", "r")
            z = file.read()
            root3 = Tk()
            root3.geometry("495x525")
            root3.title("while loop to print names")
            root3.configure(background="#d6d6d6")
            root3.wm_iconbitmap("icon.ico")
            Label(root3, text="You can copy this code.", font="Helvetica 16 bold", bg="#d6d6d6").grid(row=0, column=0, padx=10, pady=10)
            t = Text(root3, width=50, font=16)
            t.grid(row=1, column=0, padx=20, pady=10)
            t.insert(1.0, z)
            root3.mainloop()
            file.close()
            
        takevalue(startentry.get(), endentry.get())
        
        
    buttonforloop = Button(root2, text="Submit To This Application", font="Helvetica 12 bold", command=submit, bg="#36a4ff", fg="white", relief=SUNKEN)
    buttonforloop.grid(row=2, column=0,columnspan=2)
    root2.mainloop()













# Label of CODE GENERATOR
Label(root, text="CODE GENERATOR", font="Helvetica 16 bold",
      bg="#d6d6d6").grid(row=0, column=0, columnspan=3)


# Buttons

# Button for Hello World
b1 = Button(text="Hello World", font="Helvetica 12 bold",
            command=helloworld, bg="#36a4ff", fg="white", relief=SUNKEN)
b1.grid(row=1, column=0, padx=10, pady=10)


# Button for Print Name
b2 = Button(text="Print Name", font="Helvetica 12 bold",
            command=print_name, bg="#36a4ff", fg="white", relief=SUNKEN)
b2.grid(row=1, column=1, padx=10, pady=10)

# Button for Arithmetic Operators
b3 = Button(text="Arithematic Operators", font="Helvetica 12 bold",
            command=arithmetic_operators, bg="#36a4ff", fg="white", relief=SUNKEN)
b3.grid(row=1, column=2, padx=10, pady=10)


# Button for if elif else
b4 = Button(text="if elif else", font="Helvetica 12 bold",
            command=if_elif_else, bg="#36a4ff", fg="white", relief=SUNKEN)
b4.grid(row=2, column=0, padx=10, pady=10)

# Button for forloop
b5 = Button(text="for Loop", font="Helvetica 12 bold",
            command=forloop, bg="#36a4ff", fg="white", relief=SUNKEN)
b5.grid(row=2, column=1, padx=10, pady=10)

# Button for forname
b5 = Button(text="for loop to print name", font="Helvetica 12 bold",
            command=forname, bg="#36a4ff", fg="white", relief=SUNKEN)
b5.grid(row=2, column=2, padx=10, pady=10)

# While Loop Button
b5 = Button(text="while loop", font="Helvetica 12 bold",
            command=whileloop, bg="#36a4ff", fg="white", relief=SUNKEN)
b5.grid(row=3, column=0, padx=10, pady=10)

# For Even Numbers Loop Button
b6 = Button(text="for even", font="Helvetica 12 bold",
            command=foreven, bg="#36a4ff", fg="white", relief=SUNKEN)
b6.grid(row=3, column=1, padx=10, pady=10)


# Button whileloopname
b7 = Button(text="while loop name", font="Helvetica 12 bold",
            command=whileloopname, bg="#36a4ff", fg="white", relief=SUNKEN)
b7.grid(row=3, column=2, padx=10, pady=10)


root.mainloop()
