#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 13845, and a_i is an integer for each participant i (1 ≤ i ≤ n) such that -336 ≤ a_i ≤ 1164, with the sum of all a_i equal to 0.
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13845; `i` is `n-1`; `a` is a list containing `n` input integers.
    b = []
    count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(a[i] / 2)
        
        if a[i] % 2 != 0:
            count = count + 1
            if count % 2 == 1:
                a[i] = a[i] / 2
                b.append(a[i])
            if count % 2 == 0:
                a[i] = a[i] / 2 + 1
                b.append(a[i])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13845; `i` is `n-1`; `b` contains the modified values of all elements from `a` based on their parity, `count` is the number of odd integers in the original list `a`, and `a` is a list containing the modified values of all elements.
    print(b)
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 13845) as input, followed by `n` integers `a_i` (where -336 ≤ a_i ≤ 1164) that sum to 0. It processes the integers such that even integers are halved and odd integers are halved with adjustments based on their count (adding 1 for every second odd integer). The modified integers are collected in a list `b`, which is then printed. The function does not return any values but outputs the list `b` directly.

