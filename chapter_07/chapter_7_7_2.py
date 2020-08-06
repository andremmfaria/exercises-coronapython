# Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

number_people = input("\nHow many people are in the dinner group?\n")

if int(number_people) > 8:
    print("\nYou have to wait for a table. ")
else:
    print("\nTable ready!")