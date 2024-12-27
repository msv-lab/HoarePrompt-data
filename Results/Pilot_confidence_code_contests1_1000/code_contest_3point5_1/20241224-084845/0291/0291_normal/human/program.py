from collections import Counter
input = raw_input
n = int(input())
As = map(int, input().split(" "))

counter = Counter(As)
cur_sum = sum(As)

q = int(input())
for i in range(q):
    b, c = map(int, input().split(" "))
    try:
        num1 = counter[b]
    except:
        num1 = 0
    try:
        counter[c] += num1
    except:
        counter[c] = num1

    diff = (c - b) * num1
    cur_sum += diff
    print(cur_sum)