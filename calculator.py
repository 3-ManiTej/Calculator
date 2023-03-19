'''WHY COLUMNSPAN?
        WE USE COLUMNSPAN BECUSE TO COVER ALL COLUMNS.SINCE IN ENTRY WIDGET
        WE'VE GIVEN 3 MEANS IT COVERS ALL 3 COLUMNS THAT IS WHY THE ENTRY
        WIDGET IS MORE WIDER.'''
from tkinter import *

root=Tk()

entry=Entry(root,width=30,borderwidth=3)
entry.grid(row=0,column=0,columnspan=3)

def button_clear():
    entry.delete(0,END)

def button_click(num):
    curr=entry.get()
    print('after inserting=',curr)
    entry.delete(0,END)
    entry.insert(0,str(curr)+str(num))
    print('res=',entry.get())
    '''print('num=',num)
    #entry.insert(0,'mani')
    current=entry.get()
    print('current=',current)
    entry.delete(0,END)
    print('after deleting=',entry.get())
    entry.insert(0,str(current)+str(num))
    print('after inserting=',entry.get())'''
def button_plus():
    first_num=entry.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_num)
    entry.delete(0,END)
def button_minus():
    first_num = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    entry.delete(0, END)
def button_divide():
    first_num = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    entry.delete(0, END)
def button_multiply():
    first_num = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    entry.delete(0, END)
def button_equal():
    s_num=entry.get()
    entry.delete(0, END)
    if math == 'addition':
        entry.insert(0, f_num+int(s_num))
        #print('addition=', entry.get())
    if math == 'subtraction':
        entry.insert(0, f_num-int(s_num))
        #print('subtraction=', entry.get())
    if math == 'multiplication':
        entry.insert(0, f_num*int(s_num))
        #print('multiplication=',entry.get())
    if math == 'division':
        entry.insert(0, f_num/int(s_num))
        #print('division=',entry.get())

'''WHY LAMBDA?
      WE USE LAMBDA FUNCTION BECAUSE NORMALLY IF WE KEEP PARENTHESIS IN FUNCTION
      THEN IT IS FUNCTION CALL AND IT DOES TAKE ARGUMENTS WHILE FUNCTION CALL,
      NOT SO WE USE LAMBDA FUNCTION'''
button1=Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1))    #DURIING FUNCTION CALL IT PASSES VALUE 1
button2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2))    #DURIING FUNCTION CALL IT PASSES VALUE 2
button3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3))    #DURIING FUNCTION CALL IT PASSES VALUE 3
button4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4))    #SO ON
button5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5))
button6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6))
button7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7))
button8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8))
button9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9))
button0=Button(root,text='0',padx=40,pady=20,command=lambda:button_click(0))
button_plus=Button(root,text='+',padx=36,pady=20,command=button_plus)
button_minus=Button(root,text='-',padx=36,pady=20,command=button_minus)
button_division=Button(root,text='/',padx=30,pady=20,command=button_divide)
button_multiplication=Button(root,text='*',padx=30,pady=20,command=button_multiply)
button_equal=Button(root,text='=',padx=48,pady=20,command=button_equal)
button_clear=Button(root,text='Clear',padx=50,pady=20,command=button_clear)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

button_minus.grid(row=6,column=0)
button_division.grid(row=6,column=1)
button_multiplication.grid(row=6,column=2)

root.mainloop()
