#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: Output State: `v` is a list of length n+1 where the first element is 0, and the rest of the elements are integers from the input split and converted to int. The value printed is either 2 or nothing, depending on whether the condition `v[v[i]] == i` is met for any `i` in the range 1 to n. If the condition is met for any `i`, then 2 is printed; otherwise, nothing is printed.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function processes a single test case consisting of an integer `n` and a list `p` of `n` integers. It constructs a list `v` based on the input and checks if there exists an index `i` such that `v[v[i]] == i`. If such an index is found, it prints `2` and returns immediately. Otherwise, it prints `3`. The function does not return any value explicitly but modifies and uses the list `v` to determine the output.

