#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: After the loop executes all iterations, `r` will be a concatenated string formed by adding elements from `a` based on the indices found in `b` for each character in `s` for all iterations. The list `b` will have each count of characters in `s` incremented by the total number of times that character appeared across all iterations of `s`. The variable `t` will be equal to the total number of iterations, which is the number of lines of input excluding the first line (since `t` is read from the first line). The variable `n` and the list `a` will remain unchanged from their initial states.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n`, a list of `n` integers `s`, and outputs a string `r`. For each integer in `s`, it finds its index in a predefined string `a` and appends the corresponding character to `r`. It then increments the count of each character in `a` based on the occurrences of their indices in `s`. The function prints the resulting string `r` for each test case and does not return any value.

