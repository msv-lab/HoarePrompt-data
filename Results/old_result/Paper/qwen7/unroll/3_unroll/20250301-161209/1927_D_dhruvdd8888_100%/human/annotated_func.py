#State of the program right berfore the function call: t is a positive integer; for each test case, n is an integer such that 2 <= n <= 2 * 10^5, the array a consists of n integers where each integer a_i is in the range [1, 10^6], q is an integer such that 1 <= q <= 2 * 10^5, and each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `s` is `N`, `t` is a positive integer, `n` is an integer such that 2 <= n <= 2 * 10^5, the array `a` consists of N+1 tuples where each tuple contains three elements: (1 + starting index, ending index, value at starting index), `q` is an integer such that 1 <= q <= 2 * 10^5, and `e` is 0; `num` is equal to `nums[N]`; `arr` is a list containing `-1` and N+1 tuples of the form (1 + starting index, ending index, value at starting index).
    LA = len(arr) - 1
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1 or s > r:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N or e < l:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: After all iterations of the loop, the values of `s`, `t`, `n`, `a`, `q`, `e`, `num`, `arr`, and `LA` remain unchanged. The loop processes input pairs `(l, r)` and prints output based on conditions, but does not modify any of the given variables.
#Overall this is what the function does:The function processes a series of queries on a given array. It first identifies segments of consecutive identical elements in the array and stores these segments along with their starting and ending indices. Then, for each query, it determines the segment that overlaps with the query range [l, r] and prints specific information based on the values within that segment. If no valid segment is found, it prints -1 -1. The function does not modify the original array or any other input parameters.

