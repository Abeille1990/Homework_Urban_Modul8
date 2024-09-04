
def add_everything_up(a, b):

    try:

        sum = a + b
        return sum

    except:

        c = (f'{a},{b}')
        return c
    
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

