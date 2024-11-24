def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

x = int(input('N = '))
print(isPalindrome(x))