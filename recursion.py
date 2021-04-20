
def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    
    return product

# print(factorial(4))

def factoralRec(n):
    if n == 1:
        return 1
    else:
        return n * factoralRec(n - 1)

# print(factoralRec(3))

def mystery(n, m):
    if n == 0:
        return m
    else:
        return mystery(n - 1, m) + 1

# print(mystery(4, 5))

def arraySum(arr):
    length = len(arr)
    if length == 1:
        return arr[0]
    else:
        return arr[0] + arraySum(arr[1:])

# arraySum([5, 7])

def arrayReverse(arr):
    length = len(arr)
    if length == 1:
        return []
    else:
        return arrayReverse(arr[1:]) + arr[:1]

# print(arrayReverse([1, 2, 3]))

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(50))

def arrayReverseI(arr):
    revArr = []
    for i in range(len(arr) - 1, -1, -1):
        revArr.append(arr[i])

    return revArr

# print(arrayReverseI([1, 2, 3, 4]))

def efficientFib(n):
    print(go(n, 0, 1))

def go(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return go(n - 1, b, a + b)
    
# efficientFib(50)

def xx(a):
    if a < 5:
        return 3 * a
    else:
        return 2 * xx(a - 5) + 7

# print(xx(12))



# print(binarySearch([1, 2, 3, 4, 5, 66, 77, 234324, 544444444], 755))
