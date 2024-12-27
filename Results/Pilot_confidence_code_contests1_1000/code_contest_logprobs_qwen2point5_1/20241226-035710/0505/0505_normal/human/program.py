#k = int(raw_input())


def one_letter_thingy(number):
    if number == 0:
        return 0
    if number == 1:
        return 0
    return (one_letter_thingy(number - (number/2)) + one_letter_thingy((number/2))) + ((number - (number/2)) * (number/2))

letters = [0] * 26

k = int(raw_input())

for letter in range(26):
    if k == 0:
        break
    i = 0
    while True:
        if one_letter_thingy(i) <=k:
            letters[letter] = i
        else:
            break
        i += 1
    k -= one_letter_thingy(letters[letter])

let = "abcdefghijklmnopqrstuvwxyz"

st = ""
for idx, l in enumerate(letters):
    st += let[idx] * letters[idx]
print(st)