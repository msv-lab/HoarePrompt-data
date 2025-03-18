#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n is a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles, and piles is a list of n positive integers (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: t is a positive integer (1 ≤ t ≤ 10^4), n is a positive integer (1 ≤ n ≤ 2·10^5), piles is a list of n positive integers (1 ≤ a_i ≤ 10^9), `nums` is now a sorted list of integers converted from the unique strings in the original `nums` set, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: t is a positive integer (1 ≤ t ≤ 10^4), n is a positive integer (1 ≤ n ≤ 2·10^5), piles is a list of n positive integers (1 ≤ a_i ≤ 10^9), `nums` is now a sorted list of integers converted from the unique strings in the original `nums` set, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: cd is the number of consecutive integers starting from the first element in the `nums` list (excluding the 0 at the beginning) until the first non-consecutive integer is encountered, or until the loop reaches the second last element of `nums`. The values of `t`, `n`, and `piles` remain unchanged.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, followed by a list of `N` unique integers. It then prints 'Alice' or 'Bob' based on the following conditions: if the list contains only one unique integer, it prints 'Alice'; if the list contains exactly two unique integers, it prints 'Bob'; if the list contains more than two unique integers, it checks for the number of consecutive integers starting from the smallest (excluding the 0 inserted at the beginning). If the count of consecutive integers is odd, it prints 'Bob'; otherwise, it prints 'Alice'. The function always returns `None`. The original values of `t`, `n`, and `piles` remain unchanged.

