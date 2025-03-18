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
        
    #State: Output State: `j` is equal to `m`, `m` is greater than or equal to 3, `b[j-1]` (which is `b[m-1]`) does not equal any character in the string `a` for all iterations, `n` is greater than 0, `a` is a string obtained from the input, `b` is a user input string, and `k` is equal to the number of times the inner `while` loop did not find a match for `a[i]` before `j` reached `m`.
    #
    #In simpler terms, after the loop has executed all its iterations, `j` will always be equal to `m`, meaning it has gone through the entire length of the string `b`. The variable `k` will count how many times the condition `b[j] != a[i]` was true across all iterations of the outer loop, indicating the number of mismatches found between the characters of `a` and `b` up to the length of `m`. The variables `n`, `a`, and `b` will retain their initial states as they were not modified within the loop.
    print(k)
    #This is printed: k (where k is the number of mismatches between the characters of `a` and `b` up to the length of `m`)
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it takes two binary strings `a` and `b` of lengths `n` and `m` respectively, and counts the number of positions up to `m` where the characters in `a` do not match the corresponding characters in `b`. It then prints the total count of such mismatches. The function does not modify the input strings `a` and `b` and retains the value of `n` and `m` as they were initially provided.

