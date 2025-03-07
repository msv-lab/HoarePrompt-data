#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 500, and for each input, if n == 2, the output is the minimum value of the list a. Otherwise, the output is the second largest value among all possible triplets in the list a.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (number of inputs), followed by an integer n and an array a of n positive integers. If n equals 2, it outputs the minimum value in a. Otherwise, it finds and outputs the second largest value among all possible triplets in the array a.

