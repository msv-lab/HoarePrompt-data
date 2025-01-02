#State of the program right berfore the function call: s is a non-empty string consisting of lowercase Latin letters with a length not exceeding 105; k is an integer such that 0 ≤ k ≤ 13; each of the k lines contains a unique pair of different lowercase Latin letters representing forbidden pairs, and each letter appears in at most one forbidden pair.
def func_1():
    string = raw_input()
    pairs_num = input()
    pairs = []
    i = 0
    while i < pairs_num:
        pair = raw_input()
        
        pairs.append(pair)
        
        i += 1
        
    #State of the program after the loop has been executed: `string` is the input string, `s` is a non-empty string consisting of lowercase Latin letters with a length not exceeding 105, `k` is an integer such that 0 ≤ k ≤ 13, `pairs_num` is the original value of `pairs_num`, `pairs` is a list containing `pairs_num` unique pairs of different lowercase Latin letters, each letter appears in at most one forbidden pair, `i` is `pairs_num`.
    parser = Parser(string, pairs)
    print(parser.min_deletions())
#Overall this is what the function does:The function `func_1` reads an input string `s` and an integer `k`, followed by `k` pairs of forbidden characters. It then computes and prints the minimum number of deletions required to remove all occurrences of the forbidden pairs from the string `s`. The function does not return any value; instead, it directly prints the result. The final state of the program includes the original string `s`, the integer `k`, the list of forbidden pairs, and the printed result representing the minimum deletions needed. Edge cases include scenarios where `k` is 0 (no forbidden pairs), `s` contains no forbidden pairs, or `s` contains multiple instances of the same forbidden pair. The function assumes that each letter appears in at most one forbidden pair, and it handles the input and computation accordingly.

