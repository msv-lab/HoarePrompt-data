#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: t is an integer between 1 and 500 (inclusive), and it is now set to the integer input value; no other variables are defined or changed. The program prints the sum of the two largest numbers from each input list of integers, for a total of t times. No other variables are affected.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (1 ≤ t ≤ 500) indicating the number of test cases, followed by an integer n (2 ≤ n ≤ 100) and a list of n integers representing the number of pages in each book (1 ≤ a_i ≤ 10^9). For each test case, it sorts the list of page numbers in descending order and prints the sum of the two largest page numbers. After processing all test cases, it returns nothing.

