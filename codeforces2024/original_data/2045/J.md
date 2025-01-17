You are given an array A of N integers: [A_1, A_2, \dots, A_N] .

The array A is (p, q) -xorderable if it is possible to rearrange A such that
for each pair (i, j) that satisfies 1 \leq i < j \leq N , the following
conditions must be satisfied after the rearrangement: A_i \oplus p \leq A_j
\oplus q and A_i \oplus q \leq A_j \oplus p . The operator \oplus represents
the bitwise xor.

You are given another array X of length M : [X_1, X_2, \dots, X_M] . Calculate
the number of pairs (u, v) where array A is (X_u, X_v) -xorderable for 1 \leq
u < v \leq M .

Input

The first line consists of two integers N M (2 \leq N, M \leq 200\,000) .

The second line consists of N integers A_i (0 \leq A_i < 2^{30}) .

The third line consists of M integers X_u (0 \leq X_u < 2^{30}) .

Output

Output a single integer representing the number of pairs (u, v) where array A
is (X_u, X_v) -xorderable for 1 \leq u < v \leq M .

Examples

Input

    3 4
    0 3 0
    1 2 1 1
    
Output

    3
    
Input

    5 2
    0 7 13 22 24
    12 10
    
Output

    1
    
Input

    3 3
    0 0 0
    1 2 3
    
Output

    0
    
Note

Explanation for the sample input/output #1

The array A is (1, 1) -xorderable by rearranging the array A to [0, 0, 3] .

Explanation for the sample input/output #2

The array A is (12, 10) -xorderable by rearranging the array A to [13, 0, 7,
24, 22] .
