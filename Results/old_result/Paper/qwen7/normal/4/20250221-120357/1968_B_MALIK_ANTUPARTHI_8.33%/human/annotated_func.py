#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and similarly, the sum of all m values does not exceed 2 ⋅ 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: All iterations of the loop have been executed. The value of `i` is now equal to `a-1`, `b` remains unchanged, `j` is set to `b - 1`, and `k` is updated based on the conditions within the loop for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, two integers n and m, and two binary strings a and b. For each test case, it searches for the first occurrence of each character in string a within string b, updating a position index k accordingly. After processing all test cases, it prints the final value of k for each case.

