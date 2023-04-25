# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 4

# Problem 3 - Ask for multiple lines from user and put it in text files

# Create  a file and open it
with open("mylife.txt", "a") as contents:
    # Use a while loop to ask the user for lines
    while True:
        # Ask the user to input lines
        line_ask = input("Enter line: ")
        # Write the lines in the text file
        contents.write(str(line_ask) + "\n")
        # Ask for another line
        line_more = input("More lines? yes/no: ")
        # if yes, continue
        if line_more == "yes":
            continue
        # elif no, break
        elif line_more == "no":
            break
        # else, put "invalid input"
        else:
            print("This is an invalid answer. Enter another input.")
            # Ask the user for a valid answer
            line_ask = input("More lines? yes/no: ")
            # If user input no, break
            if line_ask == "n":
                break