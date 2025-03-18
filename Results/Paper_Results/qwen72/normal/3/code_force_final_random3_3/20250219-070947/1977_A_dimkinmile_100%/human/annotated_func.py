#State of the program right berfore the function call: The function should accept two parameters, n and m, where n and m are integers such that 1 ≤ n, m ≤ 100. Additionally, the function should be able to handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `n` and `m` are integers such that 1 ≤ n, m ≤ 100. The number of test cases `t` is an integer such that 1 ≤ t ≤ 100. `n` and `m` are assigned the values from the input, where the input is a space-separated string of two integers. If the difference between `n` and `m` is even and non-negative (i.e., (n - m) % 2 == 0 and n - m >= 0), the function proceeds with this condition. Otherwise, the difference between `n` and `m` is either not divisible by 2 or `n - m` is less than 0, and the function handles this alternative condition.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads two integers, `n` and `m`, from user input, where each integer is between 1 and 100. The function then checks if the difference between `n` and `m` is even and non-negative. If this condition is true, it prints "Yes"; otherwise, it prints "No". The function does not handle multiple test cases or return a list of results.

