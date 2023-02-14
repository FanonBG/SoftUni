fuel = input("")
litters = float(input())

if fuel != "Diesel" and fuel != "Gasoline" and  fuel != "Gas":
    print("Invalid fuel!")
else:

    if litters >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")

