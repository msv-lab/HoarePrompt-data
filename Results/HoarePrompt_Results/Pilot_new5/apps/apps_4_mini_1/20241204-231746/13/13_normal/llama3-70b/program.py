n = int(input())
s = input()

golden = [i for i, x in enumerate(s) if x == 'G']

max_beauty = 0
curr_beauty = 0
left = 0

for right in range(n):
    if s[right] == 'G':
        curr_beauty += 1
    else:
        max_beauty = max(max_beauty, curr_beauty)
        curr_beauty = 0
        while left < right and s[left] != 'G':
            left += 1
        if left < right:
            curr_beauty += 1

max_beauty = max(max_beauty, curr_beauty)

max_beauty_one_swap = 0
for i in range(n - 1):
    if s[i] == 'G' and s[i + 1] == 'S':
        beauty = 1
        for j in range(i - 1, -1, -1):
            if s[j] == 'G':
                beauty += 1
            else:
                break
        for j in range(i + 2, n):
            if s[j] == 'G':
                beauty += 1
            else:
                break
        max_beauty_one_swap = max(max_beauty_one_swap, beauty)

print(max(max_beauty, max_beauty_one_swap))
