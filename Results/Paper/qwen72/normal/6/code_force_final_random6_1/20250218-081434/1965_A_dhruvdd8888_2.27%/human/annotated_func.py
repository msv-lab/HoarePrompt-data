#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. test_cases is a list of tuples, where each tuple contains an integer n (1 <= n <= 2 * 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), representing the number of piles and the initial number of stones in each pile, respectively. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: `t` is an integer such that 1 <= t <= 10^4, `test_cases` is a list of tuples, where each tuple contains an integer n (1 <= n <= 2 * 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), `N` is an input integer, `nums` is a sorted list of integers representing the input values, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: `t` is an integer such that 1 <= t <= 10^4, `test_cases` is a list of tuples, where each tuple contains an integer n (1 <= n <= 2 * 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), `N` is an input integer, `nums` is a sorted list of integers representing the input values, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `test_cases` is a list of tuples, where each tuple contains an integer n (1 <= n <= 2 * 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), `N` is an input integer, `nums` is a sorted list of integers with a 0 inserted at the beginning, and the length of `nums` is greater than 3. `i` is the largest integer such that the difference between `nums[i + 1]` and `nums[i]` is 1 for all 0 <= i < len(nums) - 2, or `i` is the index where the difference is not 1. `cd` is the number of consecutive pairs of elements in `nums` starting from the first element (0) where the difference is 1, or `cd` remains the value it had when the loop broke.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of unique integers from user input, sorts the list, and determines the winner between 'Alice' and 'Bob' based on the sorted list. If the list contains only one unique integer, 'Alice' wins. If the list contains exactly two unique integers, 'Bob' wins. If the list contains more than two unique integers, the function checks for consecutive integers starting from the smallest (after inserting a 0 at the beginning of the list). If the number of such consecutive pairs is odd, 'Bob' wins; otherwise, 'Alice' wins. The function always prints the winner and returns `None`.

