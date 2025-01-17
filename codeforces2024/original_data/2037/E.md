This is an interactive problem.

Kachina challenges you to guess her favorite binary string^{\text{∗}} s of
length n . She defines f(l, r) as the number of subsequences^{\text{†}} of
\texttt{01} in s_l s_{l+1} \ldots s_r . Two subsequences are considered
different if they are formed by deleting characters from different positions
in the original string, even if the resulting subsequences consist of the same
characters.

To determine s , you can ask her some questions. In each question, you can
choose two indices l and r (1 \leq l < r \leq n ) and ask her for the value of
f(l, r) .

Determine and output s after asking Kachina no more than n questions. However,
it may be the case that s is impossible to be determined. In this case, you
would need to report \texttt{IMPOSSIBLE} instead.

Formally, s is impossible to be determined if after asking n questions, there
are always multiple possible strings for s , regardless of what questions are
asked. Note that if you report \texttt{IMPOSSIBLE} when there exists a
sequence of at most n queries that will uniquely determine the binary string,
you will get the Wrong Answer verdict.

^{\text{∗}} A binary string only contains characters \texttt{0} and \texttt{1}
.

^{\text{†}} A sequence a is a subsequence of a sequence b if a can be obtained
from b by the deletion of several (possibly, zero or all) elements. For
example, subsequences of \mathtt{1011101} are \mathtt{0} , \mathtt{1} ,
\mathtt{11111} , \mathtt{0111} , but not \mathtt{000} nor \mathtt{11100} .

Input

The first line of input contains a single integer t (1 \leq t \leq 10^3 ) —
the number of test cases.

The first line of each test case contains a single integer n (2 \leq n \leq
10^4 ) — the length of s .

It is guaranteed that the sum of n over all test cases does not exceed 10^4 .

Interaction

To ask a question, output a line in the following format (do not include
quotes)

  * "\texttt{? l r} " (1 \leq l < r \leq n ) 

The jury will return an integer f(l, r) .

When you are ready to print the answer, output a single line in the following
format

  * If s is impossible to be determined, output "\texttt{! IMPOSSIBLE} " 
  * Otherwise, output "\texttt{! s} " 

After that, proceed to process the next test case or terminate the program if
it was the last test case. Printing the answer does not count as a query.

The interactor is not adaptive, meaning that the answer is known before the
participant asks the queries and doesn't depend on the queries asked by the
participant.

If your program makes more than n queries for one test case, your program
should immediately terminate to receive the verdict Wrong Answer. Otherwise,
you can get an arbitrary verdict because your solution will continue to read
from a closed stream.

After printing a query do not forget to output the end of line and flush the
output. Otherwise, you may get Idleness limit exceeded verdict. To do this,
use:

  * fflush(stdout) or cout.flush() in C++; 
  * System.out.flush() in Java; 
  * flush(output) in Pascal; 
  * stdout.flush() in Python; 
  * see the documentation for other languages.

Hacks

To make a hack, use the following format.

The first line should contain a single integer t (1 \leq t \leq 10^3 ) – the
number of test cases.

The first line of each test case should contain an integer n (2 \leq n \leq
10^4 ) — the length of s .

The following line should contain s , a binary string of length n .

The sum of n over all test cases should not exceed 10^4 .

Example

Input

    2
    5
    
    4
    
    0
    
    1
    
    2
    
    2
    
    0

Output

    ? 1 5
    
    ? 2 4
    
    ? 4 5
    
    ? 3 5
    
    ! 01001
    
    ? 1 2
    
    ! IMPOSSIBLE

Note

In the first test case:

In the first query, you ask Kachina for the value of f(1, 5) , and she
responds with 4 in the input stream.

In the second query, you ask Kachina for the value of f(2, 4) . Because there
are no subsequences of \texttt{01} in the string \texttt{100} , she responds
with 0 in the input stream.

After asking 4 questions, you report \texttt{01001} as s , and it is correct.

In the second test case:

In the first query, you ask Kachina for the value of f(1, 2) , and she
responds with 0 in the input stream. Notice that this is the only distinct
question you can ask.

However, notice that the strings 00 and 11 both have an answer of 0 , and it
is impossible to differentiate between the two. Therefore, we report
IMPOSSIBLE.

Please note that this example only serves to demonstrate the interaction
format. It is not guaranteed the queries provided are optimal or uniquely
determine the answer. However, it can be shown there exists a sequence of at
most 5 queries that does uniquely determine sample test case 1 .
