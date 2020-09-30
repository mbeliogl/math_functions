

### imports the math module ###
import sys 
import math



### the function approximates and returns the value of sqrt(2) for each n value ###
def squareRoot(n):

    acc = 2
    for i in range(n):
        acc = 2 + 1 / acc
    acc = acc - 1
    return acc


### calculates and prints the diff(difference) between the value of squareRoot(n) and math.sqrt(2) ###
### the loop allows for the calculation of all values from 1 to user_num ###
def main():
	user_num = int(sys.argv[1])

	if user_num == 1:
		sqareRoot = str(squareRoot(1))
		diff = str(math.sqrt(2) - squareRoot(1))
		print(str(squareRoot(1)) + " " + str(math.sqrt(2) - squareRoot(1)))

	else:	
		for i in range(1, user_num+1):
			sqareRoot = str(squareRoot(i))
			diff = str(math.sqrt(2) - squareRoot(i))
			print(str(squareRoot(i)) + " " + str(math.sqrt(2) - squareRoot(i)))




main()




