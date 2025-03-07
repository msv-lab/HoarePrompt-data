#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: Output State: After the loop executes all its iterations, `t` will be equal to the total number of iterations completed, which is the initial value of `t` plus the number of additional iterations minus one (since the loop starts counting from 0). For each iteration, `n` will be an input integer, and `nums` will be a list of integers sorted in descending order after sorting. The final state of `nums` will be the result of sorting the last input list of integers in descending order.
    #
    #In simpler terms, `t` will be the total number of iterations the loop ran, `n` will be the most recent input integer, and `nums` will be the sorted list of integers from the last input, sorted in descending order.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer t indicating the number of test cases, an integer n indicating the number of books, and a list of n integers representing the number of pages in each book. It then sorts these page numbers in descending order and prints the sum of the first two page numbers for each test case. The function does not return any value but prints the results for each test case.

