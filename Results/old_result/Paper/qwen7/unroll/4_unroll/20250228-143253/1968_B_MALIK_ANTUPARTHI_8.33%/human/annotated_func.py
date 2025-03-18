#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a and b are binary strings of lengths n and m respectively. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and the sum of all m values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an integer input by the user, each iteration of the outer loop modifies variable `k` based on the conditions given, and the final value of `k` for each iteration is printed. The final state of `k` after all iterations of the loop will be the last value printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers n and m, followed by two binary strings a and b. It then finds the first occurrence of string a within string b (considering overlaps) and prints the starting index of this occurrence. If no such occurrence exists, it prints the length of string a. After processing all test cases, the function concludes with the final output consisting of indices for each test case.

