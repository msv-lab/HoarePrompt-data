#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of integers representing the doors opened by Mr. Black consists of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 3 <= n <= 200,000, `c` is a map object created by converting the input integers to integers and splitting them, `ans` is the value of the first index where the element changes in the sequence
    print(ans)
#Overall this is what the function does:The function `func` reads input representing the number of doors `n` and a sequence of door states. It iterates through the sequence to find the index where the door state changes and prints that index as output. The function does not return a specific value, and the output depends on the provided sequence of integers. The code might not handle cases where the door state sequence has certain patterns or edge cases, as it only focuses on finding the index of the first change in the sequence.

