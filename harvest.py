import math

vineyard_area = int(input())
grape_per_sqm = float(input())
needed_wine = int(input())
workers = int(input())
grape_production = vineyard_area * grape_per_sqm

wine_production = (grape_production / 2.5) * 0.4
wine_diff = abs(wine_production - needed_wine)

if wine_production >= needed_wine:
    print(f'Good harvest this year! Total wine: {int(wine_production)} liters.')
    print(f"{math.ceil(wine_diff)} liters left -> {math.ceil(wine_diff / workers)} liters per person.")
else:
    print(f'It will be a tough winter! More {math.floor(wine_diff)} liters wine needed.')
