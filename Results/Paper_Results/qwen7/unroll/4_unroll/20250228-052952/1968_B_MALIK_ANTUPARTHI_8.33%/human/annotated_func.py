#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and the sum of all m values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an integer input from the user, b and c are integers input from the user, d is a string input from the user, e is a string input from the user, and k is an integer with the value determined by the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts integers \( n \) and \( m \), and binary strings \( a \) and \( b \). It then finds the first occurrence of any character from string \( a \) in string \( b \) and prints the index of this occurrence. If no such character is found, it prints the length of string \( b \). This process is repeated for each test case specified by the input integer \( t \).

