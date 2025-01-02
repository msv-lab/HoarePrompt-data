#State of the program right berfore the function call: n and k are integers such that 4 ≤ n ≤ 1000 and n - 1 ≤ k ≤ 2n - 2. a, b, c, and d are distinct integers such that 1 ≤ a, b, c, d ≤ n.
def func():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a, b, c, d = map(int, input().split())
    if (n == 4) :
        print('-1')
    else :
        if (k >= n + 1) :
            chain = [a, c]
            for i in range(1, n + 1):
                if i not in [a, b, c, d]:
                    chain.append(i)
                
            #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 1000, `k` is an integer such that `n` - 1 ≤ `k` ≤ 2`n` - 2, `a`, `b`, `c`, and `d` are distinct integers such that 1 ≤ `a`, `b`, `c`, `d` ≤ `n`, `n` is not equal to 4, `k` is greater than or equal to `n` + 1, `chain` is `[a, c]` followed by all integers from 1 to `n` that are not in `[a, b, c, d]`.
            chain.append(b)
            chain.append(d)
            p1 = list(chain)
            p1[-1], p1[-2] = p1[-2], p1[-1]
            print(' '.join(map(str, p1)))
            p2 = list(chain)
            p2[0], p2[1] = p2[1], p2[0]
            print(' '.join(map(str, p2)))
        else :
            print('-1')
        #State of the program after the if-else block has been executed: *`n` and `k` are integers such that 4 ≤ `n` ≤ 1000 and `n` - 1 ≤ `k` ≤ 2`n` - 2, `a`, `b`, `c`, and `d` are the integers read from input and are distinct such that 1 ≤ `a`, `b`, `c`, `d` ≤ `n`. Additionally, `n` is not equal to 4. If `k` ≥ `n` + 1, the elements of `p2` are printed. If `k` < `n` + 1, `-1` is printed to the console.
    #State of the program after the if-else block has been executed: *`n` and `k` are integers such that 4 ≤ `n` ≤ 1000 and `n` - 1 ≤ `k` ≤ 2`n` - 2, `a`, `b`, `c`, and `d` are distinct integers such that 1 ≤ `a`, `b`, `c`, `d` ≤ `n`. If `n` is 4, `-1` has been printed to the console. If `n` is not 4 and `k` ≥ `n` + 1, the elements of `p2` are printed. If `n` is not 4 and `k` < `n` + 1, `-1` is printed to the console.
#Overall this is what the function does:The function reads two lines of input: the first line contains two integers `n` and `k`, and the second line contains four distinct integers `a`, `b`, `c`, and `d`. The function then performs the following checks and actions:

1. If `n` is 4, the function prints `-1`.
2. If `n` is not 4 and `k` is less than `n + 1`, the function also prints `-1`.
3. If `n` is not 4 and `k` is greater than or equal to `n + 1`, the function constructs a list `chain` starting with `a` and `c`, followed by all integers from 1 to `n` that are not in `[a, b, c, d]`, and finally appends `b` and `d` to the list. It then creates two permutations of `chain`:
   - `p1`: The last two elements of `chain` are swapped.
   - `p2`: The first two elements of `chain` are swapped.
   The function prints both `p1` and `p2` as space-separated strings.

After the function executes, the final state of the program is:
- If `n` is 4 or `k` is less than `n + 1`, `-1` is printed to the console.
- If `n` is not 4 and `k` is greater than or equal to `n + 1`, two lines of space-separated integers representing the permutations `p1` and `p2` are printed to the console.

