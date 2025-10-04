def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower() # lowercases the inputs

    if (player == "rock") and (opponent == "scissors"):
        return 1
    elif (player == "paper") and (opponent == "rock"):
        return 1
    elif (player == "scissors") and (opponent == "paper"): # choices
        return 1
    else:
        return 0

def factorial(n):
	if n == 0:
		return 1 
	result = 1
	for i in range(1, n + 1):
			result *= i  #multiplies the result from the range of numbers
	return result
	return 0


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    firstNum = 0
    secondNum = 1
    for i in range(2, n + 1):
        next = firstNum + secondNum
        firstNum = secondNum
        secondNum = next

    return secondNum


#[2,4,5,2] 

def sum_to_goal(numbers, goal):
    for i in range(len(numbers)): #circles the first number through the list
        for j in range(i + 1, len(numbers)): 
            if numbers[i] + numbers[j] == goal: # checks if both numbers sums up goal
                return numbers[i] * numbers[j]
    return 0


class UpCounter():
    def __init__(self, step_size=1):
        self.value = 0      
        self.step_size = step_size      #initializing the step size

    def count(self):
        return self.value      

    def update(self):
        self.value = self.value + self.step_size  

class DownCounter(UpCounter):
    def update(self):
        self.value = self.value - self.step_size
