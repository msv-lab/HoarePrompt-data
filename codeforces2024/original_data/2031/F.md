This is an interactive problem.

Returning from a restful vacation on Australia's Gold Coast, Penchick forgot
to bring home gifts for his pet duck Duong Canh! But perhaps a beautiful
problem crafted through deep thought on the scenic beaches could be the
perfect souvenir.

There is a hidden permutation^{\text{∗}} p of length n , where n is even. You
are allowed to make the following query:

  * Choose a subsequence^{\text{†}} of the permutation p with even length 4\le k\le n . The interactor will return the value of the two medians^{\text{‡}} in the chosen subsequence. 

Find the index of the two medians in permutation p using at most 80 queries.

Note that the interactor is non-adaptive. This means that the permutation p is
fixed at the beginning and will not change based on your queries.

^{\text{∗}} A permutation of length n is an array consisting of n distinct
integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a
permutation, but [1,2,2] is not a permutation (2 appears twice in the array),
and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

^{\text{†}} A sequence a is a subsequence of a sequence b if a can be obtained
from b by the deletion of several (possibly, zero or all) element from
arbitrary positions.

^{\text{‡}} The two medians of an array a with even length k are defined as
the \frac{k}{2} -th and \left(\frac{k}{2} + 1\right) -th smallest element in
the array (1 -indexed).

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 1000 ). The description of the test cases follows.

The only line of each test case contains a single integer n (6 \le n \le 100 ,
n is even) — the length of the hidden permutation p .

For each test case, after reading the integer n , you should begin the
interaction and find the answer before reading n for the next test case.

It is guaranteed that the sum of n over all test cases does not exceed 10^4 .

Interaction

To make a query, print a single line in the following format:

  * \mathtt{?}\;k\;x_1\;x_2 \ldots x_{k-1}\;x_k (4\le k\le n , k is even, 1 \le x_i \le n , x_i is pairwise distinct) — the length of the chosen subsequence followed by the indices of the chosen subsequence. 

After each query, you should read a line containing two integers m_1 and m_2
(1 \le m_1 < m_2 \le n ) — the value of the two medians in array [p_{x_1},
p_{x_2}, \ldots, p_{x_{k-1}}, p_{x_k}] .

You can make at most 80 such queries in each test case.

To give the final answer, print a single line in the following format:

  * \mathtt{!}\;i_1\;i_2 (1\le i_1, i_2 \le n ) — the index of the two medians. 

Note that the order in which i_1 and i_2 is printed does not matter. In other
words, your solution is valid as long as p_{i_1} = \frac{n}{2} and p_{i_2} =
\frac{n}{2} + 1 , or p_{i_1} = \frac{n}{2} + 1 and p_{i_2} = \frac{n}{2} .

After printing each query do not forget to output the end of line and
flush^{\text{∗}} the output. Otherwise, you will get Idleness limit exceeded
verdict.

If, at any interaction step, you read -1 instead of valid data, your solution
must exit immediately. This means that your solution will receive Wrong answer
because of an invalid query or any other mistake. Failing to exit can result
in an arbitrary verdict because your solution will continue to read from a
closed stream.

Hack format

For hacks, use the following format.

The first line should contain t — the number of test cases.

The first line of each test case should contain a single even integer n .

The second line of each test case should contain a permutation p_1, p_2,
\ldots, p_n of length n .

As an example, the hack format for the example input is:

    2  
    6  
    6 2 3 5 1 4  
    10  
    10 9 8 7 6 5 4 3 2 1  
    
^{\text{∗}} To flush, use:

  * fflush(stdout) or cout.flush() in C++; 
  * sys.stdout.flush() in Python; 
  * see the documentation for other languages. 

Example

Input

    2
    6
    
    3 4
    
    3 4
    
    2 3
    
    10
    
    3 4
    
    6 7
    
Output

    ? 6 1 2 3 4 5 6
    
    ? 4 3 6 1 5
    
    ? 4 3 6 2 5
    
    ! 3 6
    
    ? 6 1 3 7 8 9 10
    
    ? 8 1 2 3 4 5 6 7 8
    
    ! 6 5

Note

In the first test case, the hidden permutation is p = [6, 2, 3, 5, 1, 4] .

  1. The entire permutation was chosen for the first query. The two medians of the entire permutation p are 3 and 4 . 
  2. The indices of the chosen subsequence in the second query are 3 , 6 , 1 , and 5 . The interactor returns the two medians of the subsequence [p_3, p_6, p_1, p_5] = [3, 4, 6, 1] , which are 3 and 4 . 
  3. The indices of the chosen subsequence in the second query are 3 , 6 , 2 , and 5 . The interactor returns the two medians of the subsequence [p_3, p_6, p_2, p_5] = [3, 4, 2, 1] , which are 2 and 3 .

The answer "! 3 6" is valid as p_3 = 3 and p_6 = 4 .

In the second test case, the hidden permutation is p = [10, 9, 8, 7, 6, 5, 4,
3, 2, 1] .

  1. The indices of the chosen subsequence in the second query are 1 , 3 , 7 , 8 , 9 , and 10 . The interactor returns the two medians of the subsequence [p_1, p_3, p_7, p_8, p_9, p_{10}] = [10, 8, 4, 3, 2, 1] , which are 3 and 4 . 
  2. The indices of the chosen subsequence in the second query are 1 , 2 , 3 , 4 , 5 , 6 , 7 , and 8 . The interactor returns the two medians of the subsequence [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8] = [10, 9, 8, 7, 6, 5, 4, 3] , which are 6 and 7 .

The answer "! 5 6" is valid as p_5 = 6 and p_6 = 5 .
