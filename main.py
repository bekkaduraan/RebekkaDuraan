import sys, numpy as ny

# Function to determine index of first term in Fibonacci sequence to contain N digits
def indexOfDigits(N):
    prevFib, fib = 0, 1
    compare = ny.power(10, (N-1))
    index = 1
    while(fib < compare):
        fib, prevFib = ny.sum([fib, prevFib]), fib
        index = ny.sum([1, index])
    return index

# If the number entered is below 20, calculate index
try:
    N = int(sys.argv[1])
    if N < 20:   # Numpy uses int64 data type which limits the calculations
        print(indexOfDigits(N))
    else:
        print("This number goes beyond the boundaries of this program.")

# If the value entered is not a number, print message
except ValueError:
    print('This is not a number!')