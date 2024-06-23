from tkinter import Tk, Entry, Button, StringVar, Label

class Calculator:
    def __init__(self, root):
        root.title("Simple Calculator")   
        root.geometry('357x420+0+0')
        root.config(bg="gray")
        root.resizable(False, False)

        self.equation = StringVar()
        self.entervalue = ''
        Entry(width=20, bg="#ccddff", font=('Times New Roman', 28), textvariable=self.equation).place(x=0, y=0)
        
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=125)
        Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=180,y=275)
        Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11,height=4,text='=',relief='flat',bg='Light Blue',command=self.solve).place(x=270,y=350)
        Button(width=11,height=4,text='C',relief='flat',command=self.clear).place(x=0,y=350)


    def show(self, value):
        self.entervalue += str(value)
        self.equation.set(self.entervalue)
    
    def clear(self):
        self.entervalue = ''
        self.equation.set(self.entervalue)

    def solve(self):
        try:
            result = eval(self.entervalue)
            self.equation.set(result)
        except ZeroDivisionError:
            self.equation.set("Error: Division by zero")

            

root = Tk()
calculator = Calculator(root)
root.mainloop()

