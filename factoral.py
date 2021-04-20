
def factoral(n):
    if n == 1:
        return 1
    else:
        return n * factoral(n - 1)

def bigO(n):
    sum = 0
    print(sum)
    for j in range(1, n):
        print("j index: " + str(j))
        for k in range(1, j):
            print("k index: " + str(k))
            sum = sum + 1
            print(sum)

# bigO(10)

def loop(n):
    # If n < i then execute.
    for i in range(1, n):
        print("I: " + str(i))

# loop(1)
# loop(1, 9)

def add(n):
    sum = 0
    for i in range(1, n + 1):
        print(sum)
        sum = sum + i
    print(sum)

# add(10)

def nestedLoop(n):
    i = 0
    while(i < n):
        j = n
        while(j > i):
            print(j)
            j = j - 1

        i = i + 1

nestedLoop(10)