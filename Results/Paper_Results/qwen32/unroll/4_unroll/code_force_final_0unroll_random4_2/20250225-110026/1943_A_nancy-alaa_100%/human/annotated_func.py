#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) representing the number of test cases. Each test case consists of two lines: the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: For each test case, the smallest integer i (0 ≤ i ≤ n) that either does not appear in the array or appears exactly once and is not the smallest such number that appears exactly once.
#Overall this is what the function does:For each test case, the function identifies and prints the smallest integer \( i \) (where \( 0 \leq i \leq n \)) that either does not appear in the array or appears exactly once, ensuring that if multiple such numbers exist, the smallest one is chosen.

