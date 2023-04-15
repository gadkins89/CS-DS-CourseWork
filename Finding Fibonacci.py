import math
import time


def perfectSquare(x):
    ps = int(math.sqrt(x))
    return ps * ps == x


def fibCheck(n):
    return perfectSquare(5*n*n + 4) or perfectSquare(5*n*n - 4)


if __name__ == "__main__":

    n = int(input("Enter a number: \n"))

    start = time.process_time()

    fibCount = 0

    for i in range(0, n):
        
        if (fibCheck(i) == True):
            print(f"{i}: is a Fibonacci number. ")
            fibCount += 1
        else:
            pass

    end = time.process_time() - start

    print(f'{fibCount} Fibonacci numbers were found in {end} seconds. ')