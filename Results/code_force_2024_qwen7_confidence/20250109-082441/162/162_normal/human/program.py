from math import ceil
n_tests = int(input())

for i in range(n_tests):
    n = int(input())
    x = [int(i) for i in input().split()]
    counter = x[0]
    for i in range(1, len(x)):
        if x[i] == 1:
            counter += 1
        elif counter > x[i]:
            counter = x[i] * ceil(counter / x[i])
        elif counter < x[i]:
            counter = x[i]
        else:
            counter = x[i] * 2
    print(counter)