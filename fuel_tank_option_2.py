fuel = input("")
litters = float(input())

allowed_fuels = {'Gas', 'Diesel', 'Gasoline'}
if fuel not in allowed_fuels:
    print(f'Invalid fuel: {fuel}')
else:

    if litters >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
