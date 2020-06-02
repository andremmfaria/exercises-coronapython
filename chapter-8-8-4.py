# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt( text_on_tshirt = 'I love Python', tshirt_size = 'Large'):
        print("The size of the t-shirt is " + tshirt_size + "\n - "   + text_on_tshirt + " -  will be printed on it. ")


make_shirt()
make_shirt(tshirt_size= 'medium')
make_shirt('Sounds great!', 'small')
