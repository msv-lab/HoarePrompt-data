# Question: 4293
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
There are three airports A, B and C, and flights between each pair of airports in both directions.
A one-way flight between airports A and B takes P hours, a one-way flight between airports B and C takes Q hours, and a one-way flight between airports C and A takes R hours.
Consider a route where we start at one of the airports, fly to another airport and then fly to the other airport.
What is the minimum possible sum of the flight times?

-----Constraints-----
 - 1 \leq P,Q,R \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
P Q R

-----Output-----
Print the minimum possible sum of the flight times.

-----Sample Input-----
1 3 4

-----Sample Output-----
4

 - The sum of the flight times in the route A \rightarrow B \rightarrow C: 1 + 3 = 4 hours
 - The sum of the flight times in the route A \rightarrow C \rightarrow C: 4 + 3 = 7 hours
 - The sum of the flight times in the route B \rightarrow A \rightarrow C: 1 + 4 = 5 hours
 - The sum of the flight times in the route B \rightarrow C \rightarrow A: 3 + 4 = 7 hours
 - The sum of the flight times in the route C \rightarrow A \rightarrow B: 4 + 1 = 5 hours
 - The sum of the flight times in the route C \rightarrow B \rightarrow A: 3 + 1 = 4 hours
The minimum of these is 4 hours.
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
P, Q, R = map(int, input().split())

# Calculate the sum of flight times for each possible route
route1 = P + Q
route2 = P + R
route3 = Q + R

# Find the minimum sum of flight times among all routes
min_sum = min(route1, route2, route3)

# Print the minimum sum of flight times
print(min_sum)
#@!CODE END!@#
````

---

