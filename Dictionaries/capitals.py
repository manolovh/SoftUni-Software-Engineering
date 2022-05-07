country_names = input().split(', ')
capital_cities = input().split(', ')

capitals_and_countries = tuple(zip(country_names, capital_cities))
dict_countries = {key: value for key, value in capitals_and_countries}

for key, value in dict_countries.items():
    print(f"{key} -> {value}")