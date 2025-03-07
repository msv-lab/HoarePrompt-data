#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the input consists of n integers a_1, a_2, \ldots, a_n where -n ≤ a_i ≤ n. It is guaranteed that there is at least one valid permutation p for the given data, and the sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    maxx = 0
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            minn += 1
            if minn == maxx:
                minn = maxx + 1
        else:
            mex.append(abs(arr[i] - minn))
            if abs(arr[i] - minn) > maxx:
                maxx = abs(arr[i] - minn)
        
    #State: Output State: `minn` is either `maxx` + 1, `maxx` + 2, ..., up to `maxx + n`, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is an input integer such that \(1 \leq n \leq 2 \times 10^5\), `arr` is a list of integers obtained from splitting the input string by spaces and converting each element to an integer, `mex` is a list containing either the absolute difference between each element in `arr` and `minn`, followed by `minn`, or an additional element which is the absolute difference between `arr[i]` and `minn` for each iteration, and `maxx` is the maximum value between `maxx` and `abs(arr[i] - minn)` for each iteration where `abs(arr[i] - minn) > maxx`.
    #
    #In simpler terms, after all iterations of the loop have finished:
    #- `minn` will be at least `maxx + 1` and can be as high as `maxx + n`.
    #- `t`, `n`, and `arr` will retain their initial values.
    #- `mex` will contain all the values calculated during the loop, including the absolute differences and the values of `minn` appended when `arr[i] > 0`.
    #- `maxx` will be the highest value it was updated to during any iteration of the loop.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `mex` will contain all the absolute differences between each element in `arr` and `minn`, starting from `minn` being `maxx + 1` up to `maxx + n`. Additionally, `minn` will be appended to `mex` for each iteration where `arr[i] > 0`, and `maxx` will be the maximum value it was updated to during any iteration of the loop.
    print()
    #This is printed: Output:
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \), and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). For each test case, it calculates a sequence of integers stored in `mex` based on the input array and a variable `minn`. After processing all test cases, it prints the elements of `mex` for each test case. The final state of the program includes the printed sequence of integers for each test case, while the input variables `t`, `n`, and `arr` remain unchanged.

