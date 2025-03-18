#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains an integer n such that 1 ≤ n ≤ 3 ⋅ 10^5, and a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: Output State: `i` is equal to `n`; `st` is a set containing `n` elements, each element being one of the values `arr[i] + i + 1` for `i` ranging from `0` to `n-1`.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `i` will have the value of `n`, indicating that all elements in the range of the loop have been processed. The set `st` will contain `n` unique elements, each of which is the sum of an element from the list `arr` and its index plus one (`arr[i] + i + 1`).
    print(*sorted(st, reverse=True))
    #This is printed: the n unique elements of st sorted in descending order
#Overall this is what the function does:The function processes input data consisting of multiple test cases, where each test case includes an integer `n` and a list of `n` integers. For each test case, it computes the sum of each list element and its index plus one (`arr[i] + i + 1`), stores these sums in a set to ensure uniqueness, and then prints these unique sums in descending order. The function does not return any value but modifies and prints the output based on the input provided.

