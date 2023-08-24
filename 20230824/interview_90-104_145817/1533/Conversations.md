# Question: 1533
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
Harry Potter is on a mission to destroy You-Know-Who's Horcruxes. The first Horcrux that he encountered in the Chamber of Secrets is Tom Riddle's diary. The diary was with Ginny and it forced her to open the Chamber of Secrets. Harry wants to know the different people who had ever possessed the diary to make sure they are not under its influence.

He has names of n people who possessed the diary in order. You need to tell, for each person, if he/she possessed the diary at some point before or not.

Formally, for a name s_{i} in the i-th line, output "YES" (without quotes) if there exists an index j such that s_{i} = s_{j} and j < i, otherwise, output "NO" (without quotes).


-----Input-----

First line of input contains an integer n (1 ≤ n ≤ 100) — the number of names in the list.

Next n lines each contain a string s_{i}, consisting of lowercase English letters. The length of each string is between 1 and 100.


-----Output-----

Output n lines each containing either "YES" or "NO" (without quotes), depending on whether this string was already present in the stream or not.

You can print each letter in any case (upper or lower).


-----Examples-----
Input
6
tom
lucius
ginny
harry
ginny
harry

Output
NO
NO
NO
NO
YES
YES

Input
3
a
a
a

Output
NO
YES
YES



-----Note-----

In test case 1, for i = 5 there exists j = 3 such that s_{i} = s_{j} and j < i, which means that answer for i = 5 is "YES".
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
n = int(input())
names = []
for _ in range(n):
    name = input().lower()
    if name in names:
        print("YES")
    else:
        print("NO")
        names.append(name)
#@!CODE END!@#
````

---

