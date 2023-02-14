kilometers = int(input())
day_time = input('')

day_taxi_price = kilometers * 0.79 + 0.70
night_taxi_price = kilometers * 0.9 + 0.7

bus_price = kilometers * 0.09  # can be used > 20 km only

train_price = kilometers * 0.06  # can be used > 100 km only

if kilometers < 20 and day_time == 'day':
    print(f"{day_taxi_price:.2f}")
elif kilometers < 20 and day_time == 'night':
    print(f"{night_taxi_price:.2f}")
elif 20 <= kilometers < 100:
    print(f'{bus_price:.2f}')
else:
    print(f"{train_price:.2f}")



