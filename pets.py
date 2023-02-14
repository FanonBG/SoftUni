import math
number_of_days = int(input())
total_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

food_needed = dog_food_per_day * number_of_days \
              + cat_food_per_day * number_of_days \
              + turtle_food_per_day * number_of_days

food_diff = abs(total_food - food_needed)

if food_needed <= total_food:
    print(f"{math.floor(food_diff)} kilos of food left.")
else:
    print(f'{math.ceil(food_diff)} more kilos of food are needed.')



