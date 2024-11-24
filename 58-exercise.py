def lengthOfLastWord(s):
    k = s.split()
    return len(k[-1])

s = input('Enter word: ')
print(lengthOfLastWord(s))