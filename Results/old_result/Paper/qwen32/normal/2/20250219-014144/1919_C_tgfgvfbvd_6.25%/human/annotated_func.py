#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2⋅10^5), representing the size of the array a. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), which are the elements of the array a. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: For each test case, `a` is the smallest element in `l` that meets the loop's conditions, `b` is the second smallest element in `l` that meets the loop's conditions, and `c` is the count of elements greater than both `a` and `b`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the count of elements in the list that are greater than both the smallest and the second smallest elements encountered so far during the iteration through the list.

