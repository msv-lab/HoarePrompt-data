#State of the program right berfore the function call: The function should accept two parameters: an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list of integers p of length n (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend. The function should be called multiple times with different test cases, where the number of test cases t is an integer (1 ≤ t ≤ 5000).
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    if (n == 2) :
        print(2)
        #This is printed: 2
    else :
        for i in range(1, n + 1):
            if v[v[v[i]]] == i:
                print(2)
                return
            
        #State: `n` is greater than or equal to its initial value, `i` is `n + 1`, and `v[v[v[i]]]` is not equal to `i` for any `i` in the range from 1 to `n`.
        print(3)
        #This is printed: 3
    #State: *The function accepts two parameters: an integer `n` (2 ≤ n ≤ 50) and a list of integers `p` of length `n` (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct). The function is called multiple times with different test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 5000). `n` is an input integer, and `v` is a list of length `n + 1` initialized with the input integers, with an additional 0 at the beginning. If `n` is 2, the current value of `n` remains 2. If `n` is greater than 2, `i` is set to `n + 1`, and `v[v[v[i]]]` is not equal to `i` for any `i` in the range from 1 to `n`.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads an integer `n` from the input, representing the number of friends, and a list of integers `p` of length `n`, representing the best friends of each friend. For each test case, if `n` is 2, it prints 2. If `n` is greater than 2 and there exists any friend `i` such that the best friend of the best friend of the best friend of `i` is `i` itself, it prints 2. Otherwise, it prints 3. The function is designed to be called multiple times with different test cases.

