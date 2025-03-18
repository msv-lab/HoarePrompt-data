#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers where each integer a_i is in the range 1 <= a_i <= 10^6; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
def func_1():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    s = 0
    e = 0
    num = nums[0]
    arr = []
    nums.append(-1)
    for i in range(N + 1):
        if nums[i] != num:
            arr.append((1 + s, i, num))
            s = i
        
        num = nums[i]
        
    #State: Output State: `arr` will contain tuples representing the start and end indices along with the value of `num` for each segment of consecutive identical elements in the list `nums`. Specifically, `arr` will include a tuple for every change in the value of `num` within the list `nums`, starting from the index `s` up to `N`.
    #
    #In more detail, `arr` will be a list of tuples, where each tuple is of the form `(start_index, end_index, value)`, indicating that the value `value` was encountered in the list `nums` from index `start_index` to `end_index - 1`. The loop iterates through the entire list `nums` (from index 0 to `N`), and whenever it encounters a different value than the current `num`, it appends a new tuple to `arr` with the current start index (`s`), the current index (`i`), and the value of `num` before the change. After appending, it updates `s` to the current index `i` and sets `num` to the new value found at index `i`. This process continues until the loop completes all iterations over `nums`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [value1, value1, ..., valueN]
    #State: Postcondition: `arr` is a list of tuples, where each tuple is of the form (start_index, end_index, value), indicating segments of consecutive identical elements in the list `nums`. The last element in `arr` is updated to reflect the end of the last segment, and `LA` is set to the length of `arr` minus one. The current value of `ppp` is 23.
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        if tc > 5:
            if ppp == 23:
                print(l, r)
            continue
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: The loop will run until the user inputs a number greater than 5 for `tc`. Since the initial value of `ppp` is 23 and it is not modified within the loop, `ppp` will remain 23 after all iterations. The values of `l` and `r` will be the last pair of integers entered by the user during the loop. The variables `eli`, `s`, `e`, and `_` will be determined based on the last iteration's conditions.
#Overall this is what the function does:The function processes a list of integers and handles a series of queries. Initially, it constructs a list of segments where each segment contains consecutive identical elements from the input list. For each query, it determines the segment that covers the specified range `[l, r)` and outputs the start and end indices of that segment, or `-1` if no such segment exists. The function does not return any value but prints the results directly.

