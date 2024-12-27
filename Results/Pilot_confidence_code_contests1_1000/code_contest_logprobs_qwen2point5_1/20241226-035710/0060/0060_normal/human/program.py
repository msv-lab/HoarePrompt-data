mystr = raw_input()
n = input()

res = []


def cap(c):
    if ord(c) >= 97:
        return chr(ord(c) + ord('A') - ord('a'))
    else :return c

def decap(c):
    if ord(c) < 97:
        return chr(ord(c) + ord('a') - ord('A'))
    else: return c

mystr = map(decap, mystr)

for i in mystr:
    if ord(i) < n + 97:
        res += [cap(i)]
    else: 
        res += [decap(i)]

print (''.join(res))
