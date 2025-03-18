#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should be `def func_1(t, test_cases):` where `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), and `test_cases` is a list of test cases. Each test case is a tuple containing the length of the array `n` (2 ≤ n ≤ 2·10^5), the array `a` (a list of integers where 1 ≤ a_i ≤ 10^6), and a list of queries `q` (1 ≤ q ≤ 2·10^5), where each query is a tuple of two integers `l` and `r` (1 ≤ l < r ≤ n). The sum of `n` and `q` across all test cases does not exceed 2·10^5.
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
        
    #State: The loop has completed all iterations, `i` is `N`, `num` is the last element in the `nums` list (which is `-1`), and `arr` contains tuples representing the start and end indices of contiguous segments of the same number in the `nums` list, along with the number itself. The variable `s` is the index of the last segment's start position.
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
        
    #State: The loop has completed all iterations, `i` is `N`, `num` is `-1`, `arr` contains tuples representing the start and end indices of contiguous segments of the same number in the `nums` list, along with the number itself. The variable `s` is the first element of the tuple at the index `min(eli, LA)` in `arr`, and `e` is the second element of the tuple at the index `min(eli, LA)` in `arr`. The variable `_` is the number of times the loop has executed, which is equal to the integer value provided by `int(input())`. The variable `LA` is `len(arr) - 1`. The values of `s`, `e`, and `num` after the loop depends on the conditions evaluated during each iteration, but the final state will be such that the conditions for the last iteration are met.
#Overall this is what the function does:The function `func_1` processes a series of queries on an input array. It reads an integer `N` representing the length of the array, followed by the array itself. It then reads a series of queries, each consisting of two integers `l` and `r`. For each query, the function determines and prints a pair of indices that represent the boundaries of a segment in the array where the segment starts and ends with the same number, and this segment is adjacent to the range `[l, r]`. If no such segment exists, it prints `(-1, -1)`. The function does not return any value; it only prints the results of the queries.

