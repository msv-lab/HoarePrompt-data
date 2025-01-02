#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of three lines: the first line contains two positive integers n and m such that 1 ≤ n, m ≤ 1000, representing the lengths of two arrays; the second line contains n integers a_1, …, a_n such that 1 ≤ a_i ≤ 1000, representing the elements of the first array; the third line contains m integers b_1, …, b_m such that 1 ≤ b_i ≤ 1000, representing the elements of the second array. It is guaranteed that the sum of n and the sum of m across all test cases does not exceed 1000 (∑_{i=1}^t n_i, ∑_{i=1}^t m_i ≤ 1000).
def func():
    input = lambda : stdin.readline().strip()
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        
        lst1 = [int(i) for i in input().split()]
        
        lst2 = [int(i) for i in input().split()]
        
        nk = 0
        
        lst1 = set(lst1)
        
        lst2 = set(lst2)
        
        for i in lst1:
            if i in lst2:
                print('YES')
                print(1, i)
                nk = 1
                break
        
        if nk == 0:
            print('NO')
        
    #State of the program after the  for loop has been executed: `nk` is 1 or 0, `n` is the number of integers in the first list, `m` is the number of integers in the second list, `lst1` is a set containing the unique elements from the first list, `lst2` is a set containing the unique elements from the second list, and if `nk` is 1, then 'YES' is printed along with the 1-based index and the value of the matching element; otherwise, if `nk` is 0, 'NO' is printed.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two arrays of integers. For each test case, it reads the lengths of the two arrays, `n` and `m`, followed by the elements of the arrays. It then checks if there is any common element between the two arrays. If a common element is found, the function prints 'YES' along with the 1-based index and the value of the matching element. If no common element is found, the function prints 'NO'. The function ensures that the sum of the lengths of the arrays across all test cases does not exceed 1000.

