if __name__ == "__main__":
    
    #Read text file into numbers within an array
    with open("input_test.txt") as values:
        depths = values.readlines()

    #Prints out value 1
    print(depths[0])

    list_length = len(depths)

    #Set up a for loop
    for i in range(list_length):
        print(depths[i])
