
import sys
import math


def fibo(n):

    value1 = 0
    value2 = 1
    sumOfValues = 1
    
    for i in range(n):
        sumOfValues = value1 + value2
        value1 = value2
        value2 = sumOfValues

    return sumOfValues
###the function above calculates and return the fibonacci sequence value for every 'n' input number###


### the main function prints the number and the fibo value side to side ###

def main():
    for i in range(1, int(sys.argv[1]) + 1):
        print(str(i) + " " + str(fibo(i - 1)))

main()
