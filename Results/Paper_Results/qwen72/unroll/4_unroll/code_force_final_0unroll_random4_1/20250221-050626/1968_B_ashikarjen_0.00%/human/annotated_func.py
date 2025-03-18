#State of the program right berfore the function call: The function should actually be defined with parameters to match the problem description. The correct function definition should be:
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
        
    #State: `n` and `m` remain unchanged, `a` remains unchanged, `b` remains unchanged, `k` is the number of characters in `a` that match characters in `b` in the same order, `j` is the index of the last matched character in `b` plus 1.
    print(k)
    #This is printed: - The `print(k)` statement will print the value of `k`, which is the number of characters in `a` that match characters in `b` in the same order.
    #
    #Since the exact values of `a` and `b` are not provided, we can't compute the exact numerical value of `k`. However, based on the structure of the problem, the print statement will output the value of `k`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input, followed by two strings `a` and `b`. It then calculates the number of characters in `a` that can be matched to characters in `b` in the same order and prints this count. The function does not return any value. After the function concludes, `n`, `m`, `a`, and `b` remain unchanged, and the program state includes the printed count of matched characters.

