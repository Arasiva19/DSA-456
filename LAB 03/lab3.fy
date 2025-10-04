def function1(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        return value * function1(value, number-1)

Analysis:
Step 1 – Problem size: n = number
Step 2 – Operations per call: 1 multiplication + 1 recursive call → O(1)
Step 3 – Recurrence:
     T(n) = T(n/2) + O(1)
step4: Solve the problem
       Expanding:T(n)=T(n−1)+1=T(n−2)+2=⋯=T(0)+n
Step 5 – Complexity: Linear time                        


def recursive_function2(mystring,a, b):
    if(a >= b ):
        return True
    else:
        if(mystring[a] != mystring[b]):
            return False
        else:
            return recursive_function2(mystring,a+1,b-1)


def function2(mystring):
    return recursive_function2(mystring, 0,len(mystring)-1)

Step 1 – Problem size: n = len(mystring)
Step 2 – Operations per call: a few constant comparisons + recursion on (a+1, b-1) → reduces size by 2
step 3 – Recurrence:T(n) = T(n-2) + O(1)
Solution: about n/2 calls → O(n)
Complexity: Linear time.


def function3(value, number):
    if number == 0:
        return 1
    elif number == 1:
        return value
    else:
        half = number // 2
        result = function3(value, half)
        if (number % 2 == 0):
            return result * result
        else:
            return value * result * result

Problem size: number
Operations per call: 1 recursive call on roughly n/2
Recurrence: T(n) = T(n/2) + O(1)
Solution: T(n) = O(log n)
Complexity: Logarithmic time.

How to approach writing recursive functions?
Identify the problem’s base case (smallest input with direct answer).
Define how the problem reduces to a smaller instance.
Ensure each recursive call progresses toward the base case.
Test with small inputs first.

How to analyze recursive functions?
Similar to iterative: count operations.
But with recursion, you must write a recurrence relation (time depends on smaller subproblems).
Recursive analysis differs because:
You must consider repeated sub-calls.
Complexity depends on how problem size shrinks each time (e.g., n-1, n/2).
It’s the same as non-recursive analysis in that both ultimately measure growth of operations as input grows.
