def solution():
    s = input()
    cnt = [0]*len(s)
    result = curr = 0
    for x in s:
        result += cnt[curr]
        cnt[curr] += 1
        if curr:
            cnt[(curr-1)//2] = 0
        curr += 1 if x == '(' else -1
    return result
 
for _ in range(int(input())):
    print(solution())