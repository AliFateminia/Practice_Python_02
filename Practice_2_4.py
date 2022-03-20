n = int(input("Enter the number of students :"))
num = []
count = 0
for i in range(n):
    print("Enter the ", i+1, " student grade :")
    num.append(float(input()))
    count += 1
    if count == n:
        average = round(sum(num) / len(num), 2)
        print("maximum grade: ", max(num))
        print("minimum grade: ", min(num))
        print("Students' grade point average: ", average)
