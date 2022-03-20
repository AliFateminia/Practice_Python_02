n = int(input("Enter number: "))
d = j = 1
w = v = True
for i in range(n):
    if v:
        print(d, j, end=" ")
        v = False
    if w:
        d = j + d
        w = False
        print(d, end=" ")
    if w != 1:
        j = j + d
        w = True
        print(j, end=" ")

