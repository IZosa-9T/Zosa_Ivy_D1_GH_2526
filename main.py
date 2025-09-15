# Working with numbers.
from pyscript import display, document

def add_numbers(e):
    document.getElementById('output').innerHTML = " "

    addend1 = float(document.getElementById('number_1').value)
    addend2 = float(document.getElementById('number_2').value)

    sum = addend1 + addend2

    display(f'The sum of {addend1} + {addend2} is {sum} !', target='output')

def subtract_numbers(e):
    document.getElementById('output').innerHTML = " "
    
    subtrahend1 = float(document.getElementById('number_1').value)
    subtrahend2 = float(document.getElementById('number_2').value)

    difference = subtrahend1 - subtrahend2

    display(f'The difference of {subtrahend1} - {subtrahend2} is {difference} !', target='output')

def multiply_numbers(e):
    document.getElementById('output').innerHTML = " "
    
    multiplicand1 = float(document.getElementById('number_1').value)
    multiplicand2 = float(document.getElementById('number_2').value)

    product = multiplicand1 * multiplicand2

    display(f'The product of {multiplicand1} * {multiplicand2} is {product} !', target='output')

def divide_numbers(e):
    document.getElementById('output').innerHTML = " "
    
    dividend1 = float(document.getElementById('number_1').value)
    dividend2 = float(document.getElementById('number_2').value)

    quotient = dividend1 / dividend2

    display(f'The quotient of {dividend1} / {dividend2} is {quotient} !', target='output')

def calculate_trapezoid_area(e):

    a = float(document.getElementById('b1').value) # first base.
    b = float(document.getElementById('b2').value) # second base.
    c = float(document.getElementById('h').value) # height.

    tarea = ((a+b)/(2))*c

    display(f'The trapezoids area is {tarea} !', target='trapezoid_area_output')








"""# Creating functions in python and getting values from input fields.
def collect_data(e):

    document.getElementById('output').innerHTML = " "

    account_username = document.getElementById('usern').value
    account_password = document.getElementById('usern').value

    display(f'Greetings, {account_username} ! Please confirm that your username: {account_username} and your password: {account_password} are correct.', target='output')

    # a = 2
    # b = 3
    # c = 1

    # answer = (a + b)*b-2+a*b/c

    # display(f'The answer is {answer}.')
"""