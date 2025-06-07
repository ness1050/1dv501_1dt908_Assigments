# A VG task
# To take a three number of integer and return the sum of those numbers

def sum(number):
    total = 0;
    while  (number > 0):
        digit = number % 10
        total += digit
        number = number // 10
    return total 

# main function
def main():
    userInput = int(input("Enter a three digit Number: "))
    print(f'The sum of three is: {sum(userInput)}')


main()
