#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n such that 1 ≤ a_i ≤ 10^6.
def func():
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = (start_year // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: Output State: The output state will be a series of integers, each corresponding to the value of `start_year` calculated for each test case.
    #
    #Explanation: For each test case specified by the input integer `num_tests`, the code reads an integer `n` and a list of `n` integers. It then iterates through the list, updating `start_year` based on the formula `(start_year // nums[x] + 1) * nums[x]`. After processing all the numbers in the list, it prints the final value of `start_year`. This process repeats for each test case, and the output consists of one integer per line, representing the final `start_year` value for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then updates a variable `start_year` based on a specific formula and prints the final value of `start_year` after processing all the numbers in the list. This process repeats for each test case, and the output consists of one integer per line, representing the final `start_year` value for each test case.

