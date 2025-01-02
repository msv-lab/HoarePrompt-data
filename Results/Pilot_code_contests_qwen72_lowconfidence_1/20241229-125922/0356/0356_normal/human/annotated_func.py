#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n is an integer where 1 ≤ n ≤ 3⋅10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
def func():
    rint = lambda : int(stdin.readline())
    rints = lambda : [int(x) for x in stdin.readline().split()]
    out = []
    for _ in range(int(input())):
        n, a = rint(), rints()
        
        ans, mem = ['0'] * n, [0] * (n + 1)
        
        ans[0], l, r = '1', 0, n - 1
        
        for i in range(n):
            mem[a[i]] += 1
            if mem[a[i]] == 2:
                ans[0] = '0'
        
        for i in range(1, n):
            if not mem[i]:
                break
            ans[n - i] = '1'
            if a[l] != i and a[r] != i or a[l] == a[r] == i:
                break
            elif a[l] == i:
                l += 1
            else:
                r -= 1
        
        out.append(''.join(ans))
        
    #State of the program after the  for loop has been executed: `t` is an integer where 1 ≤ t ≤ 10^4, `out` is a list of strings, each string is the result of `''.join(ans)` for each test case, `ans` is a list of '0' with length `n` for each test case where `ans[0]` is '0' if any element in `a` appears more than once, otherwise `ans[0]` is '1', and for each `i` in the range [1, n-1], if `mem[i]` is non-zero and the conditions in the loop did not cause a break, `ans[n - i]` will be '1'. Otherwise, `ans[n - i]` will remain '0', `mem` is a list of 0 with length `n + 1` for each test case and `mem[a[i]]` contains the count of `a[i]` for each `i` in the range [0, n-1], `l` is the last index where `a[l]` matched `i` or the number of elements from the start of `a` that match the corresponding `i` values, `r` is the last index where `a[r]` matched `i` or the number of elements from the end of `a` that match the corresponding `i` values, and `i` is the value of the iteration where the loop either completed or broke.
    print('\n'.join(out))
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, the function generates a binary string of length `n` where the first character is '0' if any integer in `a` appears more than once, otherwise it is '1'. For subsequent characters in the string, starting from the end, the function sets the character to '1' if the integer corresponding to its position from the end (1-indexed) appears exactly once in `a` and meets certain conditions involving the leftmost (`l`) and rightmost (`r`) positions of the array `a`. The final result is a list of these binary strings, one for each test case, which is then printed to standard output, each on a new line. The function modifies no external state and does not return any value. Edge cases include when `a` contains duplicate values, when `a` is a permutation of integers from 1 to `n`, and when `a` has repeated values but still meets the conditions for setting '1' in the result string.

