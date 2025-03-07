#State of the program right berfore the function call: There are t test cases where t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers representing the lengths of binary strings a and b respectively, such that 1 ≤ n, m ≤ 2 · 10^5. The sum of all n and m across all test cases does not exceed 2 · 10^5. The strings a and b consist only of the characters '0' and '1'.
def func_1():
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: a is the input string, b is the new input string, n is the length of a, m is the length of the new input string, k is the number of characters from a found in b in order, j is the position in b where the search stopped.
    print(k)
    #This is printed: k (where k is the number of characters from the string `a` found in the string `b` in order)
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings `a` and `b`. For each test case, it determines the maximum number of characters from `a` that can be found in `b` in the same order and prints this count for each test case.

