value = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

notes_count = [0]*len(notes)
coins_count = [0]*len(coins)

cents = int(value * 100)

for i in range(len(notes)):
    notes_count[i] = cents // (notes[i] * 100)
    cents -= notes_count[i] * notes[i] * 100

for i in range(len(coins)):
    coins_count[i] = cents // int(coins[i] * 100)
    cents -= coins_count[i] * int(coins[i] * 100)

print("NOTAS:")
for i in range(len(notes)):
    print("{} nota(s) de R$ {:.2f}".format(notes_count[i], notes[i]))

print("MOEDAS:")
for i in range(len(coins)):
    print("{} moeda(s) de R$ {:.2f}".format(coins_count[i], coins[i]))
