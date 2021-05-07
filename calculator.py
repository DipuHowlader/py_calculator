import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry('500x400')
root.title('Calculator')


Label_frame = tk.LabelFrame(root)
Label_frame.pack()



# ======================== out put =============
output_text = tk.StringVar()
output = tk.Entry(Label_frame,textvariable = output_text,width = 45,borderwidth = 5,font = ('Calibri',12))
output.grid(row = 0 ,column = 0,columnspan =3,ipady = 15 )



# main fuctionality ===========
opreators = ('+','-','*','/','%')
sign = ''

def func(num):
    global sign
    output_value = output_text.get()

    output.insert(tk.END,num)

    for opreator in opreators:
        try:
            if output_value.split()[-1][-1] == opreator:
                output.delete(0,tk.END)
                output.insert(tk.END,num)
                sign = opreator
        except IndexError:
            return
    
        

# ============ opreator fuctionality ============
frist_num = 0


def opreation(given_opreator):
    global frist_num

    if frist_num == 0:
        frist_num = int(0)
    print(frist_num)
    frist_value = output_text.get()
    output.insert(tk.END,given_opreator)
    frist_num = frist_value

    

    if len(frist_value) >= 1:
        for opreator in opreators:
            get_again = output_text.get()
            print(frist_value[-1][-1])
            if (frist_value[-1][-1]== opreator):
                output.delete(0,tk.END)
                output.insert(0,f'{get_again[0:-2]}{given_opreator}')

            


# =============== sum fuctionality ==============
def sum():
    secound_num = output_text.get()
    print(secound_num)
    output.delete(0,tk.END)
    if sign == '+':
        total = int(frist_num) + int(secound_num)
        # total = 0
    elif sign == '-':
        total = int(frist_num) - int(secound_num)
    elif sign == '*':
        print('frist',frist_num)
        print('second',secound_num)
        total = int(frist_num) * int(secound_num)
        
    elif sign == '/':
        total = int(frist_num) / int(secound_num)
    else:
        total = secound_num

    output.insert(0,total)


def clear():
    output.delete(0,tk.END)
    return
# =============== number ============
number_dict = {
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '4':'four',
    '5':'five',
    '6':'six',
    '1':'one',
    '2':'two',
    '3':'three',
    '0':'zero',
}

s = ttk.Style()
s.configure('opreator.TButton',font = ('Bahnschrift Light',14))

column  = 0
row = 1
for key in number_dict:
    button_name = 'button_'+ (number_dict.get(key))
    button_name = ttk.Button(Label_frame,text = key,command =lambda key = key:func(key),style = 'opreator.TButton')
    button_name.grid(row= row,column= column,sticky = tk.W,ipadx = 0,ipady= 10)
    column += 1
    if column == 3:
        row+=1
        column = 0

        

button_Plus = ttk.Button(Label_frame,text = '+',command =lambda :opreation('+'),style = 'opreator.TButton')
button_Minus = ttk.Button(Label_frame,text = '-',command =lambda :opreation('-'),style = 'opreator.TButton')
button_Multify = ttk.Button(Label_frame,text = '*',command =lambda :opreation('*'),style = 'opreator.TButton')
button_Division = ttk.Button(Label_frame,text = '/',command =lambda :opreation('/'),style = 'opreator.TButton')



button_Plus.grid(row= 4,column= 1,sticky = tk.W,ipadx = 0,ipady= 10)
button_Minus.grid(row= 4,column= 2,sticky = tk.W,ipadx = 0,ipady= 10)
button_Multify.grid(row= 5,column= 0,sticky = tk.W,ipadx = 0,ipady= 10)
button_Division.grid(row= 5,column= 1,sticky = tk.W,ipadx = 0,ipady= 10)




# ================= sum ===============
button_sum = ttk.Button(Label_frame,text = '=',command = sum,style = 'opreator.TButton')
button_sum.grid(row= 5,column = 2,sticky = tk.W,ipadx =0,ipady= 10)


# ================ clear button ==============
button_clear = tk.Button(Label_frame,text = 'Clear',width= 40,command = clear,bg ='crimson', fg ='#fff',border = 1,font = ('Bahnschrift Light', 12))
button_clear.grid(row= 6,column = 0,columnspan= 3,sticky = tk.W,ipady= 15)












root.mainloop()
