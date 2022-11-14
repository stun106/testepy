def sysCalculator(a:float,b:float,c:str = '') -> float:
    if c == '+':
        return int(a + b)
    elif c == '-':
        return int(a - b)
    elif c == '*':
        return float(a * b)
    else:
        if c == '/':
            return float(a / b)

        

if __name__ == '__main__':
    pass