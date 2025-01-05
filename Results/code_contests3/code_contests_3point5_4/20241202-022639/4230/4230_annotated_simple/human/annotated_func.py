#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000. The sequence of integers represents the doors Mr. Black opened, with 0 indicating a door in the left exit and 1 indicating a door in the right exit.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `c` is the mapped integer sequence of the input values, `ans` is the index of the last element in the sequence where the value changes, `i` is -1 at the end of the loop
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` representing the number of door openings that Mr. Black has made. It then reads a sequence of integers `c` representing the doors Mr. Black opened, with 0 indicating a door in the left exit and 1 indicating a door in the right exit. The function iterates through the sequence of door openings and determines the final exit point of Mr. Black based on the changes in the door values. The function prints the index of the last element in the sequence where the door value changes, indicating the exit point.

