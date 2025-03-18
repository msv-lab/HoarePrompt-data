#State of the program right berfore the function call: The function receives no direct input arguments. Instead, it reads input from standard input. The input consists of multiple test cases. The first line contains a single integer t (1 \le t \le 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 \le n \le 2\cdot 10^5) representing the number of piles, and the next line contains n integers a_1, a_2, \ldots a_n (1 \le a_i \le 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2\cdot 10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns None and prints 'Alice'
    #State: `N` is an integer representing the number of test cases; `nums` is a sorted list of unique integers from the input line, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program returns None because `print('Bob')` outputs 'Bob' to the console and the return statement returns None.
    #State: `N` is an integer representing the number of test cases; `nums` is a sorted list of unique integers from the input line, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `N` is an integer representing the number of test cases; `nums` is a sorted list of unique integers from the input line with `0` inserted at the beginning, and the length of `nums` is now greater than 3; `cd` is the number of consecutive elements starting from `nums[0]` where the difference between consecutive elements is 1.
    if (cd & 1) :
        return print('Bob')
        #The program returns None after printing 'Bob'
    else :
        return print('Alice')
        #The program returns Alice
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a number of piles and the number of stones in each pile. It determines the winner of a game for each test case and prints either 'Alice' or 'Bob' to the console, indicating the winner. The function does not return any value (implicitly returns `None`).

