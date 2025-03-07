#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and the sum of all m values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After all iterations of the loop have finished, `i` will be equal to `n`, `j` will be equal to `m`, and `k` will be the count of elements in `a` that have a matching element in `b` up to index `m-1`.
    print(k)
    #This is printed: k (where k is the count of elements in `a` that have a matching element in `b` up to index `m-1`)
    return
    #The program returns the count of elements in list 'a' that have a matching element in list 'b' up to index 'm-1'
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers \( n \) and \( m \), and two binary strings \( a \) and \( b \). It counts and returns the number of characters in string \( a \) that have a matching character in string \( b \) up to index \( m-1 \).

