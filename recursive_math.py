
#recursive factorial
def recFactorial(n):
    if n == 1:
        return 1

    else:
        return n * recFactorial(n-1)

#recursive fibonacci 
def fibo(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

#recursive sum of ints/floats in list 
def listSum(alist):
    if len(alist) == 1:
        return alist[0]

    else:
        return alist[0] + listSum(alist[1:])

#recursive check if string is palindrome 
def isPalindrome(astring):
    if len(astring) == 1 or len(astring) == 2:
        return astring[0] == astring[-1]

    else:
        return astring[0] == astring[-1] and isPalindrome(astring[1:-1])

#recursive GCD of two ints 
def gcdEuclid(a, b):
    if a == 0 and b == 0:
        print('Not defined')
        return None
    elif a == 0:
        return b
    
    return gcdEuclid(b%a, a)



