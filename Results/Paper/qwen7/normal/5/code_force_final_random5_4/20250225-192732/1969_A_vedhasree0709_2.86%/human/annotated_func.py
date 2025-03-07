#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: The loop will continue to iterate for each test case until the specified number of iterations (as determined by `input()`) is completed. After all iterations, the final state will depend on whether the condition `l[i] == i + 2 and l[i + 1] == i + 1` was met for any `i` within the range of the loop for each test case.
    #
    #If the condition `l[i] == i + 2 and l[i + 1] == i + 1` is met for any `i` during any of the iterations, `j` will be set to 1, and the loop will print `2` and break. This means that for the test cases where this condition is met, the output will be `2`.
    #
    #For the remaining test cases where the condition is not met, `j` will remain `0`, and the loop will print `3`.
    #
    #Since we do not know the exact number of test cases or the contents of the lists `l` for each test case, the final output state can be described as follows:
    #
    #- For each test case, if the condition `l[i] == i + 2 and l[i + 1] == i + 1` is met at any point during the loop, the output will be `2`.
    #- For all other test cases, the output will be `3`.
    #
    #Therefore, the output state after the loop executes all the iterations is: The loop has completed all its iterations, and the outputs consist of `2` for the test cases where the specified condition was met and `3` for the rest of the test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list `l` of length `n`. For each test case, it checks if there exists an index `i` where `l[i] == i + 2` and `l[i + 1] == i + 1`. If such an index is found, it prints `2`; otherwise, it prints `3`. The function does not return a value but prints the result for each test case.

