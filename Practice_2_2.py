time = input("enter time this format **:**:** = ")
ss = 0
for i in range(2):
    f = time.find(":")
    if i == 0:
        ss = (int(time[0: f])) * 3600
    if i == 1:
        ss = ss + ((int(time[0: f])) * 60)
    f += 1
    time = time[f:]
    if i == 2:
        ss = ss + (int(time))
print(ss)
