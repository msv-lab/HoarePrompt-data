#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful. The sum of n over all test cases does not exceed 3 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: - `same` will be 1 (since it is reset to 1 whenever a new segment starts and the loop ends after processing the last segment).
    #- `num` will be the last number in the last test case's list `ar`.
    #- `minn` will be the minimum length of contiguous segments of identical numbers found in the last test case, or `-1` if the entire list was a single segment.
    #- `i` will be equal to the length of the last test case's list `ar` (since the loop increments `i` until it reaches the end of the list).
    #- `ar` will be the list of integers from the last test case.
    #- `n` will be the length of the last test case's list.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then determines the minimum length of contiguous segments of identical numbers in the list. If the entire list consists of a single segment of identical numbers, it returns `-1`. Otherwise, it returns the minimum length of these segments.

