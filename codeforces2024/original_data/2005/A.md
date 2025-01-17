Narek has to spend 2 hours with some 2-year-old kids at the kindergarten. He
wants to teach them competitive programming, and their first lesson is about
palindromes.

Narek found out that the kids only know the vowels of the English alphabet
(the letters \mathtt{a} , \mathtt{e} , \mathtt{i} , \mathtt{o} , and
\mathtt{u} ), so Narek needs to make a string that consists of vowels only.
After making the string, he'll ask the kids to count the number of
subsequences that are palindromes. Narek wants to keep it simple, so he's
looking for a string such that the amount of palindrome subsequences is
minimal.

Help Narek find a string of length n , consisting of lowercase English vowels
only (letters \mathtt{a} , \mathtt{e} , \mathtt{i} , \mathtt{o} , and
\mathtt{u} ), which minimizes the amount of palindrome^{\dagger}
subsequences^{\ddagger}  in it.

^{\dagger} A string is called a palindrome if it reads the same from left to
right and from right to left.

^{\ddagger} String t is a subsequence of string s if t can be obtained from s
by removing several (possibly, zero or all) characters from s and
concatenating the remaining ones, without changing their order. For example,
\mathtt{odocs} is a subsequence of
\texttt{c}{\color{red}{\texttt{od}}}\texttt{ef}{\color{red}{\texttt{o}}}\texttt{r}{\color{red}{\texttt{c}}}\texttt{e}{\color{red}{\texttt{s}}}
.

Input

The first line of the input contains a single integer t (1 \le t \le 100 ) —
the number of test cases. Subsequently, the description of each test case
follows.

The only line of each test case contains a single integer n (1 \le n \le 100 )
— the size of the string.

Output

For each test case, output any string of length n that satisfies the above
conditions.

Example

Input

    3
    
    2
    
    3
    
    6

Output

    uo
    iae
    oeiiua
    
Note

In the first example, \texttt{uo} has only three palindrome subsequences:
\texttt{u} , \texttt{o} , and the empty string. It can be shown that there is
no better answer.

In the third example, \texttt{oeiiua} has only eight palindrome subsequences:
\texttt{o} , \texttt{e} , \texttt{i} , \texttt{i} , \texttt{u} , \texttt{a} ,
\texttt{ii} , and the empty string. It can be shown that there is no better
answer.
