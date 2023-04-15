import matplotlib.pyplot as plt
import math
from math import isqrt
import time


def find_primes (n: int):
    if n <= 2:
        return []
    prime_num = [True] * n
    prime_num[0] = False
    prime_num[1] = False

    for i in range(2, isqrt(n)+1):
        if prime_num[i]:
            for x in range(i*i, n, i):
                prime_num[x] = False
    return [i for i in range(n) if prime_num[i]]


#def perfectSquare(x):
    #ps = int(math.sqrt(x))
    #return ps * ps == x


#def fibCheck(n):
    #return perfectSquare(5*n*n + 4) or perfectSquare(5*n*n - 4)



if __name__ == "__main__":

    y = int(input("Enter a number: \n"))

    start = time.process_time()

    find_primes(y)
 
    end = time.process_time() - start
    

    plt.plot(find_primes(y))
    plt.title(f"Sieve of Eratosthenes Curve -- Solved In: {end:.8f} seconds. ")
    plt.xlabel("Number of Primes ")
    plt.ylabel(f"Given Number: {y} ")
    plt.show()