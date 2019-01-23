def main():
    # problem1()
    problem2()



# ### Problem 1:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ```q```.
# If the user doesn't enter ```q```, ask them to input another string.
#
# BONUS: Make sure the code can handle whatever case the User enters the ```q``` as (uppercase or lowercase).

def problem1():
    x = input(" Enter a word or phrase. Press 'q' to Quit")
    while True:
        if(x == "q" or x == "Q"):
            break
        else:
            x = input("Enter another word or phrase. Press 'q' to Quit")


# ### Problem 2:
# Write 2 functions: ```exercise2()``` and ```exercise2_helper(num1, num2, num3. operation)```
# The function ```exercise2_helper(num1, num2, num3)``` should expect 3 numbers, and
# an operation to perform as a String as parameters.
# The function should support 3 operations:
# * ```SUM``` - Return the sum of the 3 numbers
# * ```PROD``` - Return the product of the 3 numbers
# * ```AVG``` - Return the average of the 3 numbers
#
# The operation and the returned value should then be printed out back in the main ```exercise2()``` function
# Return ```INVALID OPERATION``` if an operation passed in that isn't supported. HINT: Use ```switch/case```
# #### Examples:
# ```
# exercise2_helper(2,4,6,"SUM")
# exercise2_helper(2,4,6,"PROD")
# exercise2_helper(2,4,6,"AVG")
# ```
# Expected Output:
# ```
# The SUM of 2,4,6 is 12
# The PROD of 2,4,6 is 48
# The AVG of 2,4,6 is 4
# ```

def problem2():

    # problem2_helper(2,4,6,"sum1")
    # problem2_helper(2,4,6,"avg")
    # problem2_helper(2,4,6,"prod")

    print(str("The product of 1, 2, 3, is ") + problem2_helper(1, 2, 3, "prod"))
    print(str("The average of 1, 2, 3, is ") + problem2_helper(1, 2, 3, "avg"))
    print(str("The sum of 1, 2, 3, is ") + problem2_helper(1, 2, 3, "sum1"))

def problem2_helper(num1, num2, num3, an):

    if(an == "sum1"):
        return str(num1 + num2 + num3)
    if(an == "avg"):
        return str((num1 + num2 + num3) / 3)
    if(an == "prod"):
        return str(num1 * num2 * num3)











if __name__ == '__main__':
    main()