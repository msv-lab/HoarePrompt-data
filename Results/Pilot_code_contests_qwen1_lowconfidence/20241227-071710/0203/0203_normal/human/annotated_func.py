#State of the program right berfore the function call: a is a list of integers where each element represents the deliciousness of a sardine, and b is a list of integers where each element represents the fragrantness of a sardine. Both lists have the same length N (1 ≤ N ≤ 2 × 10^5), and -10^{18} ≤ A_i, B_i ≤ 10^{18} for all 1 ≤ i ≤ N.
def func_1(a, b):
    if (a % b == 0) :
        return b
        #The program returns a list 'b' of integers where each element represents the fragrantness of a sardine
    #State of the program after the if block has been executed: a is a list of integers where each element represents the deliciousness of a sardine, and b is a list of integers where each element represents the fragrantness of a sardine. Both lists have the same length N (1 ≤ N ≤ 2 × 10^5), and -10^{18} ≤ A_i, B_i ≤ 10^{18} for all 1 ≤ i ≤ N. The condition (a % b != 0) holds for at least one element in the lists.
    return func_1(b, a % b)
    #The program returns the result of the function call `func_1(b, a % b)` where `b` is a list of integers representing the fragrantness of sardines, and `a % b` is a list of integers representing the deliciousness of sardines modulo their corresponding fragrantness values.
#Overall this is what the function does:- The function does not explicitly handle the case where `a` and `b` are empty lists. In practice, the GCD of an empty list is considered to be 0, but this is not explicitly covered in the given code.

