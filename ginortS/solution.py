""" 
Hackerrank
Take in a string and sort it as follwoing...
lowercase letters/Upper case/odd numbers/even numbers
"""


string_input = input()


def iseven(x): return True if int(x) % 2 == 0 else False


lower, upper, odd, even = [], [], [], []

for c in string_input:
    if str.islower(c):
        lower.append(c)
    elif str.isupper(c):
        upper.append(c)
    elif str.isdecimal(c):
        if iseven(c):
            even.append(c)
        else:
            odd.append(c)
print(''.join(sorted(lower)+sorted(upper) + sorted(odd) + sorted(even)))
