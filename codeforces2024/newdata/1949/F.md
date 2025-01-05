You are the developer of a dating app which ignores gender completely. The app
has n users, indexed from 1 to n . Each user's profile features a list of the
activities they enjoy doing. There are m possible activities, indexed from 1
to m .

A match between two users is good if they share at least one activity and, at
the same time, both of them like at least one activity that the other user
does not like.

Find a good match if it exists.

Input

The first line contains two integers n and m (2 \leq n \leq 200\,000 , 1 \leq
m \leq 10^6 ) — the number of users and the number of activities.

Each of the following n lines contains a number k_i (0 \leq k_i \leq m ) — the
number of activities that user i likes — followed by k_i distinct integers
from 1 to m — the activities user i likes.

It is guaranteed that k_1+k_2+\cdots+k_n does not exceed 10^6 .

Output

Print \texttt{YES} if a good match exists. Otherwise, print \texttt{NO} .

If a good match exists, on the next line print two integers — the indexes of
two users that make a match.

Examples

Input

    3 5
    
    3 1 2 4
    
    5 1 2 3 4 5
    
    2 1 5

Output

    YES
    3 1
    
Input

    3 3
    
    1 1
    
    1 2
    
    3 2 3 1

Output

    NO
    
Note

In the first sample, users 1 and 3 form a match, because they share activity 1
, and, furthermore, user 3 likes activity 5 (which user 1 does not like) and
user 1 likes activity 4 (which user 3 does not like). Note that users 1 and 2
, as well as users 2 and 3 , do not form a match, as there is no activity that
users 1 or 3 like, and user 2 doesn't like.
