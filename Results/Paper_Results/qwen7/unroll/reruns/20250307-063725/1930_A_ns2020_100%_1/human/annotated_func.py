#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: The output state will be a list of sums, each sum being the result of adding every second element (starting from the first element) of the sorted lists provided in each iteration of the loop.
    #
    #Explanation: In each iteration of the while loop, the value of `t` is decremented by 1. The loop continues until `t` becomes 0. During each iteration, the user inputs an integer `n` and a list of `2n` integers. These integers are sorted, and the sum of every second element starting from the first element is printed. Since the initial value of `t` is an integer between 1 and 5000, the loop will execute this many times, each time processing a different set of input data. Therefore, the final output state will consist of `t` sums, each derived from the sorted input lists according to the specified rule.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and an integer `n`, along with `2n` integers. For each test case, it sorts the `2n` integers and calculates the sum of every second element starting from the first element. It repeats this process `t` times, outputting the sum for each test case. The final state of the program consists of a list of `t` sums, each derived from the sorted input lists according to the specified rule.

