# Question: 2516
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
Takahashi has a string S of length N consisting of digits from 0 through 9.
He loves the prime number P. He wants to know how many non-empty (contiguous) substrings of S - there are N \times (N + 1) / 2 of them - are divisible by P when regarded as integers written in base ten.
Here substrings starting with a 0 also count, and substrings originated from different positions in S are distinguished, even if they are equal as strings or integers.
Compute this count to help Takahashi.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - S consists of digits.
 - |S| = N
 - 2 \leq P \leq 10000
 - P is a prime number.

-----Input-----
Input is given from Standard Input in the following format:
N P
S

-----Output-----
Print the number of non-empty (contiguous) substrings of S that are divisible by P when regarded as an integer written in base ten.

-----Sample Input-----
4 3
3543

-----Sample Output-----
6

Here S = 3543. There are ten non-empty (contiguous) substrings of S:
 - 3: divisible by 3.
 - 35: not divisible by 3.
 - 354: divisible by 3.
 - 3543: divisible by 3.
 - 5: not divisible by 3.
 - 54: divisible by 3.
 - 543: divisible by 3.
 - 4: not divisible by 3.
 - 43: not divisible by 3.
 - 3: divisible by 3.
Six of these are divisible by 3, so print 6.
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
import itertools

N, P = map(int, input().split())
S = input()

count = 0
prefix_sum = 0
digits_mod = [0] * P

for i in range(N-1, -1, -1):
    prefix_sum = (prefix_sum + int(S[i]) * pow(10, N-i-1, P)) % P
    count += digits_mod[prefix_sum]
    digits_mod[prefix_sum] += 1

count += digits_mod[0]

print(count)
#@!CODE END!@#
````

---

