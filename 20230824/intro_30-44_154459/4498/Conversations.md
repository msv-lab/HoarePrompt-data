# Question: 4498
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
Three people, A, B and C, are trying to communicate using transceivers.
They are standing along a number line, and the coordinates of A, B and C are a, b and c (in meters), respectively.
Two people can directly communicate when the distance between them is at most d meters.
Determine if A and C can communicate, either directly or indirectly.
Here, A and C can indirectly communicate when A and B can directly communicate and also B and C can directly communicate.

-----Constraints-----
 - 1 ≤ a,b,c ≤ 100
 - 1 ≤ d ≤ 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
a b c d

-----Output-----
If A and C can communicate, print Yes; if they cannot, print No.

-----Sample Input-----
4 7 9 3

-----Sample Output-----
Yes

A and B can directly communicate, and also B and C can directly communicate, so we should print Yes.
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
a, b, c, d = map(int, input().split())

if abs(a-b) <= d and abs(b-c) <= d:
    print("Yes")
elif abs(a-c) <= d:
    print("Yes")
else:
    print("No")
#@!CODE END!@#
````

---

