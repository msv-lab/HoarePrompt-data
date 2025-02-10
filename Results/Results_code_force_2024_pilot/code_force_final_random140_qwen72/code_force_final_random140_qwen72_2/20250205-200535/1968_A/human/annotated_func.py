#State of the program right berfore the function call: x is an integer such that 2 ≤ x ≤ 1000.
def func():
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: `x` is an integer such that 2 ≤ x ≤ 1000, `num` is an input integer representing the number of entries, `L1` is a list containing `num` elements, each element being an input integer, `res` is an empty list, `i` is `num - 1`.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: After the loop executes all the iterations, `x` remains an integer such that 2 ≤ x ≤ 1000, `num` is greater than 0, `L1` is a list containing `num` elements, each element being an input integer, `res` is a list containing exactly `num` elements. Each element in `res` corresponds to the result of `L1[i] // j * (j - 1)` for the smallest divisor `j` of `L1[i]` greater than or equal to 2, where `i` ranges from 0 to `num - 1`. The index `i` will have iterated through all valid indices in `L1` (i.e., from 0 to `num - 1`).
    print(*res, sep='\n')
    #This is printed: Each element of `res` on a new line, where each element is the result of `L1[i] // j * (j - 1)` for the smallest divisor `j` of `L1[i]` greater than or equal to 2, and `i` ranges from 0 to `num - 1`.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It prompts the user to enter the number of entries (`num`) and then asks for `num` integers, storing them in a list `L1`. For each integer in `L1`, the function finds the smallest divisor greater than or equal to 2, calculates the result of `L1[i] // j * (j - 1)` for this divisor, and appends this result to a list `res`. Finally, it prints each element of `res` on a new line. The function modifies the state by creating and populating the lists `L1` and `res`, and printing the contents of `res`.

