
# user input below
fuel_type = input('')
fuel_liters = float(input())
discount_card = input('')

price = 0

if fuel_type == "Diesel":

    price = 2.33
    if discount_card == "Yes":
        price -= 0.12

elif fuel_type == 'Gas':
    price = 0.93
    if discount_card == 'Yes':
        price -= 0.08

elif fuel_type == "Gasoline":
    price = 2.22
    if discount_card == 'Yes':
        price -= 0.18

total_fuel_price = price * fuel_liters

if 20 <= fuel_liters <= 25:
    total_fuel_price *= 0.92
elif fuel_liters > 25:
    total_fuel_price *= 0.9

print(f'{total_fuel_price:.2f} lv.')