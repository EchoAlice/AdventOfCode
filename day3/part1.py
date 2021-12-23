if __name__ == "__main__":
    
    # Read text file into numbers within an array
    with open("day3/input_test.txt") as values:
        depths = values.readlines()

    # Why is len(depths[0]) = 6?
    col = len(depths[0]) - 1   
    row = len(depths)

    # Set empty array for values of each column
    count_0 = [0] * col
    count_1 = [0] * col
    gamma_rate = ""
    for i in range(row):
        string = depths[i]
        print("Row: " + str(i + 1))
        print("String: " + string)
        # Find most common bit in gamma rate
        # Access each individual value in list.
        for j in range(col):
            if int(string[j]) == 0:
                count_0[i] = count_0[i] + 1 
            if int(string[j]) == 1:
                count_1[i] = count_1[i] + 1
        print("Count_0 ++: " + str(count_0[i]))
        print("Count_1 ++: " + str(count_1[i]))

        # How do I add 1 or 0 to a string to create a binary number?
        #if count_0 > count_1:
        #    gamma_rate += str(0)
        #if count_0 < count_1:
        #    gamma_rate += str(1)
        #print("Gamma Rate: " + gamma_rate) 
    for i in range(col):
        # How do I add 1 or 0 to a string to create a binary number?
        if count_0[i] > count_1[i]:
            gamma_rate += str(0)
            print("Gamma Rate: " + gamma_rate)
        if count_0[i] < count_1[i]:
            gamma_rate += str(1)
            print("Gamma Rate: " + gamma_rate)    