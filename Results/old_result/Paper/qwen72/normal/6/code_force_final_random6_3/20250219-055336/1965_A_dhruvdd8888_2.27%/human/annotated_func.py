#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2·10^5, and piles is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2·10^5, `piles` is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5, `N` is an input integer, `nums` is a sorted list of unique integers converted from the set of unique strings from the input. The length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2·10^5, `piles` is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5, `N` is an input integer, `nums` is a sorted list of unique integers converted from the set of unique strings from the input. The length of `nums` is greater than 1, and the length of `nums` is not equal to 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 2·10^5, `piles` is a list of n integers where 1 ≤ a_i ≤ 10^9, `N` is an input integer, `nums` is a sorted list of unique integers with a 0 inserted at the beginning and has at least 2 elements, `i` is the index of the last element in `nums` that was checked (i.e., `len(nums) - 2`), `cd` is the number of consecutive pairs of elements in `nums` that have a difference of 1, starting from the first element (0) up to the point where the difference is not 1 or the loop ends.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.
#Overall this is what the function does:The function reads an integer `N` and a list of integers from the user, converts the list to a set of unique integers, sorts them, and then determines the winner ('Alice' or 'Bob') based on the following logic: If the list has only one unique integer, 'Alice' wins. If the list has two unique integers, 'Bob' wins. If the list has more than two unique integers, the function checks for consecutive pairs of integers with a difference of 1. If the count of such consecutive pairs is odd, 'Bob' wins; otherwise, 'Alice' wins. The function prints the winner and returns `None`.

