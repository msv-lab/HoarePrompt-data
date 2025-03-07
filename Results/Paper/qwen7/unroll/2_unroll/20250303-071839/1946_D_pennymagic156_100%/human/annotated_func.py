#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30; and the third line is empty or contains additional input which should be ignored.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers parsed from the input split by spaces.
#Overall this is what the function does:The function reads three lines of input from standard input. It ignores the first line containing two integers n and x, and parses the second line into a list of integers. Any additional input on the third line is also ignored. The function then returns this list of integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, followed by an array a of n integers where 0 ≤ a_i < 2^30.
def func_2():
    return int(input())
    #The program returns an integer input provided by the user, which represents the number of test cases (t) such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function accepts no parameters and returns an integer input provided by the user, representing the number of test cases (t), where 1 ≤ t ≤ 10^4.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Additionally, the subsequent line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing integers. The map object is created by converting the input split by spaces into integers. The number of elements in the map object corresponds to the number of integers inputted after the test case count.
#Overall this is what the function does:The function processes input data by reading a series of integers from standard input. It returns a map object containing these integers, where the number of elements in the map object matches the number of integers inputted after the test case count.

#State of the program right berfore the function call: The function does not receive any parameters and it is expected to be called within the main logic of another function that processes the test cases. It returns a string containing an integer, which represents the number of test cases.
def func_4():
    return input().strip()
    #The program returns a string containing an integer, which represents the number of test cases entered by the user and stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function reads an integer value representing the number of test cases from the user input, strips any leading or trailing whitespace, and returns this value as a string.

#State of the program right berfore the function call: (n, x) is a tuple of two integers where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; a is a list of n integers where 0 ≤ a_i < 2^30.
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
        
    #State: Output State: `t` is an empty list, `ans` is the maximum count of consecutive 1s found in the binary representation of the elements in `a` for each bit position from 29 to 0, `n` is a value between 1 and 100000, `x` is an integer between 0 and 2^30 - 1, `a` is the return value of `func_1()`.
    #
    #Explanation: The loop iterates over bit positions from 29 to 0. For each bit position, it checks the bit values of `x` and the elements in `a`. If both bits are 0, it skips. If the bit in `x` is 0 and the corresponding bit in `a`'s sum is odd, it returns `ans`. If the bit in `x` is 0 and the corresponding bit in `a`'s sum is even, it performs some operations on `a` and updates `t`. If the bit in `x` is 1 and the corresponding bit in `a`'s sum is odd, it skips. If the bit in `x` is 1 and the corresponding bit in `a`'s sum is even, it calculates the maximum count of consecutive 1s found in the binary representation of the elements in `a` for that bit position and updates `ans`. If the bit in `x` is 1 and the corresponding bit in `a`'s sum is 0, it breaks the loop. After the loop, `t` remains empty, `ans` contains the maximum count of consecutive 1s, and other variables retain their original values.
    return max(ans, len(a))
    #The program returns the maximum value between ans (which is the maximum count of consecutive 1s found in the binary representation of the elements in a for each bit position from 29 to 0) and the length of the list a.
#Overall this is what the function does:The function calculates the maximum count of consecutive 1s found in the binary representation of the elements in the list `a` for each bit position from 29 to 0. It then returns the maximum value between this count and the length of the list `a`.

