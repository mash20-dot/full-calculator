try:
   a = float(input('enter your first number'))
   b = float(input('enter your second number'))
   ab = input('enter an operator(/,*,-,+)').strip()
   
   if ab not in ('/', '*', '-', '+'):
        print("invalid operator input")
   elif ab == '/'and b == 0:
        print('number not divisible by zero')
   else:
    if ab == '/':
        print(a / b)
    elif ab == '*':
        print(a * b)
    elif ab == '-':
        print(a - b)
    elif ab == '+':
        print(a + b)
except ValueError:
   print("error, please enter correct value")









