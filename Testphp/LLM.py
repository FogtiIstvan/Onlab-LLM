import sys

def main(arg1, arg2):
    # Convert the arguments to integers and calculate the sum
    sum = int(arg1) + int(arg2)

    # Print the sum
    print(sum)

# Call the main function with the command line arguments
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])