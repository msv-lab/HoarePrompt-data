#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 100), representing the number of problems. This is followed by two lines: the first line contains a sorted list a of n integers (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9), representing the difficulties of the proposed problems, and the second line contains a sorted list b of n integers (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9), representing the expected difficulties of the problems. The number of test cases t is between 1 and 100.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: 1 0
#Overall this is what the function does:The function processes multiple test cases, each consisting of two sorted lists of integers representing the difficulties of proposed and expected problems. For each test case, it calculates and prints the count of expected difficulties that are less than the smallest unpaired proposed difficulty.

