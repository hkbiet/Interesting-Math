# Input a number
# Apply 3N+1 to if its odd.
# Divide by 2 if its even.
# Print the new number after each operation.
# Count the steps.
# Keep doing until we reduce the number to 1.
# Print all numbers reached till 1 and print the count.




def compute(number, count):
    if number == 1:
        print("FINALLY : ", number)
        print("FINAL COUNT : ", count)
        return
    
    if (number % 2 == 0):
        count = count + 1
        print("NUMBER: ", number, "    COUNT : ", count)
        number = number / 2
        compute(number, count)
    
    else:
        count = count + 1
        print("NUMBER: ", number,"    COUNT : ", count)
        number = (3 * number) + 1
        compute(number, count)


if __name__=="__main__":
    number = int(input("ENTER THY NUMBER: "))
    compute(number, 0)
