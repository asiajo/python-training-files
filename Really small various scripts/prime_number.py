"""Checks if a given number is a prime number"""


def prime(m):
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return "The number " + str(m) + " is not a prime. You can divide it for example by: " + str(i)
    return str(m) + " is a prime number."
        

def search(m, t):
    for i in range(2, int(m**0.5) + 1):
        m = m + t
        if not m % i == 0:
            return m
    return None
       

n = 677
print(prime(n))
