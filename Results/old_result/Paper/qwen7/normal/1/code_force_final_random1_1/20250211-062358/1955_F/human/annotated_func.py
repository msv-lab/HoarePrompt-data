#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: Output State: The final state of `p` is a list of integers where each element is the largest even number less than or equal to the corresponding input integer, and the input integer has been reduced to 0 after all iterations of the loop.
    #
    #In natural language, after the loop has executed all its iterations, the list `p` will contain the largest even numbers possible for each of the initial counts of 1s, 2s, 3s, and 4s, with the input integer being decremented until it reaches 0. This means that each count in `p` will be the highest even number that was ever present in the sequence during any iteration of the loop, and the input integer will be 0 since it keeps decrementing by 1 in each iteration until it can no longer decrease.
#Overall this is what the function does:The function processes four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each input, it calculates the largest even number less than or equal to each of the counts and prints whether the sum of the counts of odd numbers (excluding the count of 4s) is 3, followed by the total sum of the processed counts divided by 2. After processing all inputs, the function outputs a series of results based on the given conditions.

