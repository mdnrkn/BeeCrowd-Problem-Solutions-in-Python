import math

p1 = input().split()
p2 = input().split()

x1 = float(p1[0])
x2 = float(p2[0])
y1 = float(p1[1])
y2 = float(p2[1])

a = pow((x2 - x1), 2) + pow((y2 - y1), 2)

formula = math.sqrt(a)

print(f"{formula:.4f}")
