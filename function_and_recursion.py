'''Functions'''

def greet_na(name):
    '''Docstring'''
    gr_na = "Hello" + name
    return gr_na
A = greet_na("aashi")
print(A)

def op_na(name = "Stranger"):
    '''Docstring'''
    print("Hello" + name)

op_na()

#Recursion

def factorial_nu(n_l):
    '''product'''
    product = 1
    for i in range(n_l):
        product = product*(i + 1)
    return product

def factorial_recursive(n_l):
    '''Recursion'''
    if n_l == 0  or n_l == 1:
        return 1
    return n_l* factorial_recursive(n_l - 1)

print(factorial_recursive(4))
print(factorial_nu(8))
