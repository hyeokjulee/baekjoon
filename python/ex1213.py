import sys

name = sys.stdin.readline().rstrip()
cntOfAlphabet = {}
palindrome = ''
lengthOfName = len(name)

for i in range(lengthOfName):
    if name[i] in cntOfAlphabet:
        cntOfAlphabet[name[i]] += 1
    else:
        cntOfAlphabet[name[i]] = 1

for key, value in sorted(cntOfAlphabet.items(), reverse=True):
    a, b = divmod(value, 2)
    palindrome = key * a + palindrome + key * a
    if b:
        cntOfAlphabet[key] = 1
    else:
        del cntOfAlphabet[key]

if len(cntOfAlphabet) == 0:
    print(palindrome)
elif len(cntOfAlphabet) == 1:
    print(palindrome[: lengthOfName // 2] + list(cntOfAlphabet.keys())[0] + palindrome[lengthOfName // 2 :])
else:
    print('I\'m Sorry Hansoo')