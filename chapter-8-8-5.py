# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city_name, country = 'Brazil'):
    print(city_name + " is in " + country + ".\n")

describe_city(city_name='Rio de janeiro')
describe_city(city_name= 'Minneapolis', country='the US')
describe_city(city_name='Sao Paulo')

