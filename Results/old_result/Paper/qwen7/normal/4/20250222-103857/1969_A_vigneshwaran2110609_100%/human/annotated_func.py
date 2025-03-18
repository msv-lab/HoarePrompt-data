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
        
    #State: i is 49, x is 49, and flag is either True or False depending on whether the condition l[l[i] - 1] == i + 1 was met for any i from 0 to 48.
#Overall this is what the function does:The function processes multiple test cases, each defined by three values: `t`, `n`, and `p`. For each test case, it reads `n` integers from input, checks if the condition `l[l[i] - 1] == i + 1` holds for any index `i` within the range 0 to `x-1`, and prints 2 if the condition is met for any index. If the condition is not met for any index, it prints 3. The function does not return any value.

