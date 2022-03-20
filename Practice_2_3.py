ss = int(input("Enter time in seconds = "))
lst = []
ss = (ss / 3600)
h = int(ss)
t = (ss - h) * 60
m = int(t)
s = int(round(((t - m) * 60)))

print('{:d}:{:02d}:{:02d}'.format(h, m, s))
