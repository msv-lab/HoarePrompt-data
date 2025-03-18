#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 < n ≤ 2·10^5, `l` is a list of integers read from the input, `y` is the index where the first element in `l` that is greater than its previous element is found, or `y` is `n-1` if no such element exists, `a` is the last element in `l` that is less than or equal to all elements from `l[y+1]` to `l[n-1]`, `b` is the last element in `l` that is greater than or equal to all elements from `l[y+1]` to `l[n-1]`, and `c` is the total count of elements in `l` from `l[y+1]` to `l[n-1]` that are greater than both `a` and `b` when they were initially set, summed over all iterations of the outer loop.
#Overall this is what the function does:The function reads multiple sets of inputs, where each set consists of an integer `n` and a list `l` of `n` integers. For each set, it identifies the first element in `l` that is greater than its predecessor, then iterates through the remaining elements to count how many are greater than two reference values (`a` and `b`). The function prints the count for each set. After processing all sets, the function completes without returning any value.

