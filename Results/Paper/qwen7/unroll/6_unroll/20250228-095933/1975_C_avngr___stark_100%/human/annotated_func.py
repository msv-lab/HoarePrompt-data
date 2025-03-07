#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of all n values across all test cases does not exceed 10^5.
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
        
    #State: Output State: t is an integer between 1 and 500 inclusive. For each value of t, there is a corresponding value of n (an integer), and a list a of integers. After executing the loop, for each n:
    #- If n is 2, the output is the minimum value in list a.
    #- If n is greater than 2, the output is the second largest value among all possible triplets in list a when considering the first two elements of each triplet.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer t (1 ≤ t ≤ 500), an integer n (2 ≤ n ≤ 10^5), and an array a consisting of n positive integers (1 ≤ a_i ≤ 10^9). If n is 2, it outputs the minimum value in array a. If n is greater than 2, it finds and outputs the second largest value among all possible triplets in array a, considering only the first two elements of each triplet.

