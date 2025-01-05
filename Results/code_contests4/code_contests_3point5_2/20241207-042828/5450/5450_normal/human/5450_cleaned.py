list = [int(i) for i in raw_input().split()]
if list[1] % list[0] == 0:
    print(list[0] + list[1])
else:
    print(list[1] - list[0])