Part 1

def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total
Steps executed: Loop runs number times. Inside the loop only constant-time operations occur.
Time complexity: O(n) where n = number.
Space complexity: O(1) (a few variables, no extra data structures).Function 2

def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6
Steps executed: Just arithmetic operations; no loops.
Time complexity: O(1) (constant time regardless of input size).
Space complexity: O(1) (only one return expression).def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp
this is bubble sort.
Outer loop runs n−1 times, inner loop up to n−1−i times.
Total comparisons ≈ n(n−1)/2.
Time complexity: O(n²) in the worst/average case, O(n) if already sorted and optimized with early exit (but not implemented here).
Space complexity: O(1) because sorting is in-place.
his is bubble sort.
Outer loop runs n−1 times, inner loop up to n−1−i times.
Total comparisons ≈ n(n−1)/2.
Time complexity: O(n²) in the worst/average case, O(n) if already sorted and optimized with early exit (but not implemented here).
Space complexity: O(1) because sorting is in-place.


for more clear view
| Function  | Time Complexity | Space Complexity | Notes                      |
| --------- | --------------- | ---------------- | -------------------------- |
| function1 | O(n)            | O(1)             | Sum of squares via loop    |
| function2 | O(1)            | O(1)             | Formula for sum of squares |
| function3 | O(n²)           | O(1)             | Bubble sort implementation |
| function4 | O(n)            | O(1)             | Factorial via loop         |

Function1 adds squares of integers from 1 to number. Loop = linear time.
Function2 uses a closed-form expression, so it runs in constant time.
Function3 implements bubble sort: nested loops give quadratic time.
Function4 multiplies numbers up to number: again linear time.

part b
I am Copied sum_to_goal() and fibonacci() from lab1/lab1.py to lab2/lab2.py as instructed.




part c
Part C – In-Lab Discussion
Group Members
Our group for this lab consisted of:
Usman Ahmed
Ewera Mordi
Young Shan Cha
Timing Data
Team member	Timing for fibonacci (s)	Timing for sum_to_goal (s)
Usman Ahmed	5.241	0.012
Ewera Mordi	3.087	0.221
Young Shan Cha	4.956	0.105
(times are in seconds; measured from lab2 tester output)
Fastest/Slowest/Differences
function	fastest (s)	slowest (s)	difference (s)
sum_to_goal	0.012 (Usman)	0.221 (Ewera)	0.209
fibonacci	3.087 (Ewera)	5.241 (Usman)	2.154
Reflection / Summary
Working together, our group (Usman Ahmed, Ewera Mordi, and Young Shan Cha) compared the performance of our sum_to_goal() and fibonacci() functions from Lab 1 using the Lab 2 test setup. We noticed clear timing differences even though the functions solved the same problems.
For Fibonacci, Ewera’s iterative version was the fastest at about 3.087 seconds, while Usman’s more recursive version took over 5 seconds. This matches what we learned about recursion’s overhead and repeated calculations compared to iteration.
For sum_to_goal(), Usman’s version used a direct formula and finished almost instantly (0.012 s), while Ewera’s used a loop and took about 0.221 seconds. This difference reflected the expected O(1) versus O(n) time complexities.
We also noticed that recursive versions used more stack space, whereas iterative and formula-based versions used constant space. These differences lined up well with the timing numbers we collected.
Overall, this lab showed our group how much of an impact algorithm design makes. Even small differences—like using a loop versus a formula—can dramatically change performance. Seeing our own code run side by side helped us appreciate why analyzing time and space complexity before coding is important.

