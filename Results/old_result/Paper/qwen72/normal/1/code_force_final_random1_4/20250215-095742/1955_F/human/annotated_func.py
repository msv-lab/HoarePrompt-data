#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i are four integers (0 <= p_i <= 200) representing the counts of 1s, 2s, 3s, and 4s in the sequence, respectively.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: After the loop executes all the iterations, `t` is an integer such that 1 <= t <= 10^4, and for each of the `t` test cases, `p` is a list of four even integers derived from the input, where each element is the nearest even number less than or equal to the corresponding input value. The loop prints the result of the expression `(sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2` for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, and for each test case, it reads four integers representing counts of 1s, 2s, 3s, and 4s. It then processes these counts to ensure they are even numbers and calculates a specific value based on the counts. The function prints the result of this calculation for each test case. After processing all test cases, the function completes without returning any value.

