def div(a, b):
    if a < 10:
        raise ValueError("Age smaller")
    print(a / b)


try:
    div(1, 0)

except ZeroDivisionError:
    print("Zero Div Error occured")
