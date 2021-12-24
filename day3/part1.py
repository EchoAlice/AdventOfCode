if __name__ == "__main__":
    
    # Read text file into numbers within an array
    with open("day3/input.txt") as values:
         binary_input = values.readlines()

    # Why is len(binary_input[0]) = 6?
    col = len(binary_input[0]) - 1   
    row = len(binary_input)
     
    binary_input_gamma = ""
    binary_input_epsilon = ""
    for i in range(col):
        #print("Column: " + str(i + 1))
        # Find most common bit in gamma rate                               # Why did changing binary_input[i][j] to binary_input[j][i] work?
        # Access each individual value in list.                            # [5][12]
        count_0 = 0
        count_1 = 0 
        for j in range(row): 
            # Calculates the number of times first bit of each number showed up
            if int(binary_input[j][i]) == 0:                                   
                count_0 = count_0 + 1 
            if int(binary_input[j][i]) == 1:                
                count_1 = count_1 + 1
        # When ith digit in binary_input is a 0
        if count_0 > count_1:
            binary_input_gamma += str(0)
            binary_input_epsilon += str(1)
        # When ith digit in binary_input is a 1
        if count_0 < count_1:
            binary_input_gamma += str(1)
            binary_input_epsilon += str(0)
    #Convert
    gamma_rate = int(binary_input_gamma, 2)
    epsilon_rate =  int(binary_input_epsilon, 2)
    power_consumption = gamma_rate*epsilon_rate
    print(str(power_consumption)) 