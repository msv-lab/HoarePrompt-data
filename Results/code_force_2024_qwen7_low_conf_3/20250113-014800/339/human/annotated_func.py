#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^5.
def func():
    N = int(input())
    ans = []
    a = [int(x) for x in input().split()]
    b = [(i, a[i]) for i in range(len(a))]
    S = sorted(b, key=lambda x: x[1])
    m = max(a)
    bits = [0] + [1] * N + [0]
    wtr = [[] for q in range(N)]
    f = []
    g = 1
    last = 0
    for (i, num) in S:
        for e in range(num - last):
            f.append(g)
        
        last = num
        
        bits[i + 1] = 0
        
        g += bits[i] + bits[i + 2] - 1
        
    #State of the program after the  for loop has been executed: `f` is a list containing `m` elements, each equal to `g` after the loop; `last` is equal to `m`; `bits` is updated such that `bits[i + 1] = 0` for each index `i` corresponding to an executed iteration of the inner loop; `g` is `g + bits[i] + bits[i + 2] - 1` for each executed iteration of the inner loop. If the loop does not execute, `f` remains an empty list, `last` is `0`, `bits` remains as initially defined, and `g` is `1`.
    for d in range(1, m + 1):
        print(sum([f[d * x] for x in range(1 + (m - 1) // d)]), end=' ')
        
    #State of the program after the  for loop has been executed: `f` is a list containing `m` elements, each equal to `g`, `last` is `m`, `bits` remains as initially defined, `g` is `1`, and `m` is at least `1`. The loop does not execute further because `d` starts from `1` and goes up to `m+1`, and for `d=m+1`, there are no valid `x` values in the range `0` to `(m-1)//d` since `(m-1)//(m+1)` is always `0`. Therefore, the sum of selected elements from `f` is `0`.
#Overall this is what the function does:The function processes a list of integers `a` of length `n` (where \(1 \leq n \leq 10^5\)) and each integer in the list satisfies \(1 \leq a_i \leq 10^5\). It first sorts the indices of the list `a` based on the values in `a`. Then, it initializes several auxiliary lists and variables. During the first for loop, it populates the list `f` with a specific value `g` and updates the `bits` list. Finally, it prints the sum of selected elements from the list `f` for each divisor `d` of `m`, where `m` is the maximum value in the original list `a`.

