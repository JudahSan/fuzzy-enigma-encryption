import math
def factors(number):
    return [(x, number / x)  
    for x in range(int(math.sqrt(number)))[2:] if not number % x]

print(factors(128))
print(factors(299))

import math

def factorials(num):
    return [(x, num / x) for x in range(1, int(math.sqrt(num)) + 1) if num % x == 0]
    
print(factorials(128))