''''
THE CALCULATOR
'''
def input_number():
    num = input("Введите число: ")
    if num == '':
        return None
    try:
        num = float(num)
    except ValueError:
        num = num
    return num

def input_oper():
    oper = input("Операция(*, /, +, -, ^): ")

    if oper == '':
        oper = None

    return oper

def calc_me(x=None,y=None, oper=None):
    if x is None:
        return "ERROR: send me Number1"
    if y is None:
        return "ERROR: send me Number2"
    if (not isinstance(x, (int, float))) or (not isinstance(y, (int, float))):
        return "ERROR: it is not supported yet"

    if oper == '*':
        return x * y
    elif oper == '/':
        if y == 0:
            return "ERROR: Division by zero!"
        else:
            return x / y
    elif oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '^' or oper == '**':
        return x ** y
    else:
        return "ERROR: Unknown operation"

def body():
    number1 = input_number()
    oper = input_oper()
    number2 = input_number()
    result = calc_me(number1,number2, oper)
    print(result)

if __name__ == '__main__':
    body()