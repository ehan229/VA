"""
Solutions to module 2 - A calculator
Student: Yihan Zeng
Mail: yihanzeng229@gmail.com
Reviewed by: Chengzi
Reviewed date: 2024/09/24
"""




"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)
# handle evaluation error
class EvaluationError(Exception):
    def __init__(self,arg):
        self.arg = arg
        super().__init__(self.arg)

def safe_log(x):
    if x<=0:
        raise EvaluationError("log() argument must be greater than 0")
    return math.log(x)
def safe_fac(n):
    if not float.is_integer(n) or n<0 :
        raise EvaluationError("fac() argument must be a non-negative integer")
    return  math.factorial(int(n))  #make sure n is an int



def statement(wtok, variables):  #read the statement
    """ See syntax chart for statement"""
    if wtok.is_at_end():  # check the input, return if it is null
        return
    result = assignment(wtok, variables) #call the assignment function
    if wtok.is_at_end():
        return result  #check the result, return result if not unexpected token
    else:
        raise SyntaxError(f"Unexpected token after assignment")



def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok,variables)  #call the expression to calculate
    while wtok.get_current()=='=': #check'=' for multiple assignment
        wtok.next()

        if not wtok.is_name():  #if not a variable name
            raise SyntaxError(f"Expected a variable name after'='")
        else:
            variables[wtok.get_current()]= result #read the current
            wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+','-']: #add '-'
        op = wtok.get_current() #to get current operator
        wtok.next()
        # handle invalid term
        # ensure there's a valid term after the operator, not another number directly
        if op == '+':
            result += term(wtok,variables)
        else:
            result -= term(wtok,variables)

    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*','/','^']: #add'/''^'
        operator = wtok.get_current()
        wtok.next()
        if operator == '*':
            result *= factor(wtok, variables)
        elif operator == '/':
           divisor = factor(wtok,variables)
           if divisor == 0:
            raise EvaluationError("Division by Zero")
           result /= divisor

    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok,variables)  #handle with negative number
        return result
    elif wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise TokenError("Expected ')'")
        wtok.next()
        return result


    elif wtok.is_name(): #deal with variables and factors
        name = wtok.get_current()


        if name in Functions_1:   # functions with 1 argument
            func = Functions_1[name]
            wtok.next()
            if wtok.get_current()!='(':
                raise SyntaxError("Expected '('after function name")
            wtok.next()
            result = func(assignment(wtok,variables)) #recusively read the function arguments ()
            if wtok.get_current()!=')':
                raise SyntaxError("Expected ')'after function arguments")
            wtok.next()
            # if fac, return int
            if name == 'fac':
                return result
            else:
                return result

        elif name in Functions_N:     # functions with multiple arguments
            func = Functions_N[name]
            wtok.next()

            result = func(*arglist(wtok,variables))

            return result

        elif name in variables:    # for variable return itself
            wtok.next()
            return variables[name]

        else:
            raise EvaluationError("no variable")


    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        return result

    else:
        raise SyntaxError("Expected number or '('")

# ! Fibonacci function with error handling

def fib(n):
    if not float.is_integer(n) or n<0 :
        raise EvaluationError("fib() argument must be integer >= 0")
    else:
        n = int(n)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

'''
def fib(n):
    if not float.is_integer(n) or n < 0:
        raise EvaluationError("fib() argument must be integer >= 0")
    n = int(n)
    mem = {0:0, 1:1}
    def _fib(n, mem):
        if n in mem:
            return mem[n]
        else:
            mem[n] = _fib(n - 1,mem) + _fib(n - 2,mem)
            return mem[n]
    return _fib(n,mem)
'''
#  Min function to return the minimum value from arguments
def min_func(*args):
    if len(args) == 0:
        raise EvaluationError("min() requires at least one argument")
    return min(args)
# Mean function to calculate the mean value
def mean(*args):
    if len(args) == 0:
        raise EvaluationError("mean() require at least one argument")
    return sum(args) / len(args)
# Standard deviation function
def std(*args):
    if len(args) == 0:
        raise EvaluationError("std() requires at least one argument")
    avg = mean(*args)
    variance = sum((x-avg)**2 for x in args) / len(args)
    return math.sqrt(variance)
# crate a dictionary to add functions 'sin' 'cos' 'log' ...
Functions_1={
    'sin': math.sin,
    'cos': math.cos,
    'log': safe_log,
    'exp': math.exp,
    'sqrt': math.sqrt,
    'fac': safe_fac,
    'fib': fib, #add fibonacci function
}

Functions_N={
    'sum': lambda *args:sum(args),
    'max': lambda *args:max(args),
    'min': min_func,
    'std': std,
}
# handle with multiple functions
def arglist(wtok, variables):
    # parse a list of arguments and return them as a list
    args =[]
    if wtok.get_current() != '(':
        raise SyntaxError(f"Expected '(' after function name")
    wtok.next()
    while True:
        args.append(assignment(wtok, variables))    #add expression result into args
        if wtok.get_current()!=',':
            break
        wtok.next()
    if wtok.get_current() != ')':
        raise SyntaxError(f"Expected')' after arguments")
    wtok.next()
    return args

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

## modification here
        if wtok.get_current() == 'vars':
            for key in variables:
                print(f' {key} \t {variables[key]}')
            continue

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 









if __name__ == "__main__":
    main()
