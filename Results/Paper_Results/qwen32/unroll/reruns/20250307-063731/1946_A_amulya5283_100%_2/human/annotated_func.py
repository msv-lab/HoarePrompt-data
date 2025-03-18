#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4). For each test case, n is a positive integer (1 ≤ n ≤ 10^5), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of all n across all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        if n == 1:
            print(1)
        else:
            res = 0
            mdx = n // 2 + n % 2 - 1
            for i in range(mdx, n):
                if a[mdx] == a[i]:
                    res += 1
            print(res)
        
    #State: The output state consists of the results printed for each test case. For each test case, the code prints the count of the most frequent element that appears in the second half of the sorted list (including the middle element if `n` is odd).
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it sorts the list and prints the count of the most frequent element that appears in the second half of the sorted list, including the middle element if `n` is odd.

