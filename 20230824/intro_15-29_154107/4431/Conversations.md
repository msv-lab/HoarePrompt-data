# Question: 4431
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
Recently, Norge found a string $s = s_1 s_2 \ldots s_n$ consisting of $n$ lowercase Latin letters. As an exercise to improve his typing speed, he decided to type all substrings of the string $s$. Yes, all $\frac{n (n + 1)}{2}$ of them!

A substring of $s$ is a non-empty string $x = s[a \ldots b] = s_{a} s_{a + 1} \ldots s_{b}$ ($1 \leq a \leq b \leq n$). For example, "auto" and "ton" are substrings of "automaton".

Shortly after the start of the exercise, Norge realized that his keyboard was broken, namely, he could use only $k$ Latin letters $c_1, c_2, \ldots, c_k$ out of $26$.

After that, Norge became interested in how many substrings of the string $s$ he could still type using his broken keyboard. Help him to find this number.


-----Input-----

The first line contains two space-separated integers $n$ and $k$ ($1 \leq n \leq 2 \cdot 10^5$, $1 \leq k \leq 26$) — the length of the string $s$ and the number of Latin letters still available on the keyboard.

The second line contains the string $s$ consisting of exactly $n$ lowercase Latin letters.

The third line contains $k$ space-separated distinct lowercase Latin letters $c_1, c_2, \ldots, c_k$ — the letters still available on the keyboard.


-----Output-----

Print a single number — the number of substrings of $s$ that can be typed using only available letters $c_1, c_2, \ldots, c_k$.


-----Examples-----
Input
7 2
abacaba
a b

Output
12

Input
10 3
sadfaasdda
f a d

Output
21

Input
7 1
aaaaaaa
b

Output
0



-----Note-----

In the first example Norge can print substrings $s[1\ldots2]$, $s[2\ldots3]$, $s[1\ldots3]$, $s[1\ldots1]$, $s[2\ldots2]$, $s[3\ldots3]$, $s[5\ldots6]$, $s[6\ldots7]$, $s[5\ldots7]$, $s[5\ldots5]$, $s[6\ldots6]$, $s[7\ldots7]$.
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
n, k = map(int, input().split())
s = input()
available_letters = input().split()

count = 0

for i in range(n):
    if s[i] not in available_letters:
        continue
    count += 1
    for j in range(i+1, n):
        if s[j] not in available_letters:
            break
        count += 1

print(count)
#@!CODE END!@#
````

---

