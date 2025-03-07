#State of the program right berfore the function call: a and b are binary strings (strings consisting of the characters '0' and '1'), and their lengths n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5.
def func_1():
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: `a` and `b` remain unchanged, `n` and `m` remain unchanged, `k` is the number of characters in `a` that match characters in `b` in the same order, `j` is the index in `b` where the next unmatched character would be found or `m` if all characters in `b` have been checked.
    print(k)
    #This is printed: k (where k is the number of characters in `a` that match characters in `b` in the same order)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input, representing the lengths of two binary strings `a` and `b` respectively, and then reads the binary strings `a` and `b` from the input. It calculates the number of characters in `a` that match characters in `b` in the same order and prints this count `k`. The function does not return any value, but the final state of the program includes the unchanged binary strings `a` and `b`, the unchanged lengths `n` and `m`, and the printed count `k`.

