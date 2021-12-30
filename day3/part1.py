if __name__ == "__main__":
    
    # Read text file into numbers within an array
    with open("day3/input.txt") as values:
         binary_input = values.readlines()

    width = len(binary_input[0]) - 1   
    height = len(binary_input)
     
    binary_input_gamma = ""
    binary_input_epsilon = ""
    for c in range(width): 
        # Find most common bit in gamma rate                      
        # Access each individual value in list.                            # [5][12]
        count_0 = 0
        count_1 = 0
        for r in range(height): 
            # Calculates the number of times first bit of each number showed up
            count_0 += 1 if int(binary_input[r][c]) == 0 else count_0
            count_1 += 1 if int(binary_input[r][c]) == 1 else count_1
        # Reworded logic
        binary_input_gamma += str(0) if count_0 > count_1 else str(1)
        binary_input_epsilon += str(1) if count_0 > count_1 else str(0)

    #Convert
    gamma_rate = int(binary_input_gamma, 2)
    epsilon_rate =  int(binary_input_epsilon, 2)
    power_consumption = gamma_rate*epsilon_rate
    print(str(power_consumption)) 