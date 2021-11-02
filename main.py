# # At home to do:
# # Install Python version 3.7+ (any version above 3.7)
# # If you already have Python version 3.7 or above, there is no need to upgrade it.
# # Install PyCharm (Community version).
# # Do a google search for PyCharm download and install the Community version (Free).
# # **** There is Thonny Python IDE also on the lab computers ****
#
# # *** Today's Lesson - Intro to functions ***
# # function - a collection or group of statements/commands with a name that performs a
# # specific task or actions.
# # e.g. print(), math.pow(), math.sqrt(), len(), etc
#
# # There are 2 types of functions
# # 1. void function. It does not return any result. Usually prints the result.
# # 2. Returning function. It returns a result.
#
# # def is the keyword to define a function.
#
# """
# def functionName():
#     command
#     command
#     ....
#
# functionName()  - calling the function
# """
#
# # void methods
# def displayMessage():
#     print("Good Morning!")
#
# displayMessage()  # calling the displayMessage function
#
# def greeting():
#     print("Hello, good morning.")
#     print("How are you doing today?")
#
# greeting()  # calling the greeting function
#
# # functions can have parameters to receive value or values
# # calling a function must then include arguments to send to the function
#
# def add23(num):    # num is the parameter
#     print(num + 23)
#
# add23(100)  # 100 is the argument
# add23(13)  # 13 is the argument

# Find the discounted price of 20%
# def discountedPrice(price):
#     dp = price * 0.8
#     #print("The discounted price is", dp)
#     print("The discounted price is $" + str(dp))
#
# discountedPrice(100)
#
# p = int(input("Enter the price: "))
# discountedPrice(p)

# def discountPrice2(price, rate):
#     dp = price * rate / 100
#     print("The discounted price is $" + str(dp))
#
# p = int(input("Enter the price: "))
# r = int(input("Enter the % discount: "))
# discountPrice2(p, r)

# Function for the area of a square
# def areaOfSq(side):
#     print("The area of the square is " + str(side * side))
#
# s = float(input("Enter the side of the square: "))
# areaOfSq(s)

# Function to find the area of a rectangle. Prompt the user for all the info you need.

def area_of_rectangle(l, w):
    area = l * w
    print("The area of the rectangle is " + str(area))
    print(f"The area of the rectangle is {area:.2f}")
    print("The area of the rectangle is %.2f" % area)

length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
area_of_rectangle(length, width)
