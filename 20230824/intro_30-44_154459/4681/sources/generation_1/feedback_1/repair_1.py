def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        l_minus_1 = 1
        l_minus_2 = 1
        for i in range(2, n):
            l_i = l_minus_1 + l_minus_2
            l_minus_1 = l_minus_2
            l_minus_2 = l_i
        return l_i

N = int(input())
result = lucas_number(N)
print(result)