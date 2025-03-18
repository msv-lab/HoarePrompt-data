#State of the program right berfore the function call: The function `func` should take four non-negative integers `p1`, `p2`, `p3`, and `p4` as input, where each integer represents the count of 1s, 2s, 3s, and 4s in the sequence, respectively, and 0 <= p1, p2, p3, p4 <= 200.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The values of p1, p2, p3, and p4 remain unchanged.
#Overall this is what the function does:The function `func` reads an integer from the input, which specifies the number of sequences to process. For each sequence, it reads four integers from the input, calculates a count based on the parity of the first three integers and the floor division of each integer by 2, and prints this count. The function does not return any value. The input parameters `p1`, `p2`, `p3`, and `p4` mentioned in the comments are not actually used in the function, and their values remain unchanged.

