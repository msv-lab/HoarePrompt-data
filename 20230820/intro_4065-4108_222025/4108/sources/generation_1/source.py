s = input()
t = input()

s_count = [0] * 26
t_count = [0] * 26

for i in range(len(s)):
    s_count[ord(s[i]) - ord('a')] += 1
    t_count[ord(t[i]) - ord('a')] += 1

s_count.sort()
t_count.sort()

if s_count == t_count:
    print("Yes")
else:
    print("No")