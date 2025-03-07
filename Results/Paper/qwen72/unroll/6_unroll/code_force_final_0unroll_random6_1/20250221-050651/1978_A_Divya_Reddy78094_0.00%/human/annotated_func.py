#State of the program right berfore the function call: The function should accept two parameters: a list of integers `a` representing the number of pages in each book, and an integer `n` representing the number of books, where 2 <= n <= 100 and 1 <= a_i <= 10^9 for all 1 <= i <= n.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: The loop will execute `t` times, and for each iteration, it will read an integer `n` and a list of `n` integers `nums`. It will sort `nums` in descending order and print the sum of the two largest numbers in `nums`. After all iterations, the values of `t`, `n`, and `nums` will be undefined or reset for the next iteration, and any other variables not affected by the loop will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of books, and a list of `n` integers `nums` representing the number of pages in each book. It then sorts the list `nums` in descending order and prints the sum of the two largest numbers in `nums`. The function does not return any value. After all test cases are processed, the values of `t`, `n`, and `nums` are undefined or reset for the next iteration, and any other variables not affected by the loop remain unchanged.

