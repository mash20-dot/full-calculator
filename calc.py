try:
    while True:
            a = float(input('first number'))
            b = float(input('second number'))
            ab = input('enter an operator(/, *, -, +)')
            if ab == '/' and b == 0:
                print("erro, can not devide by zero")
            elif ab not in ('/', '*', '-', '+'):
                print('error')
            elif ab == '/':
                print(a / b)
            elif ab == '*':
                print(a * b)
            elif ab == '-':
                print(a - b)
            elif ab == '+':
                print(a + b)
            break
except ValueError:
    print("error, enter an integer or float")
    
