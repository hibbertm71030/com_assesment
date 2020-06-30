# list of shapes

list_of_shapes = ["rectangle","square", "triangle", "circle", "parallelogram"]


# shape checker function

def shape_checker(question):
    error = "please use one of the following: rectangle, square, triangle, circle, parallelogram"

    valid = False
    while not valid:
        response = input(question)

        if response.lower() in list_of_shapes:
            print("you chose {}".format(response.lower()))
            break


        elif response.lower() not in list_of_shapes:
            print(error)
            continue

# ask user for shape
shape = shape_checker("What shape do you want to calculate for? ")

