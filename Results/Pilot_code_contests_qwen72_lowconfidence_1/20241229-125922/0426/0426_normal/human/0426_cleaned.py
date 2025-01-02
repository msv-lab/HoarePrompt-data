n = int(raw_input())
s = raw_input()
temp = s.count('#')
if temp == 0 or temp == n:
    print(0)
else:
    head = 0
    tail = n - temp
    ret = tail + head
    for c in s:
        if c == '#':
            head += 1
        else:
            tail -= 1
        temp2 = head + tail
        if temp2 < ret:
            ret = temp2
    print(ret)