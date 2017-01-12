# a program that accepts a user entered string, and returns the length of the string and says whether or not the string is even or odd
def strength():
    response= (input("Please enter a sentence: "))
    print("The length of your sentence is: " + str(len(response)))
    if len(response)%2 == 0:
        print("And the sentence is even.")
    else:
        print("And the sentence is odd.")


strength()

"""while True:
    try:
except len(response) == 0:
        print("You did not enter a valid sentence. Please enter a sentence.")
    continue

    except ValueError:
        print("You did not enter a valid sentence. Please enter a sentence.")
        continue
    else:
        break
    break"""
