holidays = int(input())
year = 365
norm = 30000
working_days = year - holidays

playing_time = working_days * 63 + holidays * 127
overplay_h = abs(playing_time - norm)//60
overplay_m = abs(playing_time - norm) % 60

if playing_time > norm:
    print('Tom will run away')
    print(f'{overplay_h} hours and {overplay_m} minutes more for play')
else:
    print("Tom sleeps well")
    print(f'{overplay_h} hours and {overplay_m} minutes less for play')

