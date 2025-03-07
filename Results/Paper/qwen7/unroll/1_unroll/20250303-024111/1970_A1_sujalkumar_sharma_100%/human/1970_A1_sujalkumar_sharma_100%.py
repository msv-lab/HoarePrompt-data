def balanced_shuffle(s):
    n = len(s)
    prefix_balance = []
    balance = 0
    
    for i in range(n):
        prefix_balance.append((balance, i, s[i]))
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
    
    prefix_balance.sort(key=lambda x: (x[0], -x[1]))
    
    result = ''.join([x[2] for x in prefix_balance])
    
    return result
 
s = input().strip()
print(balanced_shuffle(s))