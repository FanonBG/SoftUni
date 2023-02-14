import math
magnolia = 3.25
hyacinth = 4  # zyumbyul
rose = 3.50
cactus = 8

# taxes = 5%

# user input area below
magnolia_quantity = int(input())
hyacinth_quantity = int(input())
rose_quantity = int(input())
cactus_quantity = int(input())
present_price = float(input())

total_income = magnolia_quantity * magnolia \
               + hyacinth_quantity * hyacinth \
               + rose_quantity * rose \
               + cactus_quantity * cactus

final_income = total_income - (total_income * 0.05)
diff = abs(present_price - final_income)

if final_income >=present_price:
    print(f"She is left with {(math.floor(diff))} leva.")
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')

