#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, participant numbers (a_i) are unique integers between 1 and n, and the number of fish caught (v_i) for each participant is an integer such that 0 ≤ v_i ≤ 100.
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 20; `value` is the maximum number of fish caught by any participant or -1 if no valid `v` was encountered; `number` is the participant number associated with `value` or remains `maxsize` if no participants were processed.
    print(number, value)
    exit()
#Overall this is what the function does:The function accepts a callable `readline` that reads input lines, processes participant numbers and the number of fish caught by each participant, and identifies the participant with the highest number of fish caught. In the event of a tie in the number of fish, it returns the smallest participant number. If no valid participants are processed, it defaults to returning the maximum size integer (indicating no valid data), along with -1 for the number of fish caught. The function does not return a value but prints the participant number and the corresponding fish count before exiting.

