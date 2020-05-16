# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
# 
# • Tests for equality and inequality with strings
print("abc" == "abc")
print("abc" != "abc")
# 
# • Tests using the lower() function
print("ABC".lower() == "abc")
# 
# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print(1 == 1)
print(1 != 1)
print(1  > 1)
print(1  < 1)
print(1 >= 1)
print(1 <= 1)
# 
# • Tests using the and keyword and the or keyword
print(1 == 1 and 2 == 2)
print(1 == 1 or 2 == 2)
# 
# • Test whether an item is in a list
alist = ["a","b","c"]
print( "c" in alist )
# 
# • Test whether an item is not in a list
alist = ["a","b","c"]
print( not "c" in alist )