
# Task: "Program that calculates order of the element in a group of integers modulo p".

# Order of the element X is the smallest positive integer n such that X^n = e where e is the identity element of the group. Since this program works only for the multiplicative groups, we know that e = 1 and therefore need to find the power of X that equals 1 in the modulo p.


# Define a function which takes 2 inputs - "element" is that specific element we want to fint he order of and "p" is modulo value.

def order_of_element(p, element):

    power = 1           # Power which we start our loop and increase every iteration.
    mod = element % p   # Variable to hold modulo value we got from the last iteration of the loop.
    e = 1               # Expected identity element when we end the loop.
        
    # I use while loop since the number of iterations is unknown and depends on the inputs. Loop stops when the mod value from the last iteration was 1.
    while mod != e:     

        # Every iteration we multiply the mod value from last iteration with element and take new mod value modulo p. We could also take element into power directly, but that would be slower implementation.
        mod = (element * mod) % p   
        power += 1  # We increment the power to keep track of it since that will be our answer once we find mod 1.

    order = power       # We found the correct power and we now save it as new variable because it represents the order of our element.
    
    return order        # Function returns the order of element modulo p.



print(order_of_element(64,5))