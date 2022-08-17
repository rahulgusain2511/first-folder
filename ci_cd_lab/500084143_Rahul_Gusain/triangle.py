# Program to find which type of triangle is given to us
# These are the three variables for taking input of sides 
x = int(input("Enter the side:"))
y = int(input("Enter the side:"))
z = int(input("Enter the side:"))
# These are all the posible condtions
# 1st condition is to check that given sides are positive and not zero  
if (x <= 0 or y <= 0 or z <= 0):
    print("Sides can only be greater than zero and not negative ")
# 2nd condition is to check for valid input 
elif (x+y < z or y+z < x or x+z < y):
    print("Invalid input, Triangle cannot be formed.")
# 3rd condition is to check for equilateral traingle .
elif (x==z & y==z & x==z):
    print("Given triangle is a Equilateral triangle with all equal sides.")
# 4th condition is to check for scalene triangle.
elif (x!=y & y!=z & x!=z):
    print("Given triangle is a Scalene triangle with no sides equal to each other.")
# 5th condition is to check for issoceles triangle.
else:
    print("Given triangle is a Issoceles triangle with two sides equal.")


    

