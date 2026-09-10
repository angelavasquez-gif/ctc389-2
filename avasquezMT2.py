#Angela Vasquez
#Midterm Program #2
#CTC 389

#Calculate the area of a rectangle using a function.

def RectangleArea(length, width):
    area = length * width
    return area

base = float(input("Enter the base of the rectangle: "))

height = float(input("Enter the height of the rectangle: "))

answer = RectangleArea(base, height)

print("The area of the rectangle is", answer)
