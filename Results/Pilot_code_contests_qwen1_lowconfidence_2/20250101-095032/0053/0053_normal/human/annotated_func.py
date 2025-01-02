#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of two lines of input: the first line contains two positive integers n and m such that 1 ≤ n, m ≤ 1000, representing the lengths of the two arrays. The second and third lines of each test case contain n and m integers respectively, where each integer is in the range 1 ≤ a_i, b_i ≤ 1000. The sum of all n across all test cases and the sum of all m across all test cases do not exceed 1000 (∑_{i=1}^t n_i, ∑_{i=1}^t m_i ≤ 1000).
def func():
    input = lambda : stdin.readline().strip()
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        
        lst1 = [int(i) for i in input().split()]
        
        lst2 = [int(i) for i in input().split()]
        
        nk = 0
        
        lst1 = set(lst1)
        
        lst2 = set(lst2)
        
        for i in lst1:
            if i in lst2:
                print('YES')
                print(1, i)
                nk = 1
                break
        
        if nk == 0:
            print('NO')
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 1000\), for each iteration, `n` is the first integer input, `m` is the second integer input, `lst1` is a set of integers from the input string, `lst2` is a set of integers from the input string, `nk` is 0, and 'NO' is printed if no common elements are found. If a common element is found, 'YES' is printed followed by the common element and `nk` becomes 1.
#Overall this is what the function does:The function reads `t` test cases from standard input, where each test case includes two integers `n` and `m`, followed by `n` and `m` integers respectively. For each test case, it converts the input lists into sets, then checks if there is at least one common element between the two sets. If a common element is found, it prints 'YES' followed by the element; otherwise, it prints 'NO'. After processing all test cases, the function concludes. Potential edge cases include when `n` or `m` are 0 (though the problem constraints ensure \(1 \leq n, m \leq 1000\)), and when there are no common elements across all test cases, 'NO' will be printed for each case.

