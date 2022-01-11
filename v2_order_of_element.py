import random
from miller_rabin import is_likely_prime as isprime
from phi import phi


# Another implementation to find the order of the element. My testing shows that it is actually slower than the first.
# This first finds the order of the group by using Euler's function which tells us how many numbers there are that are
# smaller than p and also coprime to p. This value is the group order.

def v2_order_of_element(p, element):

    order_of_group = 0

    if isprime(p) == True: # If the p is prime then the |G|==p-1 

        order_of_group = p-1
    
    else:

        order_of_group = phi(p)

    
    # I think this loop is the slow part of the algorithm. To find the divisors of the group order (potential element orders)
    # I iterate through all number smaller than p and see if they divide group order.
    for i in range(1,p):   
        if order_of_group % i == 0:
            if (element ** i) % p == 1:
                return i

    return "Could not find order for this element."


# print(v2_order_of_element(90000006,5))

 

