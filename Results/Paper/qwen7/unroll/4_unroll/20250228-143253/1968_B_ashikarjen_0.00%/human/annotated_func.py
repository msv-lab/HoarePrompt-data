#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and similarly, the sum of all m values does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `j` is `m`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is the first integer input split by space, `m` is an integer such that 1 ≤ n, m ≤ 2 ⋅ 10^5, `a` is the string input from the user, `b` is the next string input from the user, `k` is 0.
    #
    #Explanation: After the loop executes, `j` will iterate through the entire length of string `b` (i.e., `m`), because for each character in `a` (total `n` characters), `j` is incremented until it either finds a match or reaches the end of `b`. Since the loop breaks when `j` reaches `m` without finding a match for all characters in `a`, `j` will be set to `m`. The other variables (`t`, `n`, `a`, `b`, `k`) remain unchanged as they are not affected by the loop.
    print(k)
    #This is printed: 0
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts two binary strings `a` and `b` of lengths `n` and `m` respectively, and calculates the number of characters in `a` that have a matching character in `b` at the same position. It prints the count of such matching characters for each test case. If no matches are found, it prints `0`. The function does not return any value but prints the result for each test case.

