def read_char(file_path):
    with open(file_path) as file:
        firstFive= file.read(5);
        return firstFive;

file_path = "tk.py"
result= read_char(file_path)
print(result)