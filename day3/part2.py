CRITERIA = 2

if __name__ == "__main__":
    
    # Read text file into numbers within an array
    with open("day3/input_test.txt") as values:
         binary_input = values.readlines()

    width = len(binary_input[0]) - 1   
    # height = len(binary_input)        This variable changes as i remove numbers from the list! Can't hard code this in.
    
    binary_input_gamma = ""
    binary_input_epsilon = ""
    # Access each individual value in list.
    for c in range(width):
        count_0 = 0
        count_1 = 0
        removed = 0
        
        # Determines which bit shows up more often within each column
        # Convert logic into ternary expressions! Leo likes dat
        for r in range(len(binary_input)): 
            if int(binary_input[r][c]) == 0:
                count_0 = count_0 + 1
            if int(binary_input[r][c]) == 1:
                count_1 = count_1 + 1
        print(count_0)
        print(count_1)
        # Is a recursive function applicable? Or is that unnecessary with only 2 calls
        # Maybe create an array of 2 and have o2 and co2 bit criteria as the 2 values.  Encompass the already existing nested loop
    
        # co2_bit_criteria is always the opposite of o2_bit_criteria
        o2_bit_criteria = 0 if count_0 > count_1 else 1
        co2_bit_criteria = 1 if o2_bit_criteria == 0 else 0
        # Do I need to create a struct for bit_criteria?
        bit_criteria = o2_bit_criteria, co2_bit_criteria

        print(bit_criteria)
        print("Bit_criteria[0]: " + bit_criteria[0])
        print("Bit_criteria[1]: " + bit_criteria[1])
        for r in range(len(binary_input)):                                       
            for b in range(CRITERIA):
                # if bit_criteria == "o2_bit_criteria" then remove "if count_0 > count_1" ooooorrrr       
                if count_0 > count_1:
                    # if int(binary_input[r - removed][c]) == bit_criteria[b]:
                    #    print(bit_criteria[b]) 
                    if int(binary_input[r - removed][c]) == 1: 
                        print("Row Number: " + str(r - removed))
                        print("Number being removed: " + binary_input[r - removed])
                        print("Removed bit: " + str(binary_input[r - removed][c]))
                        binary_input.remove(binary_input[r - removed])
                        removed = removed + 1
                # if bit_criteria == "co2_bit_criteria" then remove "if count_1 > count_0" oooooorrrrr
                if count_1 > count_0:
                    # if int(binary_input[r - removed][c]) == bit_criteria[b]:
                    if int(binary_input[r - removed][c]) == 0: 
                        print("Row Number: " + str(r - removed))
                        print("Number being removed: " + binary_input[r - removed]) 
                        print("Removed bit: " + str(binary_input[r - removed][c]))
                        binary_input.remove(binary_input[r - removed])
                        removed = removed + 1
                if count_1 == count_0:                                      
                    if int(binary_input[r - removed][c]) == 0: 
                        print("Row Number: " + str(r - removed))
                        print("Number being removed: " + binary_input[r - removed]) 
                        print("Removed bit: " + str(binary_input[r - removed][c]))
                        binary_input.remove(binary_input[r - removed])
                        removed = removed + 1
            print("List" + str(binary_input))
            print("Length of string: " + str(len(binary_input)))
    print(binary_input)
    exit() 
    oxygen_generator = 0
    co2_scrubber = 0
    life_support = oxygen_generator * co2_scrubber
    print(life_support)