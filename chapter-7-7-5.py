# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

active = True
while active:
    message = input("\nPlease enter your age: \n")
    if message == 'quit':
        active = False
        
    else:
        if (int(message) < 3):
            print("\nYour ticket is free! \n")
        elif(3<=int(message)<=12):
            print("\nYour ticket is $10 \n")   
        else:
            print("\nYour ticket is $15 \n")  


