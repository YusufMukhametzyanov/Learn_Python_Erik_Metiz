rivers_of_the_Earth = {'Nile': 'Egypt', 'Amazon': 'Brazil',
                       'Mississippi': 'United States of America',
                       }

for key, value in rivers_of_the_Earth.items():
    print(f'The {key} runs through {value}')

print('\n')

for river in rivers_of_the_Earth.keys():
    print(river)

print('\n')

for country in rivers_of_the_Earth.values():
    print(country)
