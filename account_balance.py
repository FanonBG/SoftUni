newnum = input()
balance = 0.0
while newnum != "NoMoreMoney":
    amount = float(newnum)
    if amount < 0:
        print("Invalid operation!")
        break
    balance += amount
    print(f"Increase: {amount:.2f}")
    newnum = input()

print(f"Total: {balance:.2f}")
