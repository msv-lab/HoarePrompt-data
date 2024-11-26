n = int(input())
strings = input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

new_strings = ''
for s in strings:
    index = letters.index(s)
    added_index = index + n
    new_index = added_index % 26
    new_s = letters[new_index]
    new_strings += new_s

print(new_strings)