# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# 
# "Santiago, Chile"
# 
# Call your function with at least three city-country pairs, and print the value that’s returned.

def city_country(city, country):
    print(city + ", " + country)

city_country("Rio de Janeiro","Brazil")
city_country("Toronto","Canada")
city_country("New York","United States of America")