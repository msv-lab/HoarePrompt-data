#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: After the loop executes all its iterations, `i` will be equal to `n`, `t` will be an integer such that \(1 \leq t \leq 5000\), `n` will be a non-negative integer, `l` will be a list of integers obtained from splitting the input string and converting each element to an integer, and `j` will be 0.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer `t` (1 ≤ t ≤ 5000), an integer `n` (2 ≤ n ≤ 50), and a list `p` of `n` integers (1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct). For each test case, the function checks if there exists a pair of consecutive elements in the list `p` such that one element is `i+2` and the next is `i+1`. If such a pair is found, the function prints `2` and stops processing further test cases. If no such pair is found after checking all elements, the function prints `3`. The function does not return any value but prints the result for each test case.

