# Question: 2585
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
Let's consider all integers in the range from $1$ to $n$ (inclusive).

Among all pairs of distinct integers in this range, find the maximum possible greatest common divisor of integers in pair. Formally, find the maximum value of $\mathrm{gcd}(a, b)$, where $1 \leq a < b \leq n$.

The greatest common divisor, $\mathrm{gcd}(a, b)$, of two positive integers $a$ and $b$ is the biggest integer that is a divisor of both $a$ and $b$.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 100$)  — the number of test cases. The description of the test cases follows.

The only line of each test case contains a single integer $n$ ($2 \leq n \leq 10^6$).


-----Output-----

For each test case, output the maximum value of $\mathrm{gcd}(a, b)$ among all $1 \leq a < b \leq n$.


-----Example-----
Input
2
3
5

Output
1
2



-----Note-----

In the first test case, $\mathrm{gcd}(1, 2) = \mathrm{gcd}(2, 3) = \mathrm{gcd}(1, 3) = 1$.

In the second test case, $2$ is the maximum possible value, corresponding to $\mathrm{gcd}(2, 4)$.
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
t = int(input())

for _ in range(t):
    n = int(input())
    max_gcd = n // 2
    print(max_gcd)
#@!CODE END!@#
````

---

