# list of shapes

list_of_shapes = ["rectangle","square", "triangle", "circle", "parallelogram"]


# shape checker function

def shape_checker(question):
    error = "please use one of the following: rectangle, square, triangle, circle, parallelogram"

    valid = False
    while not valid:
        response = input(question)

        if response.lower() in list_of_shapes:
            return response.lower()


        elif response.lower() not in list_of_shapes:
            print(error)
            continue

# not blank function
def not_blank(question):
    error = "please use a number"


    valid = False
    while not valid:
        response = input(question)

        if response is int:
            print("nice")
            return response

        elif response is not int:
            print(error)
            continue





# ask user for shape
shape = shape_checker("What shape do you want to calculate for? ")

if shape == "square":
    not_blank("what is the base? (please use same units for base and height) ")