#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: `t` integers are appended to the `results` list. If the count of 'U' in each input string `arr` is odd, 'yes' is appended; otherwise, 'no' is appended.
    for i in results:
        print(i)
        
    #State: Output State: The `results` list contains 'yes' or 'no' based on whether the count of 'U' in each input string `arr` is odd or even, respectively, and then each element in `results` is printed on a new line.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by `t` pairs of integers `n` and strings `s` of length `n` containing only "U" and "D". It checks if the count of "U" in each string `s` is odd or even and appends "yes" or "no" to the `results` list accordingly. Finally, it prints each element in the `results` list on a new line.

