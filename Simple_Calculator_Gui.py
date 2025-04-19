from tkinter import *

root=Tk()
root.title("Calculator")                #Title of the GUI
root.resizable(False,False)             #This will lock the maximise button
root.iconbitmap('calculator_icon.ico')  #GUI Icon

#Functions
def btn_click(num):
    global val

    #Check for two or more operators entered consecutively one after another
    if(val=='' and (num=='*' or num=='/')):
        screen_val.set("Error")
    elif (val!='' and (val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/') and (num=='*' or num=='/')):
        screen_val.set(val)
    elif (val!='' and (val[-1]=='+' or val[-1]=='-') and (num=='+' or num=='-')):
        screen_val.set(val)
    else:
        val+=num
        screen_val.set(val)

def btn_equal():
    global val
    
    if val.isdigit() or val=='':
        screen_val.set("No Operation")
        
    else:
        try:
            screen_val.set(str(eval(val)))
            val=str(eval(val))
        except:
            screen_val.set("Error")
            val=''

def btn_clear():
    global val
    val=''
    screen_val.set(val)

def btn_bs():
    global val
    val=val[0:len(val)-1]
    screen_val.set(val)

#Frames
f1=Frame(root,bg='white')
f2=Frame(root,bg='white')
f3=Frame(root,bg='white')
f4=Frame(root,bg='white')
f5=Frame(root,bg='white')
f6=Frame(root,bg='white')

#Entry Screen
val=''
screen_val=StringVar()
E=Entry(f1,textvariable=screen_val,font="verdana 22",fg='black',bg='white',width=20,borderwidth=10,justify='right')
E.pack()
f1.pack()

#Buttons
button_c=Button(f2,text="C",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=btn_clear)
button_bs=Button(f2,text="Backspace",bd=5,font="verdana 15",height=2,width=12,fg='white',bg='black',command=btn_bs)
button_add=Button(f2,text="+",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('+'))

button_c.pack(side=LEFT,padx=9,pady=10)
button_bs.pack(side=LEFT,padx=9,pady=10)
button_add.pack(side=LEFT,padx=9,pady=10)
f2.pack()

button_7=Button(f3,text="7",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('7'))
button_8=Button(f3,text="8",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('8'))
button_9=Button(f3,text="9",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('9'))
button_sub=Button(f3,text="-",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('-'))

button_7.pack(side=LEFT,padx=9,pady=10)
button_8.pack(side=LEFT,padx=8,pady=10)
button_9.pack(side=LEFT,padx=8,pady=10)
button_sub.pack(side=LEFT,padx=9,pady=10)
f3.pack()

button_4=Button(f4,text="4",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('4'))
button_5=Button(f4,text="5",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('5'))
button_6=Button(f4,text="6",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('6'))
button_mult=Button(f4,text="*",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('*'))

button_4.pack(side=LEFT,padx=9,pady=10)
button_5.pack(side=LEFT,padx=8,pady=10)
button_6.pack(side=LEFT,padx=8,pady=10)
button_mult.pack(side=LEFT,padx=9,pady=10)
f4.pack()

button_1=Button(f5,text="1",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('1'))
button_2=Button(f5,text="2",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('2'))
button_3=Button(f5,text="3",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('3'))
button_div=Button(f5,text="÷",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('/'))

button_1.pack(side=LEFT,padx=9,pady=10)
button_2.pack(side=LEFT,padx=8,pady=10)
button_3.pack(side=LEFT,padx=8,pady=10)
button_div.pack(side=LEFT,padx=9,pady=10)
f5.pack()

button_0=Button(f6,text="0",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('0'))
button_dot=Button(f6,text=".",bd=5,font="verdana 25",height=1,width=3,fg='white',bg='black',command=lambda: btn_click('.'))
button_equal=Button(f6,text="=",bd=5,font="verdana 25",height=1,width=7,fg='white',bg='black',command=btn_equal)

button_0.pack(side=LEFT,padx=9,pady=10)
button_dot.pack(side=LEFT,padx=10,pady=10)
button_equal.pack(side=LEFT,padx=12,pady=10)
f6.pack()

root.mainloop()
