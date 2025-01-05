#State of the program right berfore the function call: N is a positive integer, a_i is an integer for each i such that 1 ≤ i ≤ N, and 0 ≤ a_i ≤ 1000.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads input values for N and a list of integers. It then calculates the absolute difference between the maximum and minimum values in the list 'a' and prints the result. The function does not accept any parameters explicitly, but it implicitly relies on user input for N and the list 'a'.

