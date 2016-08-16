'''
Create a function that generates prime numbers 
between 0 to n
'''

def checkprime(number):
    if number == 1:
        return False
    for n in range(2, number): 
        if number % n == 0:
            return False
    else:
        return True

def display_prime_numbers(n):
    primenumbers = list()
    for number in range(2,n):
        if checkprime(number):
            primenumbers.append(number)

    return primenumbers

print display_prime_numbers(50)