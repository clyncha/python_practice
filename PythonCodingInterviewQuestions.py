# Python Coding Interview Questions

# How can you replace string space with a given character in Python?
def replace_string(text, replacementCharacter):
    result = ''
    for i in text:
        if i == ' ':
            i = replacementCharacter
        result += i
    return result


replace_string("He loWor d", "l")
# "HelloWorld"
replace_string("He lo", "l")
# "Hello"
replace_string("Hello", "l")
# "Hello"
replace_string("He  o", "l")
# "Hello"

# Given a positive integer num, write a function that returns True if num is a perfect square else False.


def valid_square(number):
    # turns square of number into int
    square = int(number**0.5)
    # square the int (number rounds down to 0)
    # if this equal the number passed in the new have a square roto
    return square**2 == number


valid_square(10)
# False
valid_square(36)
# True
valid_square(4.0)
# False

# Given an integer n, return the number of trailing zeroes in n factorial n!


def count_trailing_zeros(n):
    # factorial ex: 5 * 4 * 3 * 2 * 1
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    # Get trailing zeros
    result = 0

    for i in str(fact)[::-1]:
        if i == '0':
            result += 1
        else:
            break

    return result


count_trailing_zeros(10)
# 2
count_trailing_zeros(18)
# 3
