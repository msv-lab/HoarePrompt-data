n = input()
base = 1989
m = 9
power_of_10 = [10 ** i for i in range(1, 1 + m)]
cut_off = [0] + power_of_10
for i in range(1, m):
    cut_off[i] += cut_off[i - 1]
cut_off = [base + cut for cut in cut_off]
cut_off_str = [str(cut_off[i])[:-(i + 1)] for i in range(1 + m)]

def func_1(code_str):
    code_len = len(code_str)
    tmp = int(cut_off_str[code_len - 1] + code_str)
    if tmp < cut_off[code_len - 1]:
        tmp += power_of_10[code_len - 1]
    return tmp
for _ in range(n):
    print(func_1(raw_input().split("'")[1]))