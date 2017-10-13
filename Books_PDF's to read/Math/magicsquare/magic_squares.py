# magic_squares.py
# Knuth TAOCP, vol. 1.3.2 ex.21

from math import *

def getN():
    while 1:
        try:
            n = int(input("n: "))
            if n % 2 == 1 and n != 1:
                return n
            else:
                raise ValueError
        except ValueError:
            print("Oops")

def makeString(array, n, nSq):
    string = "\nMagic Square"
    string += "\nn={0}, m={1}\n".format(n, int(n * (nSq + 1) / 2))
    padding = ceil(log(nSq, 10))
    for i, cell in enumerate(array):
        if i % n == 0:
            string += '\n'
        else:
            string += ' '
        string += str(array[i]).zfill(padding)
    return string

def main():
    print("*** Magic Squares ***\nPlease enter an odd number greater than one.")
    n = getN()
    normal, nSq = n + 1, n * n,
    array, i = [0] * nSq, int(nSq/2) - 1
    for j in range(1, nSq + 1):
        if (i+1) % n == 0:
            i2 = (i + 1) % nSq
        else:
            i2 = (i + normal) % nSq
        if array[i2] != 0:
            i2 = (i  + n * 2) % nSq
        array[i2] = j
        i = i2        
    print(makeString(array, n, nSq))

if __name__ == "__main__":
    main()
