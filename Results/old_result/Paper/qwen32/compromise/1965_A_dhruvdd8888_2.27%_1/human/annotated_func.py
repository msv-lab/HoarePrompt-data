#State of the program right berfore the function call: The function `func_1` takes no arguments but operates on input provided through standard input. The input consists of multiple test cases. For each test case, the first line contains an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of two lines: the first line contains an integer `n` (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of `n` across all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns Alice
    #State: `N` is an integer representing the number of test cases; `nums` is a sorted list of integers derived from the unique numbers from the input line, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program returns None because `print('Bob')` outputs 'Bob' to the console and does not return a value.
    #State: `N` is an integer representing the number of test cases; `nums` is a sorted list of integers derived from the unique numbers from the input line, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: N is unchanged; nums is unchanged; cd is the count of consecutive elements in nums (starting from index 0) where the difference between consecutive elements is 1.
    if (cd & 1) :
        return print('Bob')
        #The program returns None because `print('Bob')` outputs 'Bob' to the console and returns None.
    else :
        return print('Alice')
        #The program returns None, as the print function returns None and Alice is printed to the console.
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. For each test case, it evaluates the number of piles and the number of stones in each pile. Based on these evaluations, it prints either "Alice" or "Bob" to the console. The function does not return any explicit value; it only outputs a name to the console.

