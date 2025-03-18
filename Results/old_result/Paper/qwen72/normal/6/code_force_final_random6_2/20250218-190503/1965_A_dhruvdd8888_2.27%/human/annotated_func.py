#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains two elements: the first element is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second element is a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The length of test_cases is t (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: `test_cases` is a list of tuples, where each tuple contains two elements: the first element is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second element is a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The length of `test_cases` is t (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 2·10^5. `N` is an input integer. `nums` is now a sorted list of integers, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: `test_cases` is a list of tuples, where each tuple contains two elements: the first element is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second element is a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The length of `test_cases` is t (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 2·10^5. `N` is an input integer. `nums` is now a sorted list of integers, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `test_cases` is a list of tuples, `N` is an input integer, `nums` is a sorted list of integers with an additional 0 inserted at the beginning and the length of `nums` is greater than 3, `i` is the index of the last element in `nums` that was checked before the loop terminated. If all consecutive elements from `nums[1]` to `nums[len(nums) - 2]` have a difference of 1, then `cd` is `len(nums) - 3`. Otherwise, `cd` is the number of consecutive elements starting from `nums[1]` that have a difference of 1 before the first non-consecutive pair is found.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, which represents the number of distinct integers in a set. It then reads a line of input, splits it into a set of strings, converts them to integers, and sorts the resulting list. If the length of the sorted list `nums` is 1, it prints 'Alice'. If the length is 2, it prints 'Bob'. For lengths greater than 2, it inserts a 0 at the beginning of `nums` and checks for consecutive integers starting from the second element. If the number of consecutive integers (excluding the first 0) is odd, it prints 'Bob'; otherwise, it prints 'Alice'. In all cases, the function returns `None`.

