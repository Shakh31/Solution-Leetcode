def reverse(x):
    negative = x < 0
    reversed_str = str(abs(x))[::-1]

    reversed_int = int(reversed_str)

    if negative:
        reversed_int = -reversed_str
    return reversed_int

x = int(input('N = '))
print(reverse(x))