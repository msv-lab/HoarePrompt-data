#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: Output State: The loop prints `3` after all iterations. This means that for the entire range of `i` from `0` to `x-1`, the condition `l[l[i] - 1] == i + 1` was never satisfied. Therefore, the flag `flag` remained `False` throughout the loop's execution, and the loop printed `3` after completing all its iterations.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer \( n \) (the size of the list \( p \)), followed by a list \( p \) of \( n \) integers. For each element in the list \( p \), it checks if the value at the index specified by \( p[i] - 1 \) equals \( i + 1 \). If this condition is met for any element, it prints `2`. If the condition is never met for any element, it prints `3` after processing all elements. The function does not return any value but outputs the result for each test case.

