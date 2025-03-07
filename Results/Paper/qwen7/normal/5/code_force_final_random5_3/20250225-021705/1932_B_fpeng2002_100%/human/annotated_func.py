#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: After the loop executes all its iterations, `start_year` will be the result of applying the operation \((\text{start_year} // \text{nums}[x] + 1) * \text{nums}[x]\) for each index \(x\) from 0 to \(len(nums) - 1\), and `x` will be equal to \(len(nums)\).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`. It then calculates a value `start_year` by iteratively applying the operation \((\text{start_year} // \text{a}[x] + 1) * \text{a}[x]\) for each element in the list. Finally, it prints the calculated `start_year` for each test case.

