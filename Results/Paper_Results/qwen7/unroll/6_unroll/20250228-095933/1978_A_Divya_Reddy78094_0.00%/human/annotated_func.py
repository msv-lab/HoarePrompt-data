#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and it is now equal to the value it was initialized to. For each iteration of the loop, n is an integer read from input, and nums is a list of integers sorted in descending order. The output for each iteration is the sum of the first two elements of the sorted list, printed to the console. After all iterations, the value of t remains unchanged, but the outputs consist of the sums of the two largest numbers from each input list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (1 ≤ t ≤ 500) and t pairs of integers. For each pair, it reads an integer n (2 ≤ n ≤ 100) and a list of n integers (1 ≤ a_i ≤ 10^9). It sorts the list of integers in descending order and prints the sum of the two largest numbers for each pair. After processing all test cases, it outputs the sums of the two largest numbers for each input list.

