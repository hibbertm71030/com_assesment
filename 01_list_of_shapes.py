# list of shapes

list_of_shapes = ["rectangle","square", "triangle", "circle", "parallelogram"]

# ask user for shape
shape = input("What shape do you want to calculate for? ")

# shape checker function
def shape_checker():
    error = "please use one of the following: rectangle, square, triangle, circle, parallelogram"

    if shape not in list_of_shapes :
        print(error)
    input("What shape do you want to calculate for? ")


 if shape in list_of_shapes:
    print("you chose",shape)