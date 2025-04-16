# min_max.py
# Name: Mutaz Al-shara
# Instructor: Rita M. Ghantous
# Date: April 16, 2025
# Class: Engr_103_401_S2025
# Description: This program asks the user for a number of integers, then finds and displays the minimum and maximum values among them.

def main():
    # Ask the user how many integers they would like to enter
    num_integers = int(input("How many integers would you like to enter? "))
    
    # Initialize variables to store the minimum and maximum values
    # Use the first input as the initial min and max
    print(f"Please enter {num_integers} integers.")
    first_number = int(input())
    min_value = first_number
    max_value = first_number
    
    # Loop to get the remaining integers
    for _ in range(1, num_integers):
        current_number = int(input())
        
        # Update min_value if the current number is smaller
        if current_number < min_value:
            min_value = current_number
        
        # Update max_value if the current number is larger
        if current_number > max_value:
            max_value = current_number
    
    # Display the minimum and maximum values
    print(f"min: {min_value}")
    print(f"max: {max_value}")

if __name__ == "__main__":
    main()