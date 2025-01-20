n = int(input())
digits = [int(d) for d in str(n)]
for i in range(len(digits)):
    new_n = int(''.join(map(str, digits[:i] + digits[i+1:])))
    if new_n % 8 == 0 and str(new_n)[0] != '0':
        print("YES")
        print(new_n)
        exit()
print("NO")
