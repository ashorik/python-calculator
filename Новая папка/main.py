import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)

def button_click(number):
    # Функция для обработки нажатия кнопок с цифрами
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    # Функция для очистки поля ввода
    entry.delete(0, tk.END)

def button_operation(operator):
    # Функция для обработки выбранной операции
    global first_number, operation
    first_number = float(entry.get())
    entry.delete(0, tk.END)
    operation = operator

def button_equal():
    # Функция для выполнения выбранной операции и вывода результата
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    entry.insert(tk.END, str(result))

# Создаем кнопки с цифрами
button_1 = tk.Button(root, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=0)
button_2 = tk.Button(root, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=1)
button_3 = tk.Button(root, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=2)
button_4 = tk.Button(root, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(root, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(root, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(root, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=0)
button_8 = tk.Button(root, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=1)
button_9 = tk.Button(root, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=2)
button_0 = tk.Button(root, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=1)

# Создаем кнопки операций
button_add = tk.Button(root, text="+", command=lambda: button_operation("+"))
button_add.grid(row=1, column=3)
button_subtract = tk.Button(root, text="-", command=lambda: button_operation("-"))
button_subtract.grid(row=2, column=3)
button_multiply = tk.Button(root, text="*", command=lambda: button_operation("*"))
button_multiply.grid(row=3, column=3)
button_divide = tk.Button(root, text="/", command=lambda: button_operation("/"))
button_divide.grid(row=4, column=3)

# Создаем кнопки для очистки и равно
button_clear = tk.Button(root, text="C", command=button_clear)
button_clear.grid(row=4, column=0)
button_equal = tk.Button(root, text="=", command=button_equal)
button_equal.grid(row=4, column=2)

# Запуск главного цикла
root.mainloop()