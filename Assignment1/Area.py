# task is taking input from user and calculating the circle's Area

# Operates the mathemtical opertion of calculating of circle area
def circle_Area(radius):
    return round(((radius**2)*3.14),1)

# Takes the radius from user and calls the circle function
def main():
    i = float(input("Enter the radius: "))
    print(f'The corresponding area is {circle_Area(i)}')
   
    
main()
