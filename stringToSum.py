from functools import reduce
sign_set = {i for i in '1234567890.'}


def reducer(val_prev, val):
    return val_prev + val


def string_to_sum(line):
    numbers = []
    numerals = ''
    for sign in line:
        if sign in sign_set:
            numerals += sign
        else:
            if numerals.__len__() != 0:
                numbers.append(float(numerals))
                numerals = ''
    return reduce(reducer, numbers)


def core():
    print('sum of string: ', string_to_sum(input('please insert a string containing numbers:\n')))


if __name__ == '__main__':
    core()
