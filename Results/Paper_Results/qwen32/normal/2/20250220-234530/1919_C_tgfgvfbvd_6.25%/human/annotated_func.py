#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t test cases consists of two lines: the first line contains an integer n such that 1 ≤ n ≤ 2·10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: A series of integers, each representing the count `c` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it calculates and prints the count of specific elements that satisfy certain conditions related to their values compared to the first two distinct elements encountered in the list.

