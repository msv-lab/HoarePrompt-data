#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and piles is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2·10^5, `piles` is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5, `N` is an input integer, `nums` is a sorted list of integers converted from the set of strings from the input, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2·10^5, `piles` is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5, `N` is an input integer, `nums` is a sorted list of integers converted from the set of strings from the input, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `cd` is the number of consecutive integers starting from the first element in `nums` (excluding the 0 at the beginning) until the first gap greater than 1 is encountered, or until the end of the list if all elements are consecutive. The values of `t`, `n`, `piles`, and `N` remain unchanged.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of integers from the input, processes the list to determine a winner between 'Alice' and 'Bob', and prints the winner. The function does not accept any parameters and does not return any value. The state of the program remains unchanged except for the printed output, which is either 'Alice' or 'Bob' based on the input list.

