def function1(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        return value * function1(value, number-1)
def recursive_function2(mystring,a, b):
    if(a >= b ):
        return True
    else:
        if(mystring[a] != mystring[b]):
            return False
        else:
            return recursive_function2(mystring,a+1,b-1)
 
def function2(mystring):
    return recursive_function2(mystring, 0,len(mystring)-1)

def function3(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        half = number // 2
        result = function3(value, half)
        if (number % 2 == 0):
            return result * result
        else:
            return value * result * result
