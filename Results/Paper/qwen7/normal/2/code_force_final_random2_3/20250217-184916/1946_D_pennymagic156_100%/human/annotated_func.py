#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The following line contains a list of n integers representing the array a, where 0 ≤ a_i < 2^30.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers entered by the user, split from a single input string. Each integer in the list corresponds to an element in the array 'a' as specified in the input.
#Overall this is what the function does:The function reads a single input string from the user, which contains multiple integers separated by spaces. It then converts these integers into a list and returns this list. Each integer in the returned list corresponds to an element in the array 'a' as specified in the input.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 <= n <= 10^5 and 0 <= x < 2^30. Additionally, the input consists of n integers a_1, a_2, ..., a_n for each test case, where 0 <= a_i < 2^30.
def func_2():
    return int(input())
    #The program returns an integer input provided by the user for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer input provided by the user. It does not modify any input parameters and simply returns this integer input for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, representing the length of the array a and the favorite number x respectively. a is a list of n integers such that 0 ≤ a_i < 2^30, representing the array a itself.
def func_3():
    return map(int, input().split())
    #The program returns a tuple of integers obtained from user input split and converted to integers.
#Overall this is what the function does:The function processes user input by splitting a single line of space-separated integers and converting them into a tuple of two integers.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 <= n <= 10^5 and 0 <= x < 2^30. Additionally, the subsequent lines contain an array a of n integers where 0 <= a_i < 2^30.
def func_4():
    return input().strip()
    #The program returns the first line of input as a string after stripping any trailing whitespace.
#Overall this is what the function does:The function reads the first line of input as a string, strips any trailing whitespace, and returns it. This action is performed without requiring any parameters.

#State of the program right berfore the function call: (n, x) is a tuple of two integers where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; a is a list of n integers where 0 ≤ a_i < 2^30 for all i from 1 to n.
def func_5():
    n, x = func_3()
    a = func_1()
    t, ans = [], -1
    for i in range(29, -1, -1):
        u, v = x >> i & 1, sum([(val >> i & 1) for val in a])
        
        if u == v == 0:
            continue
        
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= val >> i & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                a, t = t, []
        elif v % 2:
            continue
        elif v:
            op = cnt = 0
            for val in a:
                op ^= val >> i & 1
                if not op:
                    cnt += 1
            ans = max(ans, cnt)
        else:
            break
        
    #State: i is 0, u is 0, and v is even.
    return max(ans, len(a))
    #The program returns the maximum value between ans (which is not defined in the given state) and the length of list a (which is not defined in the given state)
#Overall this is what the function does:The function processes a list of integers `a` and an integer `x`, and calculates a maximum count based on certain conditions. Specifically, it iterates over bits from the most significant to the least significant (29 to 0). For each bit position, it checks the bit value of `x` and the sum of corresponding bits in the list `a`. If certain conditions are met, it updates a counter `ans` or returns early. Finally, it returns the maximum value between `ans` (if defined) and the length of the list `a`. If `ans` is not defined, it returns 28.

