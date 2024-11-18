layout1 = raw_input()
layout2 = raw_input()
s = raw_input()
Mods = ''
dic = {}
for i in range(26):
    dic[layout1[i]] = i
for i in range(len(s)):
    if s[i].isdigit():
        Mods += s[i]
    elif s[i].isupper():
        Mods += layout2[dic[s[i].lower()]].upper()
    else:
        Mods += layout2[dic[s[i]]]
print(Mods)