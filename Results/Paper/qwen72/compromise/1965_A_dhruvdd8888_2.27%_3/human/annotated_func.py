#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2⋅10^5, and piles is a list of n integers where 1 ≤ piles[i] ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2⋅10^5, `piles` is a list of n integers where 1 ≤ piles[i] ≤ 10^9, `N` is an input integer, `nums` is a sorted list of unique integers, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2⋅10^5, `piles` is a list of n integers where 1 ≤ piles[i] ≤ 10^9, `N` is an input integer, `nums` is a sorted list of unique integers, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2⋅10^5, `piles` is a list of n integers where 1 ≤ piles[i] ≤ 10^9, `N` is an input integer, `nums` is a sorted list of unique integers with a length greater than 2, and 0 is inserted at the beginning of `nums`, `cd` is the number of consecutive pairs of integers in `nums` starting from the first element (excluding 0) that have a difference of 1.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function `func_1` reads an integer `N` from the user input, then reads a space-separated list of integers, converts it to a set to remove duplicates, and sorts the resulting unique integers. It then determines the winner between 'Alice' and 'Bob' based on the following criteria: if the length of the sorted unique integers is 1, it prints 'Alice'; if the length is 2, it prints 'Bob'; otherwise, it counts the number of consecutive pairs of integers starting from the first element (excluding 0) that have a difference of 1. If this count is odd, it prints 'Bob'; if even, it prints 'Alice'. In all cases, the function returns `None`.

