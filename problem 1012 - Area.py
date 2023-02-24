a = (input()).split(" ")
pi = 3.14159

triangle = (1 / 2 * float(a[0]) * float(a[2]))
circle = (pi * pow(float(a[2]), 2))
trapezium = ((float(a[0]) + float(a[1])) / 2) * float(a[2])
square = pow(float(a[1]), 2)
rectangle = float(a[0]) * float(a[1])

print(f"TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\nTRAPEZIO: {trapezium:.3f}\nQUADRADO: {square:.3f}\nRETANGULO: {rectangle:.3f}")
