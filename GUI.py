import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg

from calculator import *


win = tk.Tk()
win.title("Pn Calculator")

# tạo menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# tao menu va them menu items
file_menu = Menu(menu_bar)
file_menu = Menu(menu_bar, tearoff=0)


menu_bar.add_cascade(label="Calculator", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= win.quit)

# 1.1 Tạo thông báo thông tin, khi chọn vào tab Help/ About
def _msgBox():
    msg.showinfo('Calculator Message Info Box', 'A Python Calculator created using tkinker:\nCoppyright by Pn')
# them help menu
help_menu = Menu(menu_bar, tearoff=0)  
menu_bar.add_cascade(label="Help", menu=help_menu)  
help_menu.add_command(label="About", command= _msgBox)


# tao tab
tabControl = ttk.Notebook(win)
dec = ttk.Frame(tabControl)
tabControl.add(dec, text="Dec")
tabControl.pack(expand=1, fill="both")

bin = ttk.Frame(tabControl)
tabControl.add(bin, text="Bin")
tabControl.pack(expand=2, fill="both")

# tao frame Nhap
Nhap = ttk.LabelFrame(dec, text='Nhap 2 so can tinh: ', style='My.TLabelframe')
Nhap.grid(column=0, row=0, padx=8, pady=4)

so1_lable = ttk.Label(Nhap, text="Nhap so thu nhat:")
so1_lable.grid(column=0, row=0, sticky='W')
num1 = tk.StringVar()
so1_enter = ttk.Entry(Nhap, width= 12, textvariable= num1 )
so1_enter.grid(column=1, row=0, sticky='W')

so2_lable = ttk.Label(Nhap, text="Nhap so thu hai:")
so2_lable.grid(column=0, row=1, sticky='W')
num2 = tk.StringVar()
so2_enter = ttk.Entry(Nhap, width= 12, textvariable= num2 )
so2_enter.grid(column=1, row=1, sticky='W')


# Tao frame ket qua:
Ketqua = ttk.LabelFrame(dec, text='Dap an')
Ketqua.grid(column=0, row=1, padx=8, pady=4)
ketqua_lb = ttk.Label(Ketqua, text="Ket qua: ")
ketqua_lb.grid(column=0, row=0)

kq = tk.StringVar()
kq_en = ttk.Entry(Ketqua, width= 24, textvariable= kq ,state='readonly')
kq_en.grid(column=1, row=0)

# Tao frame tinh
Tinh = ttk.LabelFrame(dec, text='Phep tinh')
Tinh.grid(column=1, row=0, padx=8, pady=4)

# Check input
def check_input():
    try:
        a = float(num1.get())
        b = float(num2.get())    
    
        return True
    except ValueError:
        msg.showerror("Lỗi", "Vui lòng nhập vào các số hợp lệ.")
        return False

# Cac ham phep tinh
def cong_method():
    if check_input():
        from calculator import Calculator 
        calc = Calculator(float(num1.get()), float(num2.get()), "+")
        result = calc.TinhDec()       
        kq.set(str(result))  
        
def tru_method():
    if check_input():
        from calculator import Calculator 
        calc = Calculator(float(num1.get()), float(num2.get()), "-")
        result = calc.TinhDec()     
        kq.set(str(result))         
        
def nhan_method():
        if check_input():
            from calculator import Calculator 
            calc = Calculator(float(num1.get()), float(num2.get()), "x")
            result = calc.TinhDec()     
            kq.set(str(result))        

def chia_method():
        if check_input():
            if float(num2.get()) == 0:
                msg.showinfo("Loi nhap du lieu", "Khong the chia cho 0 ")
                reset_fields()
            else:
                from calculator import Calculator 
                calc = Calculator(float(num1.get()), float(num2.get()), ":")
                result = calc.TinhDec()     
                kq.set(str(result))   
# Ham reset
def reset_fields():
    num1.set("")  
    num2.set("")  
    kq.set("") 
    
# btn Tinh toan  
cong_btn = ttk.Button(Tinh, text="+", command=cong_method)
cong_btn.grid(column=0, row=0)
tru_btn = ttk.Button(Tinh, text="-", command=tru_method)
tru_btn.grid(column=0, row=1)
nhan_btn = ttk.Button(Tinh, text="x", command=nhan_method)
nhan_btn.grid(column=1, row=0)
chia_btn = ttk.Button(Tinh, text=":", command=chia_method)
chia_btn.grid(column=1, row=1)

# btn reset
reset_btn = ttk.Button(Ketqua, text="Reset", command=reset_fields)
reset_btn.grid(column=2, row=0)



#/bin
# Tạo frame Nhap
Nhapbin = ttk.LabelFrame(bin, text='Nhập 2 số cần tính: ', style='My.TLabelframe')
Nhapbin.grid(column=0, row=0, padx=8, pady=4)

so1_bin_label = ttk.Label(Nhapbin, text="Nhập số thứ nhất:")
so1_bin_label.grid(column=0, row=0, sticky='W')
num1_bin = tk.StringVar()
so1_enter_bin = ttk.Entry(Nhapbin, width=12, textvariable=num1_bin)
so1_enter_bin.grid(column=1, row=0, sticky='W')

so2_label_bin = ttk.Label(Nhapbin, text="Nhập số thứ hai:")
so2_label_bin.grid(column=0, row=1, sticky='W')
num2_bin = tk.StringVar()
so2_enter_bin = ttk.Entry(Nhapbin, width=12, textvariable=num2_bin)
so2_enter_bin.grid(column=1, row=1, sticky='W')

# Tạo frame kết quả
Ketquabin = ttk.LabelFrame(bin, text='Đáp án')
Ketquabin.grid(column=0, row=1, padx=8, pady=4)
ketquabin_lb = ttk.Label(Ketquabin, text="Kết quả: ")
ketquabin_lb.grid(column=0, row=0)

kqbin = tk.StringVar()
kqbin_en = ttk.Entry(Ketquabin, width=24, textvariable=kqbin, state='readonly')
kqbin_en.grid(column=1, row=0)
# Kiểm tra đầu vào
def check_bin_input(num):
    try:
        num_str = str(num)
        for char in num_str:
            if char not in '01':
                msg.showerror("Lỗi", "Vui lòng nhập vào các số nhị phân (chỉ 0 và 1).")
                return False
        return True
    except ValueError:
        msg.showerror("Lỗi", "Vui lòng nhập vào các số hợp lệ.")
        return False

# Các hàm phép tính
def and_method():
    
    if check_bin_input(num1_bin.get()) and check_bin_input(num2_bin.get()): 
        from calculator import Calculator 
        calc = Calculator(int(num1_bin.get()), int(num2_bin.get()), "AND")
        result = calc.TinhBin()     
        kqbin.set(str(result))  

def xor_method():
    
    if check_bin_input(num1_bin.get()) and check_bin_input(num2_bin.get()): 
        from calculator import Calculator 
        calc = Calculator(int(num1_bin.get()), int(num2_bin.get()), "XOR")
        result = calc.TinhBin()     
        kqbin.set(str(result))  
        
def or_method():
    
    if check_bin_input(num1_bin.get()) and check_bin_input(num2_bin.get()): 
        from calculator import Calculator 
        calc = Calculator(int(num1_bin.get()), int(num2_bin.get()), "OR")
        result = calc.TinhBin()     
        kqbin.set(str(result))  

def equal_method():
    
    if check_bin_input(num1_bin.get()) and check_bin_input(num2_bin.get()): 
        from calculator import Calculator 
        calc = Calculator(int(num1_bin.get()), int(num2_bin.get()), "=")
        result = calc.TinhBin()     
        kqbin.set(str(result))  
        
# Tạo frame phép tính
Tinhbin = ttk.LabelFrame(bin, text='Phép tính')
Tinhbin.grid(column=1, row=0, padx=8, pady=4)

and_btn = ttk.Button(Tinhbin, text="AND", command=and_method)
and_btn.grid(column=0, row=0)
xor_btn = ttk.Button(Tinhbin, text="XOR", command=xor_method)
xor_btn.grid(column=1, row=0)
or_btn = ttk.Button(Tinhbin, text="OR", command=or_method)
or_btn.grid(column=0, row=1)
equal_btn = ttk.Button(Tinhbin, text="EQUAL", command=equal_method)
equal_btn.grid(column=1, row=1)


# Nút reset
def reset_fields():
    num1_bin.set('')
    num2_bin.set('')
    kqbin.set('')
reset_btn = ttk.Button(Ketquabin, text="Reset", command=reset_fields)
reset_btn.grid(column=2, row=0)

so1_enter_bin.focus()

win.mainloop()