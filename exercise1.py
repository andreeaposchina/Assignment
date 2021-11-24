# Define a function that receive a string as argument and prints it backwards. For example, the
# string “Automation” gets printed as: “noitamotuA”

def return_reversed_first_method(word: str) -> str:
    """
    There are two ways of performing this action: one using Python slice operator, or the classical method.
    :param word: the string that the user wants to have it reverted
    :return: The reversed word
    """
    return word[::-1]


def return_reversed_second_method(word: str) -> str:
    reverted_string = ''
    for i in range(len(word) - 1, -1, -1):
        reverted_string += word[i]

    return reverted_string


print(return_reversed_first_method("Automation"))
print(return_reversed_second_method("Automation"))

print(return_reversed_first_method(""))
print(return_reversed_second_method(""))

print(return_reversed_first_method("AnaHasApples"))
print(return_reversed_second_method("AnaHasApples"))

