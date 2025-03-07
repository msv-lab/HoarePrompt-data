def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        for x in str(i):
            sum_value_digits += int(x)
        values[i] = values[i - 1] + sum_value_digits
    for _ in range(t):
        value = int(input())
        print(values[value])
func_1()