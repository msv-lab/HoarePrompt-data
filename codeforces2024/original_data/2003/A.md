Turtle thinks a string s is a good string if there exists a sequence of
strings t_1, t_2, \ldots, t_k (k is an arbitrary integer) such that:

  * k \ge 2 . 
  * s = t_1 + t_2 + \ldots + t_k , where + represents the concatenation operation. For example, \texttt{abc} = \texttt{a} + \texttt{bc} . 
  * For all 1 \le i < j \le k , the first character of t_i isn't equal to the last character of t_j . 

Turtle is given a string s consisting of lowercase Latin letters. Please tell
him whether the string s is a good string!

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 500 ). The description of the test cases follows.

The first line of each test case contains a single integer n (2 \le n \le 100
) — the length of the string.

The second line of each test case contains a string s of length n , consisting
of lowercase Latin letters.

Output

For each test case, output "YES" if the string s is a good string, and "NO"
otherwise.

You can output the answer in any case (upper or lower). For example, the
strings "yEs", "yes", "Yes", and "YES" will be recognized as positive
responses.

Example

Input

    4
    
    2
    
    aa
    
    3
    
    aba
    
    4
    
    abcb
    
    12
    
    abcabcabcabc

Output

    No
    nO
    Yes
    YES
    
Note

In the first test case, the sequence of strings \texttt{a}, \texttt{a}
satisfies the condition s = t_1 + t_2 + \ldots + t_k , but the first character
of t_1 is equal to the last character of t_2 . It can be seen that there
doesn't exist any sequence of strings which satisfies all of the conditions,
so the answer is "NO".

In the third test case, the sequence of strings \texttt{ab}, \texttt{cb}
satisfies all of the conditions.

In the fourth test case, the sequence of strings \texttt{abca}, \texttt{bcab},
\texttt{cabc} satisfies all of the conditions.
