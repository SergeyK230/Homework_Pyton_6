#  1) Доделать реализацию функции eval со скобками

from os import remove


def new_eval(text):
    sibols = ['(', ')', '*', '/', '+', '-', '^']
    result = []
    mem = ''
    for i in text:
        if i not in sibols:
            mem += i
        elif i in sibols:
            if mem != '':
                result.append(float(mem))
            result.append(i)
            mem = ''
    result.append(float(mem))
    return(reshenie(result))

def scobki(prim):
    i = 0
    j = -1
    vrem = 0
    while '(' in prim:
        if prim[i] == '(':
            while True:
                if prim[j] == ')':
                    vrem = prim[i+1:j]
                    vrem = reshenie(vrem)
                    prim[j] = vrem
                    del prim[i:j]
                    j = -1
                    break
                else:
                    j -= 1
        else:
            i +=1
    return prim

def reshenie(prim):
    if '(' in prim:
        prim = scobki(prim)

    i = 0
    while '^' in prim:
        if prim[i] ==  '^':
            prim[i+1] = deistvie(prim[i-1], prim[i+1], prim[i])
            del prim[i-1:i+1]
            i = 0
        else:
            i += 1
           
    i = 0
    while ('*' in prim) or ('/' in prim):
        if prim[i] == '*' or prim[i] == '/':
            prim[i+1] = deistvie(prim[i-1], prim[i+1], prim[i])
            del prim[i-1:i+1]
            i = 0
        else:
            i += 1
    
    i = 0
    while ('+' in prim) or ('-' in prim):
        if prim[i] == '+' or prim[i] == '-':
            prim[i+1] = deistvie(prim[i-1], prim[i+1], prim[i])
            del prim[i-1:i+1]
            i = 0
        else:
            i += 1
            
    return prim[0]

def deistvie(arg1,arg2,znak):
    match znak:
        case '^':
            return arg1**arg2
        case '*':
            return arg1*arg2
        case '/':
            return arg1 / arg2
        case '+':
            return arg1 + arg2
        case '-':
            return arg1 - arg2


primer = '1+2*3+4*5'
print(eval(primer), new_eval(primer))
primer = '(1+2)*3+4*5'
print(eval(primer), new_eval(primer))
primer = '((1+2)*3+4)*5'
print(eval(primer), new_eval(primer))
primer = '((1+2)*3+4)*5^2'
print(eval('((1+2)*3+4)*5**2'), new_eval(primer))






    