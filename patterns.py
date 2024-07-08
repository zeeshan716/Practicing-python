print ("pattern 1: ")
for n in range (5):
    for i in range (5):
        print("*", end="")
    print()

print ("pattern 2: ")
for n in range (1, 6):
    for i in range (n):
        print("*", end="")
    print() 

print ("pattern 3: ")
for n in range (1, 6):
    for i in range (1, n + 1):
        print(i, end="")
    print() 

print ("pattern 4: ")
for n in range (1, 6):
    for i in range (n):
        print(n, end="")
    print() 

print ("pattern 5: ")
for n in range (5, -1, -1):
    for i in range (n):
        print("*", end="")
    print() 

print ("pattern 6: ")
for n in range (5, -1, -1):
    for i in range (1, n + 1):
        print(i, end="")
    print()

n = 5
print ("pattern 7: ")
for i in range (n):
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    #stars
    for j in range (2*i+1):
        print ("*", end = "")
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    print()
print()

print ("pattern 8: ")
for i in range (n):
    #space
    for j in range (i):
        print (" ", end = "")
    #stars
    for j in range (2*n - (2*i+1)):
        print ("*", end = "")
    #space
    for j in range (i):
        print (" ", end = "")
    print()
print()

print ("pattern 9: ")
for i in range (n):
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    #stars
    for j in range (2*i+1):
        print ("*", end = "")
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    print()
for i in range (n):
    #space
    for j in range (i):
        print (" ", end = "")
    #stars
    for j in range (2*n - (2*i+1)):
        print ("*", end = "")
    #space
    for j in range (i):
        print (" ", end = "")
    print()
print()

print ("pattern 10: ")
for i in range (1, 5):
    for j in range (i):
        print("*", end="")
    print()
for i in range (5, -1, -1):
    for j in range (i):
        print("*", end="")
    print() 

print ("pattern 11: ")
for i in range(1, n+1):
    pattern = ''
    for j in range(i):
        pattern += str((i + j) % 2)
    print(pattern)
print()

n = 4
print ("pattern 12: ")
for i in range (1, n + 1):
    #numbers
    for j in range (1, i + 1):
        print(j, end="")
    #spaces
    for j in range ((n - i)*2):
        print(" ", end="")
    #numbers
    for j in range (i, 0, -1):
        print(j, end="")
    print()
print()

n = 5
num = 1
print ("pattern 13: ")
for i in range (1, n + 1):
    for j in range (i):
        print (num, end = ' ')
        num += 1
    print()
print()

print ("pattern 14: ")
for i in range (n):
    for j in range (ord('A'), ord('A') + i + 1):
        print (chr(j), end = ' ')
    print()
print()

print ("pattern 15: ")
for i in range (n, 0, -1):
    for j in range (ord('A'), ord('A') + i):
        print (chr(j), end = ' ')
    print()
print()

print ("pattern 16: ")
for i in range (n):
    for j in range (i + 1):
        print (chr(ord('A') + i), end = ' ')
    print()
print()

n = 4
print ("pattern 17: ")
for i in range (n):
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    #alphabets
    char = 'A'
    breakpoint = (2*i+1)//2
    for j in range (2*i+1):
        print (char, end = '')
        if j < breakpoint:
            char = chr(ord(char) + 1)
        else:
            char = chr(ord(char) - 1)
    #space
    for j in range (n-i-1):
        print (" ", end = "")
    print()
print()

n = 5
print ("pattern 18: ")
for i in range (n):
    for j in range (ord('E') - i, ord('E') + 1):
        print (chr(j), end = ' ')
    print()
print()

print ("pattern 19: ")
n = 5
for i in range (n):
    #stars
    for j in range (n-i):
        print ("*", end = "")
    #spaces
    for j in range (i + 1):
        if j == 0:
            continue
        else:
            print ("  ", end = "")
    #stars
    for j in range (n-i):
        print ("*", end = "")
    print()
for i in range (n):
    #stars
    for j in range (i + 1):
        print ("*", end = "")
    #spaces
    for j in range (n-(i + 1)):
        if j == 4:
            continue
        else:
            print ("  ", end = "")
    #stars
    for j in range (i + 1):
        print ("*", end = "")
    print()
print()

print ("pattern 20: ")
for i in range (n - 1):
    #stars
    for j in range (i + 1):
        print ("*", end = "")
    #spaces
    for j in range (n-(i + 1)):
        if j == 4:
            continue
        else:
            print ("  ", end = "")
    #stars
    for j in range (i + 1):
        print ("*", end = "")
    print()
for i in range (n):
    #stars
    for j in range (n-i):
        print ("*", end = "")
    #spaces
    for j in range (i + 1):
        if j == 0:
            continue
        else:
            print ("  ", end = "")
    #stars
    for j in range (n-i):
        print ("*", end = "")
    print()
print()

print ("pattern 21: ")
n = 4
for i in range (n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print ("*", end = " ")
        else:
            print (" ", end = " ")
    print()
print()

print ("pattern 22: ")
n = 7
for i in range (n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print ("4", end = " ")
        elif i == 1 or j == 1 or i == n-2 or j == n-2:
            print ("3", end = " ")
        elif i == 2 or j == 2 or i == n-3 or j == n-3:
            print ("2", end = " ")
        else:
            print ("1", end = " ")
    print()
print()