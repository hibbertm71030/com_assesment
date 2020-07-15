# list of shapes

list_of_shapes = ["rectangle","square", "triangle", "circle"]

# imports
import numbers

# shape checker function

def shape_checker(question):
    error = "please use one of the following: rectangle, square, triangle, circle "

    valid = False
    while not valid:
        response = input(question)

        if response.lower() in list_of_shapes:
            return response.lower()

        elif response.lower() not in list_of_shapes:
            print(error)
            continue

# number only function
def number_only(question):
    error = "please use a number"

    valid = False
    while not valid:
        response = input(question)

        for letter in response:

            if letter.isdigit() == True:
                return response

            elif letter.isdigit() == False:
                print(error)
                continue


# ask user for shape
shape = shape_checker("What shape do you want to calculate for? ")

# ask user for dimensions
if shape == "rectangle":
    base = number_only("what is the base? (please use same units for base and height) ")
    height = number_only("what is the height? (please use same units for base and height) ")
    print("area = ",int(base) * int(height))
    print("perimeter =",int(base) + int(base) + int(height) + int(height))

if shape == "square":
    length = number_only("what is the length of the a side? ")
    print("area = ",int(length) * int(length))
    print("perimeter =",int(length) * 4)

