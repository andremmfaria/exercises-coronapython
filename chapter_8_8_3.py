# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(tshirt_size, text_on_tshirt):
        print("The size of the t-shirt is " + tshirt_size + "\n - "   + text_on_tshirt + " -  will be printed on it. ")

size = input(" Enter the your t shirt size")
text = input("Type the text you want to print on your t-shirt")

make_shirt(size, text)

