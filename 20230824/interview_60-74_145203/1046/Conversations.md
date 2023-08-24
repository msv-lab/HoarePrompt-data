# Question: 1046
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
Polycarpus is the director of a large corporation. There are n secretaries working for the corporation, each of them corresponds via the famous Spyke VoIP system during the day. We know that when two people call each other via Spyke, the Spyke network assigns a unique ID to this call, a positive integer session number.

One day Polycarpus wondered which secretaries are talking via the Spyke and which are not. For each secretary, he wrote out either the session number of his call or a 0 if this secretary wasn't talking via Spyke at that moment.

Help Polycarpus analyze these data and find out the number of pairs of secretaries that are talking. If Polycarpus has made a mistake in the data and the described situation could not have taken place, say so.

Note that the secretaries can correspond via Spyke not only with each other, but also with the people from other places. Also, Spyke conferences aren't permitted — that is, one call connects exactly two people.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^3) — the number of secretaries in Polycarpus's corporation. The next line contains n space-separated integers: id_1, id_2, ..., id_{n} (0 ≤ id_{i} ≤ 10^9). Number id_{i} equals the number of the call session of the i-th secretary, if the secretary is talking via Spyke, or zero otherwise.

Consider the secretaries indexed from 1 to n in some way.


-----Output-----

Print a single integer — the number of pairs of chatting secretaries, or -1 if Polycarpus's got a mistake in his records and the described situation could not have taken place.


-----Examples-----
Input
6
0 1 7 1 7 10

Output
2

Input
3
1 1 1

Output
-1

Input
1
0

Output
0



-----Note-----

In the first test sample there are two Spyke calls between secretaries: secretary 2 and secretary 4, secretary 3 and secretary 5.

In the second test sample the described situation is impossible as conferences aren't allowed.
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
ids = list(map(int, input().split()))

count = {}
for i in ids:
    if i != 0:
        count[i] = count.get(i, 0) + 1

for _, c in count.items():
    if c > 2:
        print(-1)
        exit()

pairs = 0
for _, c in count.items():
    if c == 2:
        pairs += 1

print(pairs)
#@!CODE END!@#
````

---

