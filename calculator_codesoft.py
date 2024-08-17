import tkinter as tk
from tkinter import messagebox

class BoxCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Box-Type Calculator")
        self.root.geometry("300x400")  

        
        self.current_value = ""
        self.create_widgets()

    def create_widgets(self):
        
        display_bg_color = "#d0d0d0"
        display_fg_color = "#000000"
        button_bg_color = "#040a21"
        button_fg_color = "#ebeef7"
        button_active_bg_color = "#bbbcbf"
        clear_button_bg_color = "#040a21"
        clear_button_fg_color = "#ebeef7"
        font_style = ('Arial', 16)

        
        self.display = tk.Entry(self.root, font=('Arial', 24, 'bold'), bd=8, relief='ridge', 
                                bg=display_bg_color, fg=display_fg_color, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                action = self.calculate
            else:
                action = lambda x=text: self.append_to_display(x)
            
            button = tk.Button(self.root, text=text, font=font_style, width=4, height=2, 
                               bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg_color, 
                               command=action)
            button.grid(row=row, column=col, padx=5, pady=5)

        
        self.clear_button = tk.Button(self.root, text='C', font=font_style, width=4, height=2, 
                                      bg=clear_button_bg_color, fg=clear_button_fg_color, 
                                      activebackground="#bbbcbf", command=self.clear_display)
        self.clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def append_to_display(self, value):
        self.current_value += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_value)

    def clear_display(self):
        self.current_value = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.current_value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.current_value = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = BoxCalculatorApp(root)
    root.mainloop()
