
# Task: Implementation of Miller-Rabin primality test.

# More info: https://en.wikipedia.org/wiki/Miller-Rabin_primality_test

# This program takes any integer n as an input and determines if that number is likely to be prime and does that in polynomial-time.
# There is also optional to input k which is determines the accuracy of the result. Default value for k is 5.


import random

# Function returns True if the n is probably a prime and False if it is definetly not a prime.

def miller_rabin_algo(d,n):

    # We pick random integer for the "a" such that 1 < a < n-1
    a = random.randrange(2,n-1)

    # We use helping variable x which we find by taking a to the power of d mod n.
    x = pow(a,d,n)

    # We check if x value is either 1 or n-1. If it is then the n is likely prime and we exit the function.
    if x == 1 or x == n-1:
        return True

    # We run while loop until d value is n-1. If by then x has still not satisfied the conditions then we know that n is not prime.
    # Every iteration we double the d and square the x.
    while d != n-1:
    
        x = x * x % n
        d *= 2

        if x == 1:
            return False
        if x == n-1:
            return True

    return False



def is_likely_prime(n,k=5):

    if n == 1 or n == 2 or n == 3:      # Only run the algorithm with n > 3
        return True 

    if n % 2 == 0:                      # Check if number is even. If it is, it can't be prime.
        return False        

    s = 0
    d = n-1

    # This while loop finds the s and d values for the n. Final result should look like this: n-1 == 2^s * d
    # We do it by dividing d with 2 until d is even number while incrementing s every iteration.
    while d % 2 == 0:                   
        s += 1
        d //= 2

    # This for loop will run the actual algorithm k times. Larger k means more accurate since the "a" value is random every time and if we
    # randomly pick "a" value that is a strong liar for our n, then the algorithm will return false positive.
    # If during any iteration of the algorithm we get the result False then we can be sure that the n is not prime.
    # If we go through many iterations of the algorithm and always end up with True, then it is highly likely that n is prime.
    for i in range(k):

        if miller_rabin_algo(d,n) == False:
            return False

    return True

# print(is_likely_prime(97,5))
