def func_1(x):
    return int(str(x)[::-1])

def func_2(x):
    return x + func_1(x)
x = raw_input()
y = [int(i) for i in x]
y2 = y[:]
y2.reverse()
if len(y) <= 4:
    for i in range(1, 100000):
        if func_2(i) == int(x):
            print(i)
            quit()
    print(0)
    quit()
num = []
num2 = []
for i in range(len(y) // 2):
    if i == 0:
        num.append(min(y[i], y2[i]))
        num2.append(0)
        continue
    if (num[i - 1] + num2[i - 1]) % 10 != y[i - 1]:
        k = y2[i] + 10
        if num[i - 1] + num2[i - 1] > 10:
            k -= 1
        num.append(9)
        num2.append(k - 9)
    else:
        k = y2[i]
        if num[i - 1] + num2[i - 1] > 10:
            k -= 1
        num.append(k)
        num2.append(0)
if len(y) % 2 == 1:
    k = len(y) // 2
    dig = y2[k]
    if (num[k - 1] + num2[k - 1]) % 10 != y[k - 1]:
        dig += 10
    if num[k - 1] + num2[k - 1] > 10:
        dig -= 1
    num.append(dig // 2)
num2.reverse()
cand = ''.join([str(x) for x in num]) + ''.join([str(x) for x in num2])
if func_2(int(cand)) == int(x):
    print(cand)
    quit()
num = []
num2 = []
for i in range(len(y) // 2 - 1):
    if i == 0:
        num.append(9)
        num2.append(y2[0] + 10 - 9)
        continue
    if (num[i - 1] + num2[i - 1]) % 10 != y[i]:
        k = y2[i] + 10
        if num[i - 1] + num2[i - 1] > 10:
            k -= 1
        num.append(9)
        num2.append(k - 9)
    else:
        k = y2[i]
        if num[i - 1] + num2[i - 1] > 10:
            k -= 1
        k = (k + 10) % 10
        num.append(k)
        num2.append(0)
if len(y) % 2 == 0:
    k = len(y) // 2
    dig = y[k]
    if (num[k - 2] + num2[k - 2]) % 10 != y[k - 1]:
        dig += 10
    if num[k - 2] + num2[k - 2] > 10:
        dig -= 1
    num.append(dig // 2)
num2.reverse()
cand = ''.join([str(x) for x in num]) + ''.join([str(x) for x in num2])
if func_2(int(cand)) == int(x):
    print(cand)
    quit()
print(0)