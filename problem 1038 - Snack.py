a, b = list(map(int, input().split()))

items = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

formula = items[a] * b

print(f"Total: R$ {formula:.2f}")
