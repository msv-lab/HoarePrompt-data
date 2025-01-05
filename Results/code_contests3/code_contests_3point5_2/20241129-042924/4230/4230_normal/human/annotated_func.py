#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000 and the sequence of opened doors is a list of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: If n is greater than or equal to 2, `ans` is equal to the index of the first occurrence where the value at index i is different from the value at index i + 1 in the list c. If such an index does not exist, `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function reads an integer n and a list of n integers representing the sequence of opened doors. It then iterates through the list to find the index of the first occurrence where the value at an index is different from the value at the next index. The function prints this index as the output. It does not return any value.

