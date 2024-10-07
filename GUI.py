import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox as msg, filedialog
from calculate import Calculator

class BaseCalculatorApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_menu()

    def create_menu(self):
        # Tạo menu cho cửa sổ chính
        menu_bar = Menu(self.parent.winfo_toplevel())  
        self.parent.winfo_toplevel().config(menu=menu_bar)

        # Menu File
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.parent.quit)

        # Menu Preferences
        pref_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Preferences", menu=pref_menu)
        pref_menu.add_command(label="Change Theme", command=self.change_theme)
        pref_menu.add_command(label="Language", command=self.change_language)

        # Menu Help
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Manual", command=self.show_manual)
        help_menu.add_command(label="About", command=self.show_about)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                msg.showinfo("File Content", content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = "Kết quả của phép tính: " + self.result.get()
                file.write(content)
                msg.showinfo("Save", "File đã được lưu thành công!")

    def change_theme(self):
        msg.showinfo("Change Theme", "Coming soon!")

    def change_language(self):
        msg.showinfo("Change Language", "Coming soon!")

    def show_manual(self):
        msg.showinfo("Manual", "Nhập hai số cần tính toán và chọn toán tử.")

    def show_about(self):
        msg.showinfo("About", "Pn Calculator created using tkinter.\nCopyright by Pn")

class DecCalculatorApp(BaseCalculatorApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        self.create_dec_tab(parent)

    def create_dec_tab(self, parent):
        dec_frame = ttk.Frame(parent)  # Sử dụng Frame cho tab Decimal
        parent.add(dec_frame, text="Decimal")  # Thêm frame vào tab_control

        input_frame = ttk.LabelFrame(dec_frame, text="Nhập số", padding=(10, 10))
        input_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Nhập số thập phân thứ nhất:").grid(column=0, row=0, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num1).grid(column=1, row=0, sticky='W')

        ttk.Label(input_frame, text="Nhập số thập phân thứ hai:").grid(column=0, row=1, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num2).grid(column=1, row=1, sticky='W')

        button_frame = ttk.LabelFrame(dec_frame, text="Phép toán", padding=(10, 10))
        button_frame.grid(column=1, row=0, padx=10, pady=10)

        ttk.Button(button_frame, text="+", command=self.add).grid(column=0, row=0)
        ttk.Button(button_frame, text="-", command=self.subtract).grid(column=0, row=1)
        ttk.Button(button_frame, text="x", command=self.multiply).grid(column=1, row=0)
        ttk.Button(button_frame, text=":", command=self.divide).grid(column=1, row=1)

        result_frame = ttk.LabelFrame(dec_frame, text="Kết quả", padding=(10, 10))
        result_frame.grid(column=0, row=1, padx=10, pady=10)

        ttk.Entry(result_frame, width=24, textvariable=self.result, state='readonly').grid(column=0, row=0)

    def perform_calculation(self, method):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            calc = Calculator(num1, num2, method)
            return calc.TinhDec()
        except ValueError:
            msg.showerror("Lỗi", "Vui lòng nhập vào các số hợp lệ.")
            return ""

    def add(self):
        self.result.set(self.perform_calculation("+"))

    def subtract(self):
        self.result.set(self.perform_calculation("-"))

    def multiply(self):
        self.result.set(self.perform_calculation("x"))

    def divide(self):
        if float(self.num2.get()) == 0:
            msg.showerror("Lỗi", "Không thể chia cho 0")
        else:
            self.result.set(self.perform_calculation(":"))

class BinCalculatorApp(BaseCalculatorApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        self.create_bin_tab(parent)

    def create_bin_tab(self, parent):
        bin_frame = ttk.Frame(parent)  # Sử dụng Frame cho tab Binary
        parent.add(bin_frame, text="Binary")  # Thêm frame vào tab_control

        input_frame = ttk.LabelFrame(bin_frame, text="Nhập số nhị phân", padding=(10, 10))
        input_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Nhập số nhị phân thứ nhất:").grid(column=0, row=0, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num1).grid(column=1, row=0, sticky='W')

        ttk.Label(input_frame, text="Nhập số nhị phân thứ hai:").grid(column=0, row=1, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num2).grid(column=1, row=1, sticky='W')

        button_frame = ttk.LabelFrame(bin_frame, text="Phép toán", padding=(10, 10))
        button_frame.grid(column=1, row=0, padx=10, pady=10)

        ttk.Button(button_frame, text="AND", command=self.and_op).grid(column=0, row=0)
        ttk.Button(button_frame, text="OR", command=self.or_op).grid(column=0, row=1)
        ttk.Button(button_frame, text="XOR", command=self.xor_op).grid(column=1, row=0)
        ttk.Button(button_frame, text="=", command=self.equal_op).grid(column=1, row=1)

        result_frame = ttk.LabelFrame(bin_frame, text="Kết quả", padding=(10, 10))
        result_frame.grid(column=0, row=1, padx=10, pady=10)

        ttk.Entry(result_frame, width=24, textvariable=self.result, state='readonly').grid(column=0, row=0)

    def perform_calculation(self, method):
        try:
            calc = Calculator(self.num1.get(), self.num2.get(), method)
            return calc.TinhBin()
        except ValueError as e:
            msg.showerror("Lỗi", str(e))
            return ""

    def and_op(self):
        self.result.set(self.perform_calculation("AND"))

    def or_op(self):
        self.result.set(self.perform_calculation("OR"))

    def xor_op(self):
        self.result.set(self.perform_calculation("XOR"))

    def equal_op(self):
        result = self.perform_calculation("=")
        self.result.set("True" if result else "False")

class HexCalculatorApp(BaseCalculatorApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        self.create_hex_tab(parent)

    def create_hex_tab(self, parent):
        hex_frame = ttk.Frame(parent)  # Sử dụng Frame cho tab Hexadecimal
        parent.add(hex_frame, text="Hexadecimal")  # Thêm frame vào tab_control

        input_frame = ttk.LabelFrame(hex_frame, text="Nhập số Hex", padding=(10, 10))
        input_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Nhập số hex thứ nhất:").grid(column=0, row=0, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num1).grid(column=1, row=0, sticky='W')

        ttk.Label(input_frame, text="Nhập số hex thứ hai:").grid(column=0, row=1, sticky='W')
        ttk.Entry(input_frame, width=12, textvariable=self.num2).grid(column=1, row=1, sticky='W')

        button_frame = ttk.LabelFrame(hex_frame, text="Phép toán", padding=(10, 10))
        button_frame.grid(column=1, row=0, padx=10, pady=10)

        ttk.Button(button_frame, text="+", command=self.add).grid(column=0, row=0)
        ttk.Button(button_frame, text="-", command=self.subtract).grid(column=0, row=1)
        ttk.Button(button_frame, text="x", command=self.multiply).grid(column=1, row=0)
        ttk.Button(button_frame, text=":", command=self.divide).grid(column=1, row=1)

        result_frame = ttk.LabelFrame(hex_frame, text="Kết quả", padding=(10, 10))
        result_frame.grid(column=0, row=1, padx=10, pady=10)

        ttk.Entry(result_frame, width=24, textvariable=self.result, state='readonly').grid(column=0, row=0)

    def perform_calculation(self, method):
        try:
            num1 = self.num1.get()
            num2 = self.num2.get()
            calc = Calculator(num1, num2, method)
            return calc.TinhHex()
        except ValueError:
            msg.showerror("Lỗi", "Vui lòng nhập vào các số hợp lệ.")
            return ""

    def add(self):
        self.result.set(self.perform_calculation("+"))

    def subtract(self):
        self.result.set(self.perform_calculation("-"))

    def multiply(self):
        self.result.set(self.perform_calculation("x"))

    def divide(self):
        if int(self.num2.get(), 16) == 0:
            msg.showerror("Lỗi", "Không thể chia cho 0")
        else:
            self.result.set(self.perform_calculation(":"))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pn Calculator")
    
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    DecCalculatorApp(tab_control)
    BinCalculatorApp(tab_control)
    HexCalculatorApp(tab_control)
    
    root.mainloop()
