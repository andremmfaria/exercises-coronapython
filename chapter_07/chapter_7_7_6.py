# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# 
# • Use a conditional test in the while statement to stop the loop.
# 
# • Use an active variable to control how long the loop runs.
# 
# • Use a break statement to exit the loop when the user enters a 'quit' value.



loop = 0
while True:
    loop += 1
    message = input("\nPlease enter your age: \n")
    if message == 'quit':
        print (str(loop))
        break
        
    else:
        if (int(message) < 3):
            print("\nYour ticket is free! \n")
        elif(3<=int(message)<=12):
            print("\nYour ticket is $10 \n")   
        else:
            print("\nYour ticket is $15 \n")  


