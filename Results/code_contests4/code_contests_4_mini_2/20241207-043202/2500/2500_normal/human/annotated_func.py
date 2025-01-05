#State of the program right berfore the function call: N is an integer such that 1 <= N <= 60, K is an integer such that 1 <= K <= N, and each piece of meat is represented by its coordinates (x_i, y_i) as integers in the range -1000 to 1000, and hardness c_i as an integer in the range 1 to 100, with the condition that (x_i, y_i) are distinct for all i.
def func_1(i, j):
    return math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    #The program returns the Euclidean distance between two distinct pieces of meat located at coordinates (X[i], Y[i]) and (X[j], Y[j])
#Overall this is what the function does:The function accepts two integer indices `i` and `j`, and returns the Euclidean distance between two pieces of meat located at coordinates (X[i], Y[i]) and (X[j], Y[j]). It is assumed that `i` and `j` refer to distinct pieces of meat, as the function is designed to calculate the distance between them.

